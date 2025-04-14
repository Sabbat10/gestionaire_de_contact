from data.data import contacts
import re

# Fonction pour afficher les contacts
def display_contact():
    
    for contact in contacts:
        numero = str(contact['number'])
        if not numero.startswith("0"):
            numero = "0" + numero

        print(f"👤 Nom     : {contact['name']}")
        print(f"📞 Numéro  : {numero}")
        print(f"📧 Email   : {contact['email']}")
        print("═══════════════════════════════")



# Fonction pour rechercher un contact
def search_contact():
    
    nom = input("Entrez le nom du contact : ").strip().lower()
    print("")
    found = False
    
    
    for contact in contacts:
        
        numero = str(contact['number'])
        if not numero.startswith("0"):
            numero = "0" + numero
        
        if (nom in contact['name'].lower()):
            print(f"👤 Nom     : {contact['name']}")
            print(f"📞 Numéro  : {numero}")
            print(f"📧 Email   : {contact['email']}")
            found = True
            break
        
    if not found:
        print("⚠️ Ce contact n'existe pas !.")
        
        
# Fonction pour ajouter un contact

def add_contact():
    print("\n📥 Ajouter un nouveau contact")
    
    # ✅ Nom : suppression des chiffres ou caractères bizarres
    nom = input("👤 Entrez le nom du contact : ").strip()
    if not nom.replace(" ", "").isalpha():
        print("❌ Le nom ne doit contenir que des lettres.")
        return

    # ✅ Numéro : vérifie si c’est bien un numéro congolais valide
    numero = input("📞 Entrez le numéro de téléphone : ").strip()
    if not numero.isdigit() or len(numero) not in [9, 10]:
        print("❌ Le numéro doit contenir 9 ou 10 chiffres.")
        return

    # ✅ Email : validation avec regex
    email = input("📧 Entrez l'email : ").strip().lower()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("❌ Adresse e-mail invalide.")
        return

    # 🔍 Vérification doublon
    for contact in contacts:
        if nom.lower() == contact['name'].lower():
            print("⚠️ Ce contact existe déjà !")
            return
    
    # ✅ Ajout du contact
    contacts.append({
        "name": nom.title(),
        "number": numero,
        "email": email
    })

    print("✅ Contact ajouté avec succès ! 🎉")
