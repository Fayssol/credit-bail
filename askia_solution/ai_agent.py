
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from dotenv import load_dotenv
from openai import AsyncOpenAI

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# =====================================================
# 1. CONFIGURATION
# =====================================================

# Chemin du fichier ai_agent.py :
# credit-bail/askia_solution/ai_agent.py

BASE_DIR = Path(__file__).resolve().parent

# Chemin réel du fichier .env :
# credit-bail/askia_solution/askia_solution/.env

ENV_FILE = BASE_DIR / "askia_solution" / ".env"

load_dotenv(dotenv_path=ENV_FILE)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        f"OPENAI_API_KEY introuvable. Vérifie le fichier : {ENV_FILE}"
    )

openai_client = AsyncOpenAI(api_key=api_key)

MODEL = "gpt-5.4"

MAX_TOOL_ROUNDS = 5


# =====================================================
# 2. INSTRUCTIONS DE L'AGENT
# =====================================================

INSTRUCTIONS = """
Tu es MotoLease AI, un assistant intelligent spécialisé
dans la gestion des crédits-bails de motos.

Ton rôle est d'aider les utilisateurs à consulter les
informations relatives aux contrats et aux paiements.

RÈGLES :

1. Utilise les outils disponibles pour obtenir les
   informations financières des clients.

2. Ne fabrique jamais de données financières.

3. Ne suppose jamais qu'un paiement a été effectué
   sans confirmation provenant des outils.

4. Si un client est introuvable, explique-le clairement.

5. Présente les montants de manière lisible.

6. Réponds toujours en français.

7. Si les informations sont insuffisantes, demande
   les précisions nécessaires.
"""


# =====================================================
# 3. CONVERSION DES OUTILS MCP VERS OPENAI
# =====================================================

def convertir_outils_mcp(mcp_tools):

    openai_tools = []

    for tool in mcp_tools.tools:

        openai_tools.append({
            "type": "function",
            "name": tool.name,
            "description": tool.description or "",
            "parameters": tool.inputSchema,
            "strict": False
        })

    return openai_tools


# =====================================================
# 4. EXECUTION D'UN OUTIL MCP
# =====================================================

async def executer_outil_mcp(session, function_call):

    tool_name = function_call.name

    try:

        arguments = json.loads(function_call.arguments)

        print(f"\n[Agent] Outil demandé : {tool_name}")
        print(f"[Agent] Paramètres : {arguments}")

        # Appel réel du serveur MCP
        result = await session.call_tool(
            tool_name,
            arguments=arguments
        )

        # Extraction des résultats
        tool_output = "\n".join(
            item.text
            for item in result.content
            if hasattr(item, "text") and item.text
        )

        if result.isError:
            return (
                "Erreur lors de l'exécution de l'outil : "
                + tool_output
            )

        return tool_output or "Aucune donnée retournée par l'outil."

    except json.JSONDecodeError:

        return (
            "Erreur : les paramètres transmis par le modèle "
            "ne sont pas un JSON valide."
        )

    except Exception as error:

        return f"Erreur lors de l'exécution de l'outil : {str(error)}"


# =====================================================
# 5. BOUCLE PRINCIPALE DE L'AGENT
# =====================================================

async def main():

    # Configuration du serveur MCP
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "askia_admin.mcp_server"]
    )

    try:

        # Connexion au serveur MCP
        async with stdio_client(server_params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                print("\n===================================")
                print("           MOTOLEASE AI")
                print("===================================")

                print("\nConnexion MCP réussie !")

                # -------------------------------------
                # Découverte dynamique des outils MCP
                # -------------------------------------

                mcp_tools = await session.list_tools()

                openai_tools = convertir_outils_mcp(mcp_tools)

                available_tools = {
                    tool.name for tool in mcp_tools.tools
                }

                print(f"\nOutils chargés : {len(openai_tools)}")

                for tool in mcp_tools.tools:
                    print(f"- {tool.name}")

                # -------------------------------------
                # Question de l'utilisateur
                # -------------------------------------

                question = input("\nVous : ").strip()

                if not question:
                    print("Veuillez saisir une question.")
                    return

                input_items = [
                    {
                        "role": "user",
                        "content": question
                    }
                ]

                # -------------------------------------
                # Première requête à OpenAI
                # -------------------------------------

                response = await openai_client.responses.create(
                    model=MODEL,
                    instructions=INSTRUCTIONS,
                    input=input_items,
                    tools=openai_tools,
                    tool_choice="auto"
                )

                # -------------------------------------
                # Boucle d'exécution des outils
                # -------------------------------------

                for round_number in range(MAX_TOOL_ROUNDS):

                    function_calls = [
                        item
                        for item in response.output
                        if item.type == "function_call"
                    ]

                    # Aucun outil demandé
                    if not function_calls:
                        break

                    print(
                        f"\n[Agent] Cycle d'exécution "
                        f"{round_number + 1}/{MAX_TOOL_ROUNDS}"
                    )

                    # Conserver la réponse du modèle
                    input_items.extend(response.output)

                    # Exécuter les outils demandés
                    for function_call in function_calls:

                        if function_call.name not in available_tools:

                            tool_output = (
                                f"Erreur : outil inconnu "
                                f"{function_call.name}"
                            )

                        else:

                            tool_output = await executer_outil_mcp(
                                session,
                                function_call
                            )

                        # Retour du résultat à OpenAI
                        input_items.append({
                            "type": "function_call_output",
                            "call_id": function_call.call_id,
                            "output": tool_output
                        })

                    # Nouvelle requête après les appels MCP
                    response = await openai_client.responses.create(
                        model=MODEL,
                        instructions=INSTRUCTIONS,
                        input=input_items,
                        tools=openai_tools,
                        tool_choice="auto"
                    )

                else:

                    print(
                        "\n[Agent] Limite maximale de cycles "
                        "d'exécution atteinte."
                    )

                # -------------------------------------
                # Réponse finale
                # -------------------------------------

                print("\n===================================")
                print("             RÉPONSE")
                print("===================================\n")

                print(response.output_text)

    except Exception as error:

        print("\nUne erreur est survenue :")
        print(str(error))


# =====================================================
# 6. POINT D'ENTRÉE
# =====================================================

if __name__ == "__main__":
    asyncio.run(main())
