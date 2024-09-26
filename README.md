# Projet de Comptage de Mots

Ce projet Python permet de lire un fichier texte, de compter les occurrences de chaque mot et d'afficher soit tous les mots avec leur fréquence, soit uniquement les 20 mots les plus fréquents.

## Table des Matières

- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Option --count](#option---count)
  - [Option --topcount](#option---topcount)
- [Fonctions Principales](#fonctions-principales)
  - [word_count_dict()](#word_count_dict)
  - [print_words()](#print_words)
  - [get_count()](#get_count)
  - [print_top()](#print_top)
  - [main()](#main)
- [Concepts Abordés](#concepts-abordés)
- [Liens vers la Documentation](#liens-vers-la-documentation)
- [Auteur](#auteur)

## Introduction

Ce projet est une démonstration de compétences en manipulation de fichiers, en traitement de texte et en comptage de fréquences de mots. Il utilise les fonctions de base de Python telles que la lecture de fichiers, les dictionnaires et le tri de données. Le script peut être exécuté avec deux options :
- `--count` : Affiche tous les mots et leur fréquence.
- `--topcount` : Affiche les 20 mots les plus fréquents.

## Prérequis

- Python 3 installé sur votre machine
- Un fichier texte (fichier `.txt`) à analyser

## Installation

1. Clonez ce dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/ikitamalarose/comptage-mots-python-youtube.git
    ```
2. Naviguez dans le répertoire du projet :
    ```bash
    cd comptage-mots-python-youtube
    ```
3. Assurez-vous que vous avez Python installé en exécutant :
    ```bash
    python --version
    ```

## Utilisation

Le programme se lance via la ligne de commande avec les options `--count` ou `--topcount` et le nom du fichier à analyser. Voici les exemples d'utilisation :

### Option --count

Affiche tous les mots et leur nombre d'occurrences dans l'ordre alphabétique :
```bash
python wordcount.py --count fichier.txt

```

### Option --topcount
Affiche les 20 mots les plus fréquents avec leur nombre d'occurrences :

```bash
python wordcount.py --topcount fichier.txt

```

### Fonctions Principales
`word_count_dict(filename)`
- Description : Lit le fichier donné, divise le texte en mots et crée un dictionnaire avec les mots en tant que clés et le nombre d'occurrences en tant que valeurs.
- Utilisation : Cette fonction est appelée par print_words() et print_top() pour obtenir les données de base.
Retourne : Un dictionnaire ``dict`.

`print_words(filename)`
- Description : Affiche tous les mots du fichier et leur nombre d'occurrences dans l'ordre alphabétique.
- Utilisation : Appelée quand l'option --count est utilisée.

`get_count(word_count_tuple)`
- Description : Prend un tuple (mot, fréquence) et retourne la fréquence. Utilisée pour trier les mots par fréquence.
- Utilisation : Fonction de tri utilisée par print_top().

`print_top(filename)`
- Description : Affiche les 20 mots les plus fréquents dans le fichier, avec leur nombre d'occurrences, triés du plus fréquent au moins fréquent.
- Utilisation : Appelée quand l'option --topcount est utilisée.

`main()`
- Description : Fonction principale qui gère les arguments de la ligne de commande et appelle soit print_words(), soit print_top(), en fonction de l'option spécifiée.
- Utilisation : Cette fonction est automatiquement appelée lorsque le script est exécuté directement.

### Concepts Abordés
- Manipulation de fichiers : Lecture de fichiers texte, fermeture des fichiers après utilisation.
- Dictionnaires en Python : Utilisés pour stocker les mots et leurs occurrences.
- Tri personnalisé : Utilisation de la fonction `sorted()` avec un paramètre de tri personnalisé `(key=get_count)`.
- Arguments de ligne de commande : Gestion des arguments avec `sys.argv` pour permettre différentes options lors de l'exécution du script.
- Traitement de texte : Transformation du texte en minuscules pour assurer que les mots sont traités de manière uniforme.

### Liens vers la Documentation
- [Documentation geeksforgeeks](https://www.geeksforgeeks.org/python-sys-module/): sys module : Utilisation des arguments de ligne de commande avec sys.argv.
- [Documentation w3school](https://www.w3schools.com/python/ref_func_open.asp): open() function : Fonction pour ouvrir des fichiers.
- [Documentation w3school](https://www.w3schools.com/PYTHON/python_dictionaries.asp): Dictionaries : Manipulation des dictionnaires pour stocker les données.
- [Documentation w3school](https://www.w3schools.com/python/ref_func_sorted.asp): sorted() function : Explication de la fonction sorted() et des tris personnalisés.
- [Documentation w3school](https://www.w3schools.com/python/ref_string_split.asp): split() function : Comment diviser une chaîne de caractères en mots.

### Auteur
- GitHub - [@ikitamalarose](https://github.com/ikitamalarose)
- Email - [laroseikitama@gmail.com](mailto:laroseikitama@gmail.com)