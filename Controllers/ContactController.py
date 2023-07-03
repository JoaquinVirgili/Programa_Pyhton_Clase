from Model.DTO.ContactForView import ContactForView
from Model.Repository.ContactRepository import ContactRepository


class ContactController:
    def get_contacts_by_user(self, username):
        contact_repository = ContactRepository()
        contacts = contact_repository.get_contacts_by_user(username)
        contactsForView = []
        for contact in contacts:
            contactForView = ContactForView(contact)
            contactsForView.append(contactForView)
        return contactsForView
    
    def get_contacts_birthday(self, contact):
        contact_repsitory = ContactRepository()
        contacts, salir = contact_repsitory.get_contacts_birthday(contact)
        contactsBforView = []
        if salir == False:
            salirFinal = False
        else:
            for contact in contacts:
                contactBForView = ContactForView(contact)
                contactsBforView.append(contactBForView)
            salirFinal = True
        return contactsBforView, salirFinal         
    
    def get_contact(self, contact):
        contact_repository = ContactRepository()
        contact = contact_repository.get_contact(contact)
        contactForView = ContactForView(contact)
        return contactForView
    
    def add_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.add_contact(contact)

    def update_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.update_contact(contact)

    def delete_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.delete_contact(contact)
    