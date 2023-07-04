from Model.DTO.ContactForView import ContactForView
from Model.Repository.ContactRepository import ContactRepository


class ContactController:
    def get_contacts_by_user(self, username):
        contact_repository = ContactRepository() #Se instancia a la clase ContactRepository
        contacts = contact_repository.get_contacts_by_user(username) #Se llama a la funcion y se le pasa el username del loggued
        contactsForView = [] #Se crea una lista vacia
        for contact in contacts: #Se recorre la lista obtenida de la funcion 
            contactForView = ContactForView(contact) #Cada que vez que se recorre el bucle se le pasa al contactForView el contacto que trae del bucle para convertirlo en objeto
            contactsForView.append(contactForView) #Se agrega el contacto ya convertido a la nueva lista vacia
        return contactsForView
    
    def get_contacts_birthday(self, contact):
        contact_repsitory = ContactRepository()
        contacts, salir = contact_repsitory.get_contacts_birthday(contact) #Parecido a la funcion anterior pera esta solo nos trae los contactos que cumplan años el mes actual
        contactsBforView = []
        #Se usa una bandera por si la lista esta vacia, para poder mostrar un mensaje despues
        if salir == False:
            salirFinal = False
        else:
            for contact in contacts:
                contactBForView = ContactForView(contact)
                contactsBforView.append(contactBForView)
            salirFinal = True
        return contactsBforView, salirFinal #Se devuelven los dos valores, la lista vacia/llena y el valor de la bandera   
    
    def get_contact(self, contact): #Nos trae solo un contacto especifico.
        contact_repository = ContactRepository()
        contact = contact_repository.get_contact(contact)
        contactForView = ContactForView(contact)
        return contactForView
    
    def add_contact(self, contact): #Nos permite agregar un contacto
        contact_repository = ContactRepository()
        contact_repository.add_contact(contact)

    def update_contact(self, contact): #Nos permite modificar un usuario 
        contact_repository = ContactRepository()
        contact_repository.update_contact(contact)

    def delete_contact(self, contact): #Nos permite "eliminar" un contacto
        contact_repository = ContactRepository()
        contact_repository.delete_contact(contact)
    