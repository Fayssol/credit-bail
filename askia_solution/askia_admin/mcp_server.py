import os

import django
from asgiref.sync import sync_to_async
from mcp.server.fastmcp import FastMCP

# 1. Configurer Django avant d'importer les modèles ou services
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "askia_solution.settings",
)

# 2. Initialiser Django
django.setup()

# 3. Importer les services Django après l'initialisation
from askia_admin.services import (
    obtenir_situation_contrat,
    enregistrer_versement_client,
)

# 4. Créer le serveur MCP
mcp = FastMCP("MotoLease Server")


@mcp.tool()
async def consulter_situation_client(nom_client: str) -> dict:
    """
    Consulte la situation financière d'un client :
    montant du contrat, montant payé, solde restant
    et statuts du contrat.
    """
    return await sync_to_async(
        obtenir_situation_contrat,
        thread_sensitive=True,
    )(nom_client)


@mcp.tool()
async def enregistrer_versement(
    nom_client: str,
    montant: int,
    date_versement: str,
    note: str,
) -> dict:
    """
    Enregistre un versement pour un client identifié par son nom.

    Args:
        nom_client: Nom du client.
        montant: Montant du versement en FCFA.
        date_versement: Date au format AAAA-MM-JJ.
        note: Motif ou commentaire du versement.
    """
    return await sync_to_async(
        enregistrer_versement_client,
        thread_sensitive=True,
    )(
        nom_client=nom_client,
        montant=montant,
        date_versement=date_versement,
        note=note,
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
