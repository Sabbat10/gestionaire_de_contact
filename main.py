from contact.contact import display_contact, search_contact, add_contact

while True:
    
    print("===========================")
    print("📇 Mes Contacts !")
    print("")
    print("1️⃣  📋 Afficher mes contacts")
    print("2️⃣  🔍 Rechercher un contact")
    print("3️⃣  ➕ Ajouter un contact")
    print("4️⃣  ❌ Quitter")
    print("")
    
    try:
        choix = int(input("Choisissez une option (1-4) : "))
        
        if choix not in [1, 2, 3, 4]:
            print("❌ Choix invalide. Veuillez choisir une option valide.")
        else:
            print("")
            
            if choix == 1:
                print("📋 Mes contacts :")
                display_contact()
                print("")
            
            elif choix == 2:
                print("🔍 Rechercher un contact :")
                search_contact()
                print("")
                
            elif choix == 3:
                print("➕ Ajouter un contact :")
                add_contact()
                print("")
                
            elif choix == 4:
                print("👋 Au revoir !")
                break

    except ValueError:
        print("❌ Entrée invalide. Veuillez entrer un chiffre.")
