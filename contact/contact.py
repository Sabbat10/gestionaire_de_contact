from data.data import contacts



def display_contact():
    
    for contact in contacts:
        print(f"👤 Nom     : {contact['name']}")
        print(f"📞 Numéro  : 0{contact['number']}")
        print(f"📧 Email   : {contact['email']}")
        print("")  
