# 20220131


Rapport TP1 - Docker

Introduction

Le but de ce TP était de créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude en utilisant OpenWeather API dans le langage de programmation de notre choix, de packager notre code dans une image Docker, de mettre à disposition cette image sur DockerHub et de mettre à disposition notre code dans un repository Github.

Étapes

Étape 1 : Création du repository Github

La première étape était de créer un repository Github avec mon identifiant EFREI. J'ai créé un nouveau repository public nommé 20220131 dans l'organisation sur Github.


Étape 2 : Création du wrapper

J'ai choisi d'utiliser Python pour créer mon wrapper, car c'est un langage que je maîtrise bien et qui dispose d'une bibliothèque requests pratique pour effectuer des appels API.

J'ai commencé par définir les variables d'environnement pour la latitude, la longitude et la clé API d'OpenWeather dans mon wrapper. Ensuite, j'ai utilisé la bibliothèque requests pour effectuer un appel à l'API OpenWeather avec les paramètres de latitude et de longitude.

Après avoir vérifié que la réponse de l'API était valide, j'ai extrait les informations de la réponse et j'ai renvoyé la météo du lieu demandé.

Étape 3 : Packaging du code dans une image Docker

J'ai créé un fichier Dockerfile à la racine de mon projet pour définir les instructions de construction de l'image Docker. J'ai choisi d'utiliser l'image Python 3.9 comme base pour mon image, car j'ai utilisé Python pour écrire mon wrapper.

J'ai copié mon code dans le conteneur Docker et j'ai installé la bibliothèque requests à l'aide de la commande RUN pip install requests. Enfin, j'ai défini la commande CMD pour exécuter mon wrapper lors du lancement de l'image.

Étape 4 : Mise à disposition de l'image sur DockerHub

J'ai créé un compte sur DockerHub et j'ai créé un nouveau repository public nommé  kymguzman/mydockerimage. J'ai ensuite exécuté les commandes suivantes pour créer et publier mon image Docker :

docker build . -t mydockerimage Build the container with a specific tag
docker login
docker tag mydockerimage kymguzman/mydockerimage Tag a Docker image to publish it
docker push kymguzman/mydockerimage Publish my docker image on a registry
docker pull kymguzman/mydockerimage

Etape 5 : Test

J'ai testé mon travail en utilisant la commande suivante docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY=**** kymguzman/mydockerimage qui m'a bien envoyé la météo du lieu dont la latitude et la longitude sont renseignées: The weather in your location is clear sky with a temperature of 28.01°C


TP2 DEVOPS - Docker-------------------------------------------------------------------------------------------------------------------------------------------
Introduction

L'objectif de ce TP était de configurer un workflow Github Action pour transformer un wrapper en API, publier automatiquement l'image sur Docker Hub et mettre l'image à disposition sous forme d'API sur Docker Hub, en mettant à disposition le code dans un repository Github.

Étapes de réalisation

Voici les étapes que j'ai suivies pour réaliser le TP:

Étape 1 : Configuration du workflow Github Action

J'ai modifié le Dockerfile du tp1 pour l'adapter au tp2.
J'ai commencé par créer un nouveau fichier YAML nommé ci.yml pour configurer le workflow Github Action. Ce fichier définit une action qui construit et pousse l'image Docker sur Docker Hub chaque fois qu'un push est effectué sur la branche principale. J'ai utilisé les actions Docker Hub pour me connecter à mon compte Docker Hub, installer Docker Buildx et construire et pousser l'image Docker efrei-devops-tp2

Étape 2 : Transformation d'un wrapper en API

J'ai ensuite créé une API qui utilise le wrapper pour obtenir les informations météorologiques de l'API OpenWeatherMap. J'ai utilisé le framework FastAPI pour créer cette API, en récupérant les informations de latitude et de longitude en tant que paramètres de requête, et en stockant la clé API dans une variable d'environnement.

Étape 3 : Publication automatique de l'image sur Docker Hub

J'ai configuré le workflow Github Action pour qu'il pousse automatiquement l'image Docker sur Docker Hub chaque fois qu'un push est effectué sur la branche principale.

Étape 4 : Mise à disposition de l'image sur DockerHub

J'ai publié mon image Docker sur Docker Hub pour qu'elle soit accessible au public.

Etape 5 : Test

J'ai ensuite exécuté les commandes suivantes pour tester mon travail :

docker run --network host --env API_KEY=**** kymguzman/efrei-devops-tp2
curl "http://localhost:8081/?lat=5.902785&lon=102.754175"