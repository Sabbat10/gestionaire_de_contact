# 📱 Gestionnaire de Contacts - Terminal

Une petite application Python pour gérer vos contacts directement dans le terminal.  
Vous pouvez afficher vos contacts, en rechercher un, ou en ajouter facilement via un menu interactif.

---

## 🛠️ Fonctionnalités

- 📋 **Afficher les contacts**
- 🔍 **Rechercher un contact par nom (recherche partielle et insensible à la casse)**
- ➕ **Ajouter un nouveau contact avec validation du numéro et de l’email**
- ❌ **Quitter le programme proprement**

---

## 🔧 Installation

1.  **Clonez le projet** :

    ```bash
    git clone https://github.com/Sabbat10/gestionaire_de_contact.git
    cd gestionnaire-contacts
    ```

2.  Créez un environnement virtuel (recommandé) :

    ```bash
    python3 -m venv env

    source env/bin/activate # Linux/macOS
    env\Scripts\activate # Windows
    ```

3.  Structure du projet :

            ```bash
                .

            ├── main.py
            └── contact/
            ├── contact.py # Fonctions : display_contact, search_contact, add_contact
            └── **init**.py
            ```

▶️ Lancer le programme

```bash
python main.py
```

📂 Exemple d’interface

```bash
    ===========================

    📇 Mes Contacts !
    1️⃣ 📋 Afficher mes contacts
    2️⃣ 🔍 Rechercher un contact
    3️⃣ ➕ Ajouter un contact
    4️⃣ ❌ Quitter
```

👤 Auteur :

```bash
Sabbat Lumpantshia
```
