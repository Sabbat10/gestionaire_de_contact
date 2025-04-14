from data.data import contacts

# Fonction pour afficher les contacts
def display_contact():
    
    for contact in contacts:
        print(f"👤 Nom     : {contact['name']}")
        print(f"📞 Numéro  : 0{contact['number']}")
        print(f"📧 Email   : {contact['email']}")
        print("")  


# Fonction pour rechercher un contact
def search_contact():
    
    nom = input("Entrez le nom du contact : ").strip().lower()
    print("")
    found = False
    
    for contact in contacts:
        if (nom in contact['name'].lower()):
            print(f"👤 Nom     : {contact['name']}")
            print(f"📞 Numéro  : 0{contact['number']}")
            print(f"📧 Email   : {contact['email']}")
            found = True
            break
        
    if not found:
        print("⚠️ Ce contact n'existe pas !.")