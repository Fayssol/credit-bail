
import os
import django

from asgiref.sync import sync_to_async
from mcp.server.fastmcp import FastMCP

# Initialisation de Django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "askia_solution.settings"
)

django.setup()

from askia_admin.services import obtenir_situation_contrat

# Création du serveur MCP
mcp = FastMCP("MotoLease Server")


@mcp.tool()
async def consulter_situation_client(nom_client: str) -> dict:
    """
    Consulte la situation financière d'un client.

    Retourne le montant du contrat, le montant payé,
    le solde restant et les statuts du contrat.
    """

    situation = await sync_to_async(
        obtenir_situation_contrat,
        thread_sensitive=True
    )(nom_client)

    return situation


if __name__ == "__main__":
    mcp.run(transport="stdio")
