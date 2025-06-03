# 📈 Guide des Étapes du Projet : Analyse du Risque de Crédit

Ce document retrace les étapes clés ayant mené à la création et au déploiement de l'application web d'analyse du risque de crédit, depuis l'acquisition des données brutes jusqu'à la mise en ligne sur GitHub.

## 1. Acquisition et Compréhension des Données (Data Acquisition & Understanding)

* **Source des Données :** Spécifiez d'où proviennent vos données (ex: Kaggle, jeu de données public "Loan Prediction Dataset", données internes simulées, etc.).
* **Volume des Données :** Nombre d'enregistrements, nombre de colonnes.
* **Type de Données :** Description des principales variables (numériques, catégorielles, binaires, etc.).
* **Objectif de la Prédiction :** Définition claire de la variable cible (ex: `Loan_Status` - approuvé/refusé).

## 2. Exploration et Nettoyage des Données (EDA & Data Cleaning)

* **Analyse Exploratoire des Données (EDA) :**
    * Identification des distributions des variables (histogrammes, boîtes à moustaches).
    * Analyse des corrélations entre les variables.
    * Visualisation des relations entre les caractéristiques et la variable cible.
* **Gestion des Valeurs Manquantes :**
    * Stratégie appliquée (ex: Imputation par la médiane pour les variables numériques, imputation par le mode pour les catégorielles, suppression des lignes si le nombre de valeurs manquantes est trop important).
* **Gestion des Valeurs Aberrantes (Outliers) :**
    * Détection et traitement des outliers (ex: winsorisation, suppression, transformation).
* **Gestion des Doublons :** Vérification et suppression des enregistrements dupliqués.

## 3. Ingénierie des Caractéristiques (Feature Engineering)

* **Création de Nouvelles Caractéristiques :**
    * Ex: `TotalIncome` (somme de `ApplicantIncome` et `CoapplicantIncome`).
    * Ex: `LoanAmount_per_Income` (ratio pour capter la charge du prêt par rapport aux revenus).
* **Transformation des Variables :**
    * **Transformation Logarithmique :** Application de `np.log1p` sur des variables comme `ApplicantIncome` et `LoanAmount` pour réduire l'asymétrie et stabiliser la variance, rendant les distributions plus proches de la normalité et améliorant la performance du modèle.
    * **Normalisation/Standardisation :** (Si applicable) Mise à l'échelle des variables numériques.
* **Encodage des Variables Catégorielles :**
    * **One-Hot Encoding :** Application de l'encodage One-Hot pour les variables catégorielles nominales (ex: `Property_Area`, `Education`, `Gender`, `Married`, `Dependents`, `Self_Employed`).
    * (Si applicable) **Label Encoding :** Pour les variables ordinales.

## 4. Modélisation Prédictive (Predictive Modeling)

* **Sélection du Modèle :**
    * Choix de l'algorithme de classification (ex: Régression Logistique, Random Forest Classifier, Gradient Boosting Classifier, etc. - *Précisez celui que vous avez utilisé*).
    * Justification du choix (ex: bonne interprétabilité, performance reconnue sur ce type de données, etc.).
* **Découpage des Données :**
    * Division du jeu de données en ensembles d'entraînement et de test (ex: 80% entraînement, 20% test) pour évaluer la généralisation du modèle.
* **Entraînement du Modèle :**
    * Entraînement de l'algorithme sélectionné sur le jeu de données d'entraînement.
* **Évaluation du Modèle :**
    * **Métriques utilisées :** Précision (Accuracy), Rappel (Recall), Précision (Precision), Score F1, Courbe ROC AUC.
    * Interprétation des résultats et discussion des compromis (ex: entre True Positives et False Positives dans le contexte du risque de crédit).
* **Sauvegarde du Modèle :**
    * Sérialisation du modèle entraîné à l'aide de `pickle` dans le fichier `model.pkl` pour une utilisation ultérieure dans l'application web.

## 5. Développement de l'Application Web (Web Application Development)

* **Framework :** Utilisation de Flask pour construire l'application web.
* **Interface Utilisateur (Frontend) :**
    * Développement de `templates/index.html` pour un formulaire de saisie des données client intuitif.
    * Utilisation de CSS pour le style (et potentiellement JavaScript pour l'interactivité si nécessaire).
* **Backend (Python/Flask) :**
    * `app.py` : Le script principal de l'application.
    * **Chargement du Modèle :** Chargement du `model.pkl` au démarrage de l'application.
    * **Endpoint de Prédiction :** Création d'une route `/predict` (méthode POST) pour recevoir les données du formulaire.
    * **Pré-traitement en Temps Réel :** Implémentation des mêmes étapes de transformation (`np.log1p`) et de mise en forme des données sur les entrées utilisateur pour s'assurer qu'elles correspondent au format attendu par le modèle entraîné.
    * **Logique de Décision :** Traduction de la sortie numérique du modèle (0 ou 1) en texte clair ("Prêt Refusé" ou "Prêt Approuvé").
    * **Réponse JSON :** Retourne la prédiction sous forme de JSON pour une flexibilité future.
* **Gestion des Dépendances :** Création du fichier `requirements.txt` listant toutes les bibliothèques Python nécessaires au projet.

## 6. Versionnement et Déploiement sur GitHub (Version Control & Deployment)

* **Initialisation du Dépôt Git :** Transformation du dossier de projet en dépôt Git local (`git init`).
* **Configuration du `.gitignore` :** Création du fichier `.gitignore` pour exclure les fichiers non essentiels (environnements virtuels, caches Python, fichiers d'IDE) du suivi de version.
* **Historique des Commits :** Enregistrement régulier des modifications via des commits avec des messages clairs.
* **Création du Dépôt GitHub :** Mise en place d'un dépôt distant sur [github.com/doriantino/Credit-Risk-Analysis-App](https://github.com/doriantino/Credit-Risk-Analysis-App).
* **Liaison et Push :** Connexion du dépôt local au dépôt distant et envoi du code sur GitHub (`git push`).
* **Documentation du Projet :** Rédaction d'un `README.md` détaillé et axé sur les compétences pour présenter le projet aux recruteurs et faciliter sa prise en main.

---

**Comment intégrer ce document :**

1.  **Créez un nouveau fichier** dans le répertoire `Credit_App` (au même niveau que `app.py`, `model.pkl`, `README.md`).
2.  **Nommez-le `PROJECT_STEPS.md`**.
3.  **Copiez-collez** le contenu ci-dessus dans ce fichier.
4.  **Personnalisez les sections :**
    * **Source des Données :** Mentionnez la source exacte.
    * **Algorithme de Modèle :** Précisez quel algorithme de classification vous avez réellement utilisé (ex: Régression Logistique).
    * **(Optionnel)** Si vous avez des notebooks Jupyter ou des scripts de préparation des données, mentionnez-les ici et idéalement, ajoutez-les à votre dépôt (ex: dans un dossier `notebooks/` ou `data_prep_scripts/`).

5.  **Commitez et Poussez sur GitHub :**
    ```bash
    git add PROJECT_STEPS.md
    git commit -m "Add PROJECT_STEPS.md detailing the project lifecycle"
    git push origin main
    ```