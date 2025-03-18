# CI/CD Pipeline avec Jenkins et Docker

Ce projet met en place un pipeline CI/CD complet pour une application Python conteneurisée avec Docker, géré par Jenkins.

## Objectif
Automatiser le cycle de vie d'une application comprenant les étapes suivantes :

### Intégration Continue (CI) :
- **Build** : Construction de l'image Docker.
- **Qualité du Code** : Analyse statique du code avec Flake8.
- **Tests** : Exécution des tests unitaires avec pytest.
- **Package** : Empaquetage du code dans une image Docker.

### Déploiement Continu (CD) :
- **Revue/Test** : Déploiement dans un environnement de test pour validation.
- **Staging** : Déploiement dans un environnement simulant la production.
- **Production** : Déploiement final accessible aux utilisateurs.

## Architecture du Pipeline

### CI Pipeline
1. **Code** : Écriture et versionnage du code dans un référentiel Git.
2. **Build** : Construction de l'image Docker.
3. **Qualité du Code** : Analyse statique du code avec Flake8.
4. **Tests** : Exécution des tests unitaires avec pytest.
5. **Package** : Empaquetage du code dans une image Docker.

### CD Pipeline
1. **Revue/Test** : Déploiement dans un environnement de test pour validation.
2. **Staging** : Déploiement dans un environnement simulant la production.
3. **Production** : Déploiement final accessible aux utilisateurs.

## Prérequis
- Docker
- Jenkins
- Accès à un registre Docker (ex: Docker Hub)
- Environnement de déploiement (ex: Heroku, VM locale, etc.)

## Installation
1. Clonez le référentiel :
   ```sh
   git clone https://github.com/votre-repo/ci-cd-pipeline.git
   cd ci-cd-pipeline
   ```
2. Configurez les variables d'environnement dans Jenkins.
3. Lancez le pipeline.

## Utilisation
Pour lancer le pipeline, poussez simplement votre code dans le dépôt. Jenkins déclenchera automatiquement les étapes CI/CD.

## Structure du Projet
```
ci-cd-pipeline/
├── app/                 # Code source de l'application
├── Dockerfile           # Fichier de configuration Docker
├── Jenkinsfile          # Définition du pipeline Jenkins
├── tests/               # Tests unitaires
└── README.md            # Documentation
```

## Auteur
**Cathalina Ranaivoarison**
