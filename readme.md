# ☀️ Séchoire - Planificateur de Sèche Parfaite

Le **Séchoire** est une application Python interactive conçue pour les passionnés de musculation et de fitness qui souhaitent planifier leur perte de gras avec une précision mathématique. L'objectif est simple : déterminer exactement quand commencer votre régime pour être prêt au pic de la forme pour le début de l'été (le 21 juin).

## 🎯 La Philosophie du Projet

Le but n'est pas seulement de perdre du poids, mais de le faire de manière **optimale** et **prévisible**.

### La règle du 1%

L'application repose sur le consensus scientifique en nutrition sportive : pour préserver un maximum de masse musculaire tout en perdant du gras, il est conseillé de viser une perte de **1% de son poids total par semaine**.

- Si vous pesez 100 kg, vous perdez 1 kg la première semaine.
- Si vous pesez 90 kg, vous visez 0,9 kg la semaine suivante.
  C'est cette décroissance logarithmique qui est calculée par l'algorithme pour donner une durée réaliste.

### L'objectif "Été"

Pourquoi le 21 juin ? C'est la date symbolique du début de l'été. L'application calcule automatiquement quel est le prochain 21 juin atteignable en fonction de votre poids actuel. Si votre objectif demande 80 semaines, l'app ne vous dira pas de commencer dans le passé, elle calculera l'été de l'année suivante (2027, 2028, etc.).

## 🛠️ Caractéristiques Techniques

L'application a été développée en **Python** avec plusieurs bibliothèques clés :

### 1. Interface Graphique (Tkinter & Canvas)

- **Design Moderne** : Utilisation d'un système de "Canvas" pour dessiner des rectangles arrondis avec contours, dépassant les limites de design classiques de Tkinter.
- **Responsive** : L'image de fond (`summer.webp`) se redimensionne dynamiquement selon la taille de la fenêtre sans déformer les éléments de saisie.
- **Feedback visuel** : Gestion des erreurs en temps réel (chiffres invalides, poids cible supérieur au poids actuel) avec des messages colorisés.

### 2. Logique de Date Avancée

- **Calcul Dynamique** : Contrairement à un calcul fixe, l'application utilise une boucle `while`. Elle vérifie si la date de début de régime est déjà passée. Si c'est le cas, elle incrémente l'année de l'objectif (21 juin) jusqu'à trouver une date de départ située dans le futur.
- **Formatage Local** : Pour éviter les bugs d'affichage d'accents courants sur Windows (UTF-8), les mois sont gérés par une liste interne personnalisée.

### 3. Audio & Multimédia

- **Ambiance sonore** : Intégration de `pygame.mixer` pour jouer un thème emblématique (`scarface.wav`) et te mettre le démon! Après le résultat, je garantis que tu feras au moins 10 pompes.
- **Boucle Infinie** : La musique est configurée avec le paramètre `-1` pour tourner en boucle tant que l'application est ouverte.
- **Traitement d'Image** : Utilisation de la bibliothèque `Pillow` (PIL) pour la gestion du fond d'écran et l'insertion d'images dans les widgets de texte.

## 🚀 Installation et Utilisation

### Prérequis

- Python 3.x installé.
- Les bibliothèques suivantes :
  ```bash
  pip install Pillow pygame
  ```

### 📂 Fichiers nécessaires

Pour que l'application fonctionne parfaitement, placez ces fichiers dans le même dossier que le script :

- **summer.webp** : Votre image de fond (plage).
- **scarface.wav** : Le fichier audio (ambiance Scarface).

### 🚀 Lancement

Ouvrez un terminal dans le dossier du projet et lancez :

```bash
python sechoire.py
```

🏋️‍♂️🔥

---
# Sechoire
