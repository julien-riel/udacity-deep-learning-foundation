# Anaconda

Ce document explique comment installer et configurer anaconda

## Téléchargement et installation

https://www.continuum.io/downloads

> Note
>
> Si vous rencontrez des problèmes d'installation sous Windows, il se peut que la variable d'environement `PATH` soit trop longue

## Création d'un environnement de travail

conda create -n nom_environnement python=3 a [nom des packages]

`conda create -n titi python=3 pandas`

### Pour charger un environnement à partir d'un fichier ymal, on utilisera

`conda env create -f nom_fichier.yaml`

Ceci créer un environnement avec le nom indiquer dans le fichier.

> Note
>
> Il faut exécuter la ligne de commande en tant qu'administrateur si on rencontre une erreur `access denied`


## Activation / désactivation d'un environnement de travail
Sous Windows, il n'est pas nécessaire d'utiliser la commande conda 

### Activation
`activate titi`

### Désactivation
`deactivate titi`

## Lister les environnements de travail

`conda env list` 

## Suppression des environnements de travail
`conda env remove -n titi`

## Exportation d'un environnement
Exporte l'environnement dans un fichier yaml

`conda env export`

`conda env export > titi.yaml` 
