class Contact:
    id = 0
    name = ""
    surname = ""
    fechaNacimiento = ""
    email = ""
    username = ""
    state = True

    def __repr__(self) -> str:
        return f"Contact(id={self.id}, name={self.name}, surname={self.surname}, fechaNaciento = {self.fechaNacimiento}email={self.email}, username={self.username}, state={self.state})"
