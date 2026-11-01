
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "askia_admin.mcp_server"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("Connexion MCP réussie !")

            # 1. Découvrir les outils
            tools = await session.list_tools()

            print("\nOutils disponibles :")
            for tool in tools.tools:
                print(f"- {tool.name}")

            # 2. Appeler notre outil MCP
            print("\nAppel de l'outil...")

            result = await session.call_tool(
                "consulter_situation_client",
                arguments={
                    "nom_client": "client one"
                }
            )

            # 3. Afficher le résultat
            print("\nRésultat de l'appel :")
            print(result.content)

            if result.isError:
                print("Une erreur est survenue pendant l'appel.")


if __name__ == "__main__":
    asyncio.run(main())
