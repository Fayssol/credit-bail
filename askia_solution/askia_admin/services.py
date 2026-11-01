from django.db.models import Sum
from django.shortcuts import get_object_or_404

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
