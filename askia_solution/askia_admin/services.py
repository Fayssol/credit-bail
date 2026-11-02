from django.db.models import Sum
from django.shortcuts import get_object_or_404
#

from datetime import date
from django.db import transaction
from .models import Contrat, Versement, Client


def obtenir_situation_contrat(nom_client: str) -> dict:
    """
    Retourne la situation financière d'un client à partir de son nom.
    """

    client = get_object_or_404(
        Client,
        nom__iexact=nom_client.strip()
    )

    contrat = get_object_or_404(
        Contrat.objects.select_related("client"),
        client=client
    )

    resultat = Versement.objects.filter(
        contrat=contrat
    ).aggregate(
        total_paye=Sum("montant_versement")
    )

    montant_paye = resultat["total_paye"] or 0
    montant_contrat = contrat.montant_contrat
    reste_a_payer = max(0, montant_contrat - montant_paye)

    return {
        "nom_client": client.nom,
        "contrat_id": contrat.id,
        "montant_contrat": montant_contrat,
        "montant_paye": montant_paye,
        "reste_a_payer": reste_a_payer,
        "etat_contrat": contrat.etat,
        "statut_paiement": contrat.status,
    }



@transaction.atomic
def enregistrer_versement_client(
    nom_client: str,
    montant: int,
    date_versement: str,
    note: str,
) -> dict:
    """
    Enregistre un versement pour un client.

    Vérifie le client, le contrat, le montant restant
    et l'état du contrat avant d'enregistrer le paiement.
    """

    # 1. Validation des paramètres
    nom_client = nom_client.strip()
    note = note.strip()

    if not nom_client:
        raise ValueError("Le nom du client est obligatoire.")

    if isinstance(montant, bool) or not isinstance(montant, int):
        raise ValueError("Le montant doit être un nombre entier.")

    if montant <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    if not note:
        raise ValueError("La note du versement est obligatoire.")

    try:
        date_paiement = date.fromisoformat(date_versement)
    except (ValueError, TypeError):
        raise ValueError(
            "La date doit respecter le format AAAA-MM-JJ."
        )

    # 2. Recherche du client
    clients = Client.objects.filter(nom__iexact=nom_client)

    if not clients.exists():
        raise ValueError(f"Client introuvable : {nom_client}")

    if clients.count() > 1:
        raise ValueError(
            "Plusieurs clients portent ce nom. "
            "Une identification plus précise est nécessaire."
        )

    client = clients.first()

    # 3. Recherche et verrouillage du contrat
    contrat = (
        Contrat.objects.select_for_update()
        .filter(client=client)
        .first()
    )

    if contrat is None:
        raise ValueError(
            f"Aucun contrat trouvé pour {client.nom}."
        )

    if contrat.etat != "ENCOURS":
        raise ValueError(
            f"Le contrat n'est pas en cours : {contrat.etat}."
        )

    # 4. Calcul du montant déjà payé
    resultat = Versement.objects.filter(
        contrat=contrat
    ).aggregate(
        total_paye=Sum("montant_versement")
    )

    montant_paye = resultat["total_paye"] or 0
    montant_contrat = contrat.montant_contrat
    reste_a_payer = montant_contrat - montant_paye

    if reste_a_payer <= 0:
        raise ValueError(
            "Ce contrat est déjà intégralement payé."
        )

    if montant > reste_a_payer:
        raise ValueError(
            f"Versement refusé. Solde restant : "
            f"{reste_a_payer} FCFA."
        )

    # 5. Création effective du versement
    versement = Versement.objects.create(
        contrat=contrat,
        montant_versement=montant,
        date_versement=date_paiement,
        note=note,
    )

    # 6. Calcul du nouveau solde
    nouveau_total = montant_paye + montant
    nouveau_reste = montant_contrat - nouveau_total

    # 7. Clôture du contrat si le montant total est atteint
    if nouveau_reste == 0:
        contrat.etat = "TERMINE"
        contrat.save(update_fields=["etat"])

    return {
        "succes": True,
        "message": "Versement enregistré avec succès.",
        "nom_client": client.nom,
        #"contrat_id": contrat.id,
        #"versement_id": versement.id,
        "montant_verse": montant,
        "date_versement": date_paiement.isoformat(),
        "montant_total_paye": nouveau_total,
        "montant_contrat": montant_contrat,
        "reste_a_payer": nouveau_reste,
        "etat_contrat": contrat.etat,
    }