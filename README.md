
# Projet credit bail de moto
**Projet de Recouvrement des dettes (credit bail de moto) en django utilisant postgresql/SQLite comme base de données** 
## Fonctionalites
- Enregistrement de contrat
- Enregistrement des reglements de client
- Consultation du status des reglements et l'etat du contrat

## Objectif 
Manipulation de projet Django et du concept MCP/agents AI

## Installation et Configuration de postgresql sous Linux
Lire le fichier installation.txt

## Serveur MCP (Model Context Protocol)

### Présentation

Le projet intègre un serveur MCP permettant à un agent IA d'interagir avec les fonctionnalités métier de l'application Django.

Le serveur MCP expose des outils qui permettent notamment de consulter la situation financière d'un client et d'enregistrer ses versements.

L'objectif est de rendre les fonctionnalités métier accessibles à un agent IA sans lui donner un accès direct à la base de données.

### Architecture

L'architecture repose sur les composants suivants :

- **Django** : application métier et gestion des données.
- **Services Django** : contiennent la logique métier.
- **Serveur MCP** : expose les services Django sous forme d'outils.
- **Client MCP** : se connecte au serveur et exécute les outils disponibles.
- **Agent IA** : exploite les outils MCP pour répondre aux demandes de l'utilisateur.

### Outils MCP disponibles

#### 1. Consulter la situation d'un client

Nom de l'outil : `consulter_situation_client`

Cet outil permet de retrouver la situation financière d'un client à partir de son nom.

Paramètre :

| Paramètre | Type | Description |
|---|---|---|
| `nom_client` | `str` | Nom du client à rechercher |

Informations retournées :

- Nom du client
- Identifiant du contrat
- Montant total du contrat
- Montant déjà payé
- Solde restant à payer
- État du contrat
- Statut des paiements

Exemple de résultat :

```json
{
    "nom_client": "client one",
    "contrat_id": 1,
    "montant_contrat": 500000,
    "montant_paye": 20000,
    "reste_a_payer": 480000,
    "etat_contrat": "ENCOURS",
    "statut_paiement": "AJOUR"
}




### 2. Documentation de l'agent IA (`ai_agent.py`)

```md
## Agent IA

### Présentation

Le projet intègre un agent IA permettant à un utilisateur d'interagir avec les fonctionnalités de l'application en langage naturel.

Au lieu de devoir naviguer dans l'interface Django ou connaître les identifiants techniques des contrats, l'utilisateur peut simplement poser une question ou formuler une demande.

Exemples :

- Quelle est la situation financière de client one ?
- Combien ce client a-t-il déjà payé ?
- Quel est le solde restant de son contrat ?
- Je souhaite enregistrer un versement de 50 000 FCFA pour ce client.

L'agent IA analyse la demande, identifie l'outil MCP approprié et lui transmet les paramètres nécessaires.

### Architecture de l'agent

L'architecture globale est organisée comme suit :

```text
                    UTILISATEUR
                         |
                         v
                     AGENT IA
                    ai_agent.py
                         |
                         v
                  MODÈLE DE LANGAGE
                       (LLM)
                         |
                         v
                    CLIENT MCP
                         |
                         v
                   SERVEUR MCP
                  mcp_server.py
                         |
                         v
                  SERVICES DJANGO
                    services.py
                         |
                         v
                   BASE DE DONNÉES
                       SQLite