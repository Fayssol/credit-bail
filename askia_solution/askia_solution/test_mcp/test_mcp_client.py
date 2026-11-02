import asyncio
import os
import sys
import traceback

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-u", "-m", "askia_admin.mcp_server"],
        cwd=r"C:\dev\credit-bail\askia_solution",
        env={
            **os.environ,
            "DJANGO_SETTINGS_MODULE": "askia_solution.settings",
        },
    )

    print("Démarrage du processus serveur MCP...")

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                print("Initialisation de la session MCP...")

                await session.initialize()

                print("Connexion MCP réussie !")

                # Découvrir les outils
                tools = await session.list_tools()

                print("\nOutils disponibles :")
                for tool in tools.tools:
                    print(f"- {tool.name}: {tool.description}")

                # Consulter la situation du client
                print("\nConsultation de la situation du client...")

                result = await session.call_tool(
                    "consulter_situation_client",
                    arguments={"nom_client": "client one"},
                )

                print("\nRésultat :")
                for item in result.content:
                    if hasattr(item, "text"):
                        print(item.text)

                if result.isError:
                    print("\nLe serveur a signalé une erreur.")

    except Exception:
        print("\nÉchec du test MCP.")
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
