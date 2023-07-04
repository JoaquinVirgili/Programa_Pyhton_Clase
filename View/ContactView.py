from os import system
from Controllers.ContactController import ContactController
from Model.DTO.ContactForDelete import ContactForDelete
from Model.DTO.ContactForUpdate import ContactForUpdate
from Model.DTO.UserForView import UserForView
from Controllers.OrderDate import OrderDate

class ContactView:    
    def __init__(self, user):
        self.user_logged = user
    
    def Menu(self):
        while True:
            system("cls")
            print(" Menu de contactos ".center(50, "#"))
            print("1 - Lista de contactos")
            print("2 - Listar contactos que cumplan este mes")
            print("3 - Agregar contacto")
            print("4 - Editar contacto")
            print("5 - Eliminar contacto")
            print("6 - Cerrar sesion de usuario")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1":
                self.listContacts()
            elif option == "2":
                self.listContacts_Birthday()
            elif option == "3":
                self.addContact()
            elif option == "4":
                self.editContact()
            elif option == "5":
                self.deleteContact()
            elif option == "6":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))

    def listContacts(self):
        system("cls")
        print(" Lista de contactos ".center(50, "#"))
        contactC = ContactController() #Se crea una instancia de la clase ContactController
        contacts = contactC.get_contacts_by_user(self.user_logged.username) #Y se llama a la funcion get_contacts_by_user pasandole como parametro el user logged
        #Recorremos la lista de los contactos e imprimimos uno por uno en consola. 
        for contact in contacts:
            print(contact)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def listContacts_Birthday(self):
        system("cls")
        print(" Contactos que cumplen años este mes ".center(50, "#"))
        contactC = ContactController() #Se crea una instancia de la clase ContactController
        contacts, salir = contactC.get_contacts_birthday(self.user_logged.username) #Se llama a la funcion get_contacts_birthday del Controller
        if salir == False: #Tambien se obtiene el valor de la variable salir, si nos devuelve false nos imprime que no hay contactos que cumplan este mes
            print("No hay contactos que cumplan años este mes.")
        else:
            for contact in contacts: #Recorre la lista de contactos que solo cumplen año el mes de la fecha de la pc.
                print(contact)
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def addContact(self):
        system("cls")
        print(" Alta de contacto ".center(50, "!"))
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        contactFull = ContactController()  #Se crea una instancia de la clase ContactController
        contact = ContactForUpdate(0, name, surname, email, self.user_logged.username) #Se le pasan los valores para crear el objeto contact
        #Nos permite ingresar, si lo deseamos, la fecha de cumpleaños de nuesto contacto.
        yes = input("¿Quiere ingresar la fecha de cumpleaños del contacto? Ingrese SI o NO: ")
        if yes.upper() == "SI":
            close = False
            #En caso de que sea si, hasta que no ingresemos un formato adecuado no nos va a dejar salir.
            while close == False:
                #Se puede ingresar de la forma que queramos, ya sea con coma, guion bajo, guion medio, barra, punto.
                birthday = input("Ingrese la fecha de cumpleañs, por favor que sea en el formato DD-MM-YYYY: ").replace("/" and"." and","and "_" and ":" ,"-")
                # Se le pasa a la funcion order_date, de la clase OrderDate, la fecha para que nos la formatee de la manera que se debe ingresar a la base de datos.
                birthday_order, close = OrderDate.order_date(birthday)
                #Y en caso que sea un valor correcto, ejempo no una letra, la bandera close se convierte en true y cierra el bucle.
            
            contact.birthday = birthday_order #Se le pasa al contacnt el valor de la fecha de cumpleaños
        #Si no se ejecuta la fecha el valor por default es None
        contactFull.add_contact(contact)
        
        input(" Presione enter para continuar ".center(50, "!"))
 

    def editContact(self):
        system("cls")
        print(" Editar contacto ".center(50, "#"))
        print("-"*50)
        id = input("Ingrese el id del contacto a editar: ")
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contact = ContactForUpdate(id, name, surname, email, self.user_logged.username)
        yes = input("¿Quiere agregar la fecha de cumpleaños del contacto? Ingrese SI o NO: ")
        if yes.upper() == "SI":
            close = False
            
            while close == False:
        
                birthday = input("Ingrese la fecha de cumpleaños, por favor que sea en el formato DD-MM-YYYY: ").replace("/" and"." and",","-")
                birthday_order, close = OrderDate.order_date(birthday)

            contact.birthday = birthday_order
        else:
            #En caso de que el user no quiera modificar o agregar la fecha de cumpleaños del contacto se ejecuta esto
            contacC_birthday = contactC.get_contact(contact) #Se le pasa el mismo objeto a la funcion get_contact del Controller
            #Esta funcion nos trae UN SOLO contacto
            contacC_birthday_order = contacC_birthday.birthday #Ahora traemos solo el campo birthday del objeto. 
            if not contacC_birthday_order == None: #Comparamos si no es un campo vacio/None
                contacC_birthday_finally, close =  OrderDate.order_date(contacC_birthday_order) #Aplicamos la funcion para ordenar la fecha
                contact.birthday = contacC_birthday_finally #Se la asignamos al objeto para que mantenga el clumpleaños del contacto
           
            
        contactC.update_contact(contact)
        input(" Presione enter para continuar ".center(50, "!"))

    def deleteContact(self):
        system("cls")
        print(" Eliminar contacto ".center(50, "!"))
        print("-"*50)
        id = input("Ingrese el id del contacto a eliminar: ")
        print("-"*50)
        contactC = ContactController()
        contactC.delete_contact(ContactForDelete(id, self.user_logged.username)) #Se le pasa a la funcion delete_contact el user logged.
        input(" Presione enter para continuar ".center(50, "!"))
