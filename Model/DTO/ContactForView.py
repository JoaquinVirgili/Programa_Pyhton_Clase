class ContactForView:
    id= 0
    name = ""
    surname = ""
    email = ""
    username = ""
    birthday = None

    def __init__(self, contact) -> None:
        self.name = contact.name
        self.surname = contact.surname
        self.birthday = contact.birthday
        self.email = contact.email
        self.username = contact.username
        self.id = contact.id

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Apellido: {self.surname} - Fecha Nacimiento: {self.birthday} - Email: {self.email} - Id: {self.id}"

    
