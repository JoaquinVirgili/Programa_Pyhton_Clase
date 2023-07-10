from ..Entities.Contact import Contact
from ..Context import Context
from datetime import datetime

class ContactRepository:

    def get_contacts_by_user(self, username):
        with Context() as context1:            
            query = "SELECT * FROM contact WHERE state = 1 && username = %s "
            values = (username,)
            context1.mycursor.execute(query,values)
            contactsDB = context1.mycursor.fetchall()
        contacts = []
        for contactDB in contactsDB:
            contact = Contact()
           
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]            
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            date_str = contactDB[6] 
            if not date_str == None:
                contact.birthday = date_str.strftime('%d-%m-%Y')
            else:
                contact.birthday = date_str
            contacts.append(contact)
        return contacts
    
    def get_contacts_birthday(self, username):
        fecha_actual = datetime.now().month        
        with Context() as context1:
            query = "SELECT idcontact, name, surname, birthday FROM contact WHERE state = 1 AND username = %s AND MONTH(birthday) = %s"
            values = (username, fecha_actual)
            context1.mycursor.execute(query,values)
            contactsDB = context1.mycursor.fetchall()
        contacts = []
        if len(contactsDB) == 0:
            salir = False
            
        else:
            for contactDB in contactsDB:
                contact = Contact()
                contact.id = contactDB[0]
                contact.name = contactDB[1]
                contact.surname = contactDB[2]
                date_str = contactDB[3] 
                contact.birthday = date_str.strftime('%d-%m-%Y')
                contacts.append(contact)
                salir = True
        return contacts, salir
        
    


    def get_contact(self, contact):
        with Context() as context1:
            query = "SELECT * FROM contact WHERE idcontact = %s"
            values = (contact.id,)
            context1.mycursor.execute(query, values)
            contactDB = context1.mycursor.fetchone()
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            date_str = contactDB[6] 
            if not date_str == None:
                contact.birthday = date_str.strftime('%d-%m-%Y')
            else:
                contact.birthday = date_str
        return contact
    
    def add_contact(self, contact):
        with Context() as context1:
            query = "INSERT INTO contact (name, surname, email, username, state, birthday) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (contact.name, contact.surname, contact.email, contact.username, contact.state, contact.birthday)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
            contact.id = context1.mycursor.lastrowid
        return contact

    def update_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET name = %s, surname = %s, birthday = %s, email = %s WHERE idcontact = %s AND username = %s"
            values = (contact.name, contact.surname, contact.birthday, contact.email, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()

    def delete_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET state = %s WHERE idcontact = %s AND username = %s"
            values = (0, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
        
