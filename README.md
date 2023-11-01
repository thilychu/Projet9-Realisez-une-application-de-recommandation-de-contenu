# Projet 9: "Réalisez une application de recommandation de contenu"

## Missions

- Tester différentes approches de modélisation pour la recommandation des articles

- Développer une première version de système de recommandation sous forme d’Azure Functions

- Réaliser une application simple de gestion du système de recommandation 

- Définir un architecture cible pour pouvoir prendre en compte l’ajout de nouveaux utilisateurs ou de nouveaux articles


## Données

Le jeu de données est disponible [ici](https://www.kaggle.com/datasets/gspmoreira/news-portal-user-interactions-by-globocom#clicks_sample.csv).

## Installation

### Prérequis

- [Python 3.11](https://www.python.org/downloads/)

### Environnement virtuel

```bash
python -m venv env
```

### Dépendances

```bash
pip install -r requirements.txt
```

## Développer une application de recommandation reposant sur une architecture serverless en utilisant Azure Function

### Développer une première version du système de recommandation à l'aide d'Azure Functions
- Créer une Azure Function dédiée à la mise en œuvre de l'algorithme de recommandation.

- Déclencher cette fonction en réponse aux demandes HTTP contenant l'ID de l'utilisateur.

- La fonction renvoie une liste de 5 articles recommandés spécifiques à l'utilisateur.


### Réaliser une application de gestion conviviale du système de recommandation
- Concevoir une interface utilisateur qui permet à l'utilisateur de sélectionner un ID d'utilisateur.

- Lorsqu'un ID d'utilisateur est choisi, l'application interagit automatiquement avec les Azure Functions appropriées pour obtenir les recommandations

