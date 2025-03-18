# 🚀 CI/CD Pipeline avec Jenkins et Docker

## 📌 Description
Ce projet met en place un pipeline CI/CD complet pour une application Python conteneurisée avec **Docker**, géré par **Jenkins**. 
Il suit ses étapes d'intégration et de déploiement continus :

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

### **Déploiement dans un environnement spécifique**

#### **1️⃣ Déploiement sur une VM (ex: AWS EC2, DigitalOcean, OVH)**
1. Connectez-vous à votre VM via SSH :
   ```bash
   ssh utilisateur@ip-de-la-vm
   ```
2. Installez Docker si ce n'est pas déjà fait :
   ```bash
   sudo apt update && sudo apt install -y docker.io
   ```
3. Récupérez et exécutez l'image Docker :
   ```bash
   docker pull votre-utilisateur-docker/mon-image
   docker run -d -p 5000:5000 votre-utilisateur-docker/mon-image
   ```

#### **2️⃣ Déploiement sur Kubernetes**
1. Assurez-vous que `kubectl` et `minikube` sont installés.
2. Démarrez Minikube (si local) :
   ```bash
   minikube start
   ```
3. Déployez l'application avec Kubernetes :
   ```bash
   kubectl apply -f deployment.yaml
   ```
4. Vérifiez le déploiement :
   ```bash
   kubectl get pods
   ```

#### **3️⃣ Déploiement sur Heroku**
1. Installez la CLI Heroku : [Télécharger ici](https://devcenter.heroku.com/articles/heroku-cli)
2. Connectez-vous à Heroku :
   ```bash
   heroku login
   ```
3. Ajoutez un `Procfile` avec :
   ```
   web: gunicorn app:app
   ```
4. Déployez avec :
   ```bash
   heroku create mon-app
   git push heroku main
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
 ├── 📜 deployment.yaml   # Configuration Kubernetes
```

---

## 📌 Auteur
- **Cathalina Ranaivoarison**
