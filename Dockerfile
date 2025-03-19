FROM python:3.12-slim

# Définir des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8180
ENV PYTHONPATH=/app

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Mettre à jour pip
RUN pip install --no-cache-dir --upgrade pip

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y git


# Installer flake8 pour le linting
#RUN pip install --no-cache-dir flake8 RUN pip install flake8==4.0.1

# Copier le reste du code source
COPY . .

# Exposer le port
EXPOSE $PORT

# Créer un volume pour les données persistantes
VOLUME ["/app-data"]

# Commande pour exécuter l'application
CMD gunicorn -b :$PORT -c gunicorn.conf.py main:app

