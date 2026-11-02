import asyncio
import json
import sys
from datetime import date
import traceback
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os
import sys


async def main():
    # 1. Configuration du serveur MCP
    server_params = StdioServerParameters(
           command=sys.executable,
           args=["-u", "-m", "askia_admin.mcp_server"],
           cwd=r"C:\dev\credit-bail\askia_solution",
           env={
               **os.environ,
               "DJANGO_SETTINGS_MODULE": "askia_solution.settings",
           },
       )

    try:
        # 2. Connexion au serveur MCP
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("\n===================================")
                print("      TEST VERSEMENT MCP")
                print("===================================")
                print("Connexion MCP réussie !")

                # 3. Découverte des outils
                result_tools = await session.list_tools()

                print("\nOutils disponibles :")
                for tool in result_tools.tools:
                    print(f"- {tool.name}: {tool.description}")

                tool_names = {
                    tool.name for tool in result_tools.tools
                }

                # Vérifier que l'outil existe
                tool_name = "enregistrer_versement"

                if tool_name not in tool_names:
                    print(
                        "\nERREUR : l'outil enregistrer_versement "
                        "n'est pas disponible."
                    )
                    print(
                        "Ajoute-le dans askia_admin/mcp_server.py "
                        "avant de relancer ce test."
                    )
                    return

                # 4. Saisie des données du versement
                print("\n--- Informations du versement ---")

                nom_client = input("Nom du client : ").strip()

                montant_texte = input(
                    "Montant du versement en FCFA : "
                ).strip()

                date_texte = input(
                    f"Date du versement (AAAA-MM-JJ, "
                    f"défaut {date.today().isoformat()}) : "
                ).strip()

                if not date_texte:
                    date_texte = date.today().isoformat()

                note = input("Note du versement : ").strip()

                # 5. Validation des saisies
                if not nom_client:
                    print("ERREUR : le nom du client est obligatoire.")
                    return

                try:
                    montant = int(montant_texte)
                except ValueError:
                    print("ERREUR : le montant doit être un entier.")
                    return

                if montant <= 0:
                    print("ERREUR : le montant doit être positif.")
                    return

                try:
                    date.fromisoformat(date_texte)
                except ValueError:
                    print(
                        "ERREUR : la date doit être au format "
                        "AAAA-MM-JJ."
                    )
                    return

                if not note:
                    print("ERREUR : la note est obligatoire.")
                    return

                # 6. Confirmation avant l'écriture en base
                print("\n--- Récapitulatif ---")
                print(f"Client   : {nom_client}")
                print(f"Montant  : {montant:,} FCFA".replace(",", " "))
                print(f"Date     : {date_texte}")
                print(f"Note     : {note}")

                confirmation = input(
                    "\nConfirmer l'enregistrement réel ? (oui/non) : "
                ).strip().lower()

                if confirmation not in {"oui", "o"}:
                    print("\nOpération annulée. Aucun appel d'écriture effectué.")
                    return

                # 7. Appel réel de l'outil MCP
                print("\nEnregistrement du versement...")

                result = await session.call_tool(
                    tool_name,
                    arguments={
                        "nom_client": nom_client,
                        "montant": montant,
                        "date_versement": date_texte,
                        "note": note,
                    },
                )

                # 8. Affichage du résultat
                print("\n--- Résultat MCP ---")

                for item in result.content:
                    if hasattr(item, "text") and item.text:
                        print(item.text)

                if result.isError:
                    print("\nLe serveur MCP a signalé une erreur.")
                else:
                    print("\nAppel MCP terminé sans erreur signalée.")

    except* Exception as e:
            print("\n========== ERREUR DÉTAILLÉE ==========")
            traceback.print_exception(e)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except* Exception as e:
        print("\n========== ERREUR DÉTAILLÉE ==========")
        traceback.print_exception(e)
