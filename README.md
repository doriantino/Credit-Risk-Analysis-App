# 🚀 Credit Risk Analysis Web Application : De l'Opérationnel à la Stratégie Décisionnelle

## ✨ Aperçu du Projet

Bienvenue sur le dépôt de mon application d'analyse du risque de crédit ! Ce projet est une démonstration concrète de ma capacité à **transformer des données brutes en insights actionnables** et à **déployer des solutions concrètes** qui génèrent de la valeur.

En tant que **Data & Business Analyst** aguerri en **Salesforce Operations** et **Data Analysis** (R, Alteryx, Excel, Power BI, Python), j'ai développé cette application web pour simuler un cas d'usage critique dans le secteur financier : l'évaluation rapide et fiable du risque de crédit. Ce projet illustre ma transition et mon appétence pour des rôles **Advisory et de conseil**, où l'analyse approfondie et la résolution de problématiques complexes sont au cœur des missions.

L'application permet d'évaluer la solvabilité d'un demandeur de prêt en utilisant un modèle d'apprentissage automatique pré-entraîné. Elle offre une interface simple et intuitive pour simuler des scénarios et obtenir des verdicts instantanés ("Prêt Approuvé" ou "Prêt Refusé"), imitant ainsi le processus décisionnel rapide requis dans un environnement commercial dynamique.

## 🎯 Problème Addréssé & Solution Proposée

**Le Challenge :** Dans le secteur financier, la prise de décision rapide concernant l'octroi de crédit est essentielle. Une évaluation manuelle ou inefficace du risque peut entraîner des pertes significatives dues aux défauts de paiement ou, à l'inverse, une perte d'opportunités en refusant des clients à faible risque.

**Ma Solution :** Cette application propose une approche **data-driven** pour automatiser et optimiser ce processus. En encapsulant un modèle de Machine Learning dans une interface web conviviale basée sur Flask, je démontre ma capacité à :
* **Structurer des problématiques complexes :** Définir les variables clés influençant le risque de crédit.
* **Appliquer des compétences techniques avancées :** Utiliser Python, NumPy, Scikit-learn pour le développement du modèle et Flask pour la mise en production.
* **Délivrer des solutions concrètes et utilisables :** Créer une interface utilisateur accessible qui transforme l'analyse ML en un outil décisionnel tangible.
* **Comprendre l'impact business :** Contribuer à la réduction des risques financiers et à l'optimisation des portefeuilles de prêts.

## 🌟 Points Forts Techniques

* **Backend Robuste (Python/Flask) :** Mise en place d'une API RESTful (`/predict`) pour gérer les requêtes de prédiction, garantissant évolutivité et intégration facile.
* **Modélisation Prédictive :** Utilisation de Scikit-learn pour le développement et l'intégration d'un modèle de classification fiable.
* **Pipeline de Données :** Intégration transparente des étapes de pré-traitement (ex: transformation logarithmique) directement dans le processus de prédiction, assurant la cohérence avec le modèle entraîné.
* **Gestion de l'Environnement :** Utilisation de `requirements.txt` et d'environnements virtuels pour une reproductibilité et une portabilité parfaites.
* **Versionnement (Git/GitHub) :** Gestion professionnelle du code source, démontrant des pratiques de développement collaboratives et structurées.

## 🛠️ Stack Technologique

* **Langage :** Python 3.x
* **Web Framework :** Flask
* **Librairies ML & Data :** NumPy, Pandas (implicite pour la préparation du `model.pkl`), Scikit-learn, Pickle
* **Frontend :** HTML, CSS
* **Gestion des Dépendances :** `pip`
* **Contrôle de Version :** Git, GitHub

## 📂 Structure du Projet

Credit_App/
├── .gitignore               # Fichiers et dossiers à ignorer par Git (IDE, environnements virtuels)
├── app.py                   # Point d'entrée principal de l'application Flask
├── model.pkl                # Modèle de Machine Learning pré-entraîné
├── templates/               # Fichiers HTML pour l'interface utilisateur web
│   └── index.html           # La page principale avec le formulaire de saisie
├── static/                  # Fichiers statiques (CSS, JavaScript, images - à développer si besoin)
├── requirements.txt         # Liste exhaustive des dépendances Python
└── README.md                # Ce fichier de présentation

## 🚀 Démarrage Rapide

Suivez ces étapes pour lancer l'application en local et explorer ses fonctionnalités :

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/doriantino/Credit-Risk-Analysis-App.git](https://github.com/doriantino/Credit-Risk-Analysis-App.git)
    cd Credit-Risk-Analysis-App/Credit_App
    ```

2.  **Créer et activer l'environnement virtuel :**
    ```bash
    python -m venv .venv
    # Pour Windows
    .venv\Scripts\activate
    # Pour macOS/Linux
    source .venv/bin/activate
    ```

3.  **Installer les dépendances :**
    Assurez-vous d'avoir généré votre `requirements.txt` (via `pip freeze > requirements.txt` si ce n'est pas déjà fait après installation des dépendances).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Lancer l'application Flask :**
    ```bash
    python app.py
    ```
    L'application sera accessible dans votre navigateur à l'adresse indiquée dans le terminal (généralement `http://127.0.0.1:5000/`).

## 💡 Le Modèle `model.pkl` : Un Aperçu

Le cœur de cette application repose sur `model.pkl`, un modèle d'apprentissage automatique qui a été rigoureusement entraîné. Ce modèle a été construit en suivant les étapes clés d'un pipeline Data Science :

1.  **Collecte & Nettoyage des Données :** Préparation des données historiques de crédit.
2.  **Ingénierie des Caractéristiques :** Application de transformations essentielles (comme `np.log1p` pour la normalisation de certaines variables) pour optimiser la performance du modèle.
3.  **Entraînement du Modèle :** Utilisation d'un algorithme de classification (par exemple, Régression Logistique, Random Forest, ou Gradient Boosting) pour apprendre des patterns dans les données.
4.  **Sérialisation :** Sauvegarde du modèle entraîné avec `pickle` pour une intégration facile dans l'application web.

## 🤝 Contribution & Contact

Je suis toujours ouvert(e) aux discussions sur des projets data-driven, des opportunités dans l'Advisory ou des collaborations. N'hésitez pas à me contacter via :

* **Nom :** Dorian DIKOUME
* **GitHub :** [doriantino](https://github.com/doriantino)
* **Email :** dikoume383@gmail.com
* **LinkedIn :** www.linkedin.com/in/dorian-dikoume-05a1ab186

Les contributions à ce dépôt sont également les bienvenues ! N'hésitez pas à ouvrir des "issues" pour des suggestions ou des "pull requests" pour des améliorations.