class ContactForUpdate:
    id = 0
    name = ""
    surname = ""
    fechaNacimiento = ""
    email = ""
    username = ""
    state = 1

    def __init__(self, id, name, surname, fechaNacimiento, email, username) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.fechaNacimiento = fechaNacimiento
        self.email = email
        self.username = username
        self.state = 1
