from ..Entities.Contact import Contact
from ..Context import Context
from datetime import datetime

class ContactRepository:

    def get_contacts_by_user(self, username):
        with Context() as context1:
            query = "SELECT *, DATE_FORMAT(fechaNacimiento, '%d-%m-%Y') AS fechaNacimiento_invertida FROM contact WHERE state = 1 AND username = %s"
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
            contact.fechaNacimiento = contactDB[7]
            contacts.append(contact)
        return contacts
    
    def get_contacts_birthday(self, username):
        fecha_actual = datetime.now().month        
        with Context() as context1:
            query = "SELECT *, DATE_FORMAT(fechaNacimiento, '%d-%m-%Y') AS fechaNacimiento_invertida FROM contact WHERE state = 1 AND username = %s AND MONTH(fechaNacimiento) = %s"
            values = (username, fecha_actual)
            context1.mycursor.execute(query,values)
            contactsDB = context1.mycursor.fetchall()
        contacts = []
        for contactDB in contactsDB:
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.fechaNacimiento = contactDB[7]
            contacts.append(contact)
        return contacts
    


    def get_contact(self, contact):
        with Context() as context1:
            query = "SELECT *, DATE_FORMAT(fechaNacimiento, '%d-%m-%Y') AS fechaNacimiento_invertida FROM contact WHERE idcontact = %s"
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
            contact.fechaNacimiento = contactDB[7]
        return contact
    
    def add_contact(self, contact):
        with Context() as context1:
            query = "INSERT INTO contact (name, surname, email, username, state, fechaNacimiento) VALUES (%s, %s, %s, %s, %s, STR_TO_DATE(%s, '%d-%m-%Y'))"
            values = (contact.name, contact.surname, contact.email, contact.username, contact.state, contact.fechaNacimiento)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
            contact.id = context1.mycursor.lastrowid
        return contact

    def update_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET name = %s, surname = %s, fechaNacimiento = STR_TO_DATE(%s, '%d-%m-%Y'), email = %s WHERE idcontact = %s AND username = %s"
            values = (contact.name, contact.surname, contact.fechaNacimiento, contact.email, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()

    def delete_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET state = %s WHERE idcontact = %s AND username = %s"
            values = (0, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
        
