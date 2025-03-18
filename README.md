# 🚀 CI/CD Pipeline avec Jenkins et Docker

## 📌 Description
Ce projet met en place un pipeline CI/CD complet pour une application Python conteneurisée avec **Docker**, géré par **Jenkins**. Il suit ses étapes d'intégration et de déploiement continus :

### 1️⃣ **CI Pipeline (Continuous Integration)**
- **Code** : Versionnage du code dans un référentiel Git.
- **Build** : Construction de l'image Docker.
- **Qualité du Code** : Analyse statique du code avec Flake8.
- **Tests** : Exécution des tests unitaires avec pytest.
- **Package** : Empaquetage du code dans une image Docker.

### 2️⃣ **CD Pipeline (Continuous Deployment/Delivery)**
- **Revue/Test** : Déploiement dans un environnement de test pour validation.
- **Staging** : Déploiement en environnement de pré-production.
- **Production** : Déploiement final accessible aux utilisateurs.

---

## 📌 Prérequis
Avant de commencer, assurez-vous d'avoir installé :

- [Jenkins](https://www.jenkins.io/download/)
- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- Un compte [Docker Hub](https://hub.docker.com/) pour héberger les images.

---

## 📌 Installation & Configuration

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/votre-repo/ci-cd-pipeline.git
cd ci-cd-pipeline
```

### 2️⃣ **Configuration de Jenkins**
1. Installer Jenkins avec Docker :
   ```bash
   docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
   ```
2. Accéder à **http://localhost:8080**, entrer le mot de passe initial et installer les plugins nécessaires.
3. Ajouter **un pipeline freestyle** ou utiliser un **Jenkinsfile**.

### 3️⃣ **Exécution du pipeline**
Lancer le pipeline sur Jenkins pour exécuter les étapes CI/CD.

---

## 📌 Déploiement

### **Via Docker**
```bash
docker build -t mon-image .
docker run -d -p 5000:5000 mon-image
```

---

## 📌 Structure du projet
```
📂 ci-cd-pipeline
 ├── 📜 README.md         # Documentation
 ├── 📜 Jenkinsfile       # Pipeline CI/CD
 ├── 📜 Dockerfile        # Image Docker
 ├── 📂 app/              # Code source de l'application
 ├── 📂 tests/            # Tests unitaires
```

---

## 📌 Auteur
- **Cathalina Ranaivoarison**
