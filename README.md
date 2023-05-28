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




-------------------------------------TP3 Cloud - ACI---------------------------------------------------------------

Ce rapport présente les étapes suivies pour mettre en place un déploiement automatisé d'une application conteneurisée sur Azure Container Instance (ACI) en utilisant GitHub Actions. Il détaille les choix techniques effectués et les difficultés rencontrées tout au long du processus.

Étapes suivies:

    Création du Repository GitHub: J'ai créé un nouveau repository sur GitHub pour héberger le code de l'application. https://github.com/efrei-ADDA84/20220131_TP3

    Configuration de l'environnement local: J'ai configuré mon environnement de développement en installant Docker et les dépendances nécessaires pour l'application (requests, uvicorn, fastapi).

    Mise en place du Dockerfile: J'ai rédigé un Dockerfile qui définit l'image Docker de l'application. Le Dockerfile copie les fichiers de l'application dans le conteneur, installe les dépendances Python à l'aide de pip, et définit la commande pour exécuter l'API à l'aide d'Uvicorn. 

    Test de l'application en local: J'ai testé l'application en local pour m'assurer qu'elle fonctionne correctement avant de la déployer sur Azure. J'ai utilisé des requêtes CURL pour vérifier les réponses de l'API et m'assurer qu'elle renvoie les données météo attendues.

    Configuration des secrets GitHub: Les secrets nécessaires à l'exécution du workflow de déploiement automatisé ont été ajouté. Les secrets contenant les informations d'authentification Azure (AZURE_CREDENTIALS, REGISTRY_LOGIN_SERVER, REGISTRY_USERNAME, REGISTRY_PASSWORD) ont été ajoutées par le professeur via l'organisation et j'ai ajouté le secret qui contient la clé d'API OpenWeatherMap (API_KEY).

    Mise en place du workflow GitHub Actions: J'ai créé un fichier de workflow GitHub Actions manuellement sur github pour automatiser le processus de build et de déploiement de l'application sur Azure. Le workflow est déclenché à chaque push sur la branche principale (main). Il utilise les actions GitHub pour effectuer les étapes suivantes:
        Checkout du code source du repository.
        Connexion à Azure en utilisant les informations d'authentification.
        Construction de l'image Docker et son push vers Azure Container Registry (ACR).
        Déploiement de l'image sur Azure Container Instance (ACI) en utilisant les paramètres spécifiés (resource group, DNS name label, etc.).

    Exécution du workflow: J'ai déclenché le workflow GitHub Actions lors de mon premier commit du worflow, lorsque j'ai commité les modifications que j'ai apportées au workflow et à chaque fois que j'ai pushé sur la branche principale. J'ai suivi les logs et les résultats des différentes étapes pour m'assurer que le processus de build et de déploiement s'est déroulé avec succès.

Intérêt de l'utilisation de GitHub Actions pour le déploiement :

L'utilisation de GitHub Actions pour automatiser le processus de déploiement présente plusieurs avantages significatifs :

    Automatisation du processus : GitHub Actions permet d'automatiser le processus de build, de test et de déploiement de l'application. Une fois le workflow de déploiement configuré, il est déclenché automatiquement à chaque push sur la branche principale, ce qui évite d'avoir à effectuer manuellement ces tâches répétitives.

    Facilité d'intégration avec le workflow de développement : GitHub Actions est étroitement intégré avec GitHub, ce qui facilite la mise en place d'un workflow de développement continu. Les développeurs peuvent travailler sur leurs branches, effectuer des pushs réguliers et avoir la certitude que l'application sera déployée automatiquement dès que les modifications sont validées sur la branche principale.

    Reproductibilité et traçabilité : En utilisant un workflow de déploiement basé sur GitHub Actions, le processus de déploiement est reproductible à chaque push. Chaque étape est documentée et traçable grâce aux logs et aux résultats des actions exécutées. Cela facilite la collaboration entre les membres de l'équipe et permet de revenir en arrière en cas de problème.

    Gestion des secrets et sécurité : GitHub Actions offre une gestion intégrée des secrets via les secrets GitHub. Les informations sensibles, telles que les informations d'authentification Azure, peuvent être stockées de manière sécurisée et utilisées dans les workflows sans les exposer directement dans les fichiers de configuration. Cela renforce la sécurité et permet de partager facilement les workflows sans divulguer les informations sensibles.

Apports du TP et apprentissages :

Ce TP m'a permis d'acquérir plusieurs connaissances et compétences clés :

    Gestion des conteneurs avec Docker : J'ai appris à créer un fichier Dockerfile pour définir l'environnement d'exécution de mon application et à utiliser Docker pour construire et exécuter des conteneurs.

    Déploiement sur Azure Container Instance (ACI) : J'ai appris à déployer des conteneurs sur Azure en utilisant Azure Container Instance (ACI). J'ai compris les concepts clés liés au déploiement et à la gestion des conteneurs sur une plateforme cloud.

    Automatisation du déploiement avec GitHub Actions : J'ai découvert comment configurer un workflow GitHub Actions pour automatiser le processus de build et de déploiement de l'application. J'ai compris les avantages de cette approche et la manière de l'intégrer dans un flux de développement continu.

    Gestion des secrets avec GitHub Actions : J'ai appris à utiliser les secrets GitHub pour gérer de manière sécurisée les informations sensibles nécessaires au déploiement de l'application. J'ai compris l'importance de protéger ces informations et de les gérer de manière centralisée.