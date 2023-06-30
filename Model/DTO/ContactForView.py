class ContactForView:
    id= 0
    name = ""
    surname = ""
    fechaNacimiento = ""
    email = ""
    username = ""

    def __init__(self, contact) -> None:
        self.name = contact.name
        self.surname = contact.surname
        self.fechaNacimiento = contact.fechaNacimiento
        self.email = contact.email
        self.username = contact.username
        self.id = contact.id

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Apellido: {self.surname} - Fecha Nacimiento: {self.fechaNacimiento} - Email: {self.email} - Id: {self.id}"

    
