# Introduction

Vous développez le système de suivi des ventes de la multinationale ACME. Cette entreprise vend des articles auxquels sont associées les informations suivantes :
* Code unique de l’article (3 lettres suivies de 3 chiffres, par ex. ABC123)
* Catégorie (plusieurs articles peuvent avoir la même catégorie)
* Nom
* Coût de fabrication

Les informations suivantes sont également enregistrées pour chaque vente (une vente concerne un seul article à la fois) :
* Date de la vente (jour)
* Auteur de la saisie
* Article
* Quantité
* Prix de vente unitaire

Les prix sont exprimés dans une unité arbitraire (pas de notion de devise à gérer).

# Consignes

Vous devez implémenter une API REST utilisable par un développeur front qui permet à un utilisateur :
* De se connecter.
* D'ajouter une vente.
* De modifier une vente s'il en l'auteur.
* De lister les ventes (date, catégorie article, code article, nom article, quantité, prix de vente unitaire, prix de vente total), paginées par 25 éléments.
* Bonus : de lister les articles avec leur catégorie, le total des ventes pour cet article, le pourcentage de marge pour cet article, la date de la dernière vente pour cet article, le tout ordonné par total des ventes décroissants.

Les opérations CRUD sur les articles/ventes doivent également être possibles depuis l'admin de Django, sans notion particulière de permissions.

# Pour démarrer

Le dépôt contient un projet Django prêt à être utilisé pour réaliser l'exercice (il s'agit d'une version simplifiée de la structure de nos projets internes). Pour démarrer :
* Cloner ce dépôt.
* Créer un environnement virtuel Python 3.
* Installer les dépendances avec `pip install -r requirements.txt`.

À noter :
* Écrivez le code de l'exercice comme vous écririez du code de production.
* L'utilisation de `djangorestframework` et `dj-rest-auth` est encouragée mais pas obligatoire.
* Un modèle pour les utilisateurs existe déjà (`users.User`) et peut être utilisé et vous pouvez vous connecter avec `candidat@vingtcinq.io` / `motdepasse`.
* La base de données a également déjà été initialisée avec 1000 ventes.

# Soumettre votre solution

Merci de nous envoyer un lien vers votre solution par email.
