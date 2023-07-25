import mysql.connector

class Context:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="newrootpass",
        database="contacts"
        )
        self.mycursor = self.mydb.cursor()
        #print(" Info Base Datos: Conexion abierta ".center(40, "*"))

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.mycursor.close()
        self.mydb.close()
        #print(" Info Base Datos: Conexion cerrada ".center(40, "*"))


if __name__ == "__main__":
    with Context() as context:
        print(context)