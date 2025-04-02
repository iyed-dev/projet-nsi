# 🛒 Application de Gestion de Commandes pour Restaurant

Ce projet est une **application de gestion de commandes** pour un restaurant, développée en **Python** avec `customtkinter` pour l'interface graphique.

## ✨ Fonctionnalités

- 📌 **Affichage du menu** depuis une base de données JSON (`bdd.json`).
- 🛍 **Ajout d'articles au panier** avec gestion des quantités.
- 💳 **Affichage du total de la commande** en temps réel.
- 🔄 **Mise à jour du statut** des commandes ("En cours..." → "Livré").
- 🖨 **Génération d'un ticket de caisse** au format PDF avec `FPDF`.
- 🗑 **Vidage du panier** en un clic.

## 🛠 Technologies utilisées

- **Python** (logique métier)
- **CustomTkinter** (interface utilisateur)
- **FPDF** (génération de tickets PDF)
- **JSON** (base de données des menus)

## 📂 Structure du projet

```
📁 Projet
│── main.py         # Code principal de l'application
│── bdd.json        # Base de données contenant le menu du restaurant
│── fichier.json    # Fichier temporaire pour stocker les commandes
│── ticketdecaisse.pdf  # Ticket de caisse généré
```

## 🚀 Installation et exécution

1. **Installer les dépendances** :
   ```sh
   pip install customtkinter fpdf
   ```
2. **Lancer l'application** :
   ```sh
   python main.py
   ```

## 📌 Auteurs

Projet réalisé dans le cadre du cours de **NSI** par Iyed A.

---

🛠 **Améliorations possibles :**
- Ajout d'une base de données SQLite pour une gestion plus avancée des commandes.
- Interface plus moderne et responsive.
- Ajout d'un historique des commandes.

📩 N'hésitez pas à proposer des améliorations et à contribuer au projet ! 🚀

