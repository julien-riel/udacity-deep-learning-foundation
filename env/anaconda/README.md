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

> Note
>
> Il faut exécuter la ligne de commande en tant qu'administrateur si on rencontre une erreur `access denied`


## Activation d'un

## Lister les environnements de travail

`conda env list` 