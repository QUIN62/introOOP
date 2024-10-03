class Persona:
    # Constructor para inicializar atributos
    def __init__(self, nombre, edad, genero, profesion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.profesion = profesion
        self.estado_animo = "Neutral"

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        print(f"Profesión: {self.profesion}")

    # Método para hacer que la persona hable
    def hablar(self, mensaje):
        print(f"{self.nombre} dice: '{mensaje}'")

    # Método para cambiar el estado de ánimo de la persona
    def cambiar_estado_animo(self, nuevo_estado):
        self.estado_animo = nuevo_estado
        print(f"{self.nombre} ahora está {self.estado_animo}")

    # Método para celebrar el cumpleaños y aumentar la edad
    def celebrar_cumpleaños(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

    # Método para cambiar la profesión
    def cambiar_profesion(self, nueva_profesion):
        self.profesion = nueva_profesion
        print(f"{self.nombre} ahora trabaja como {self.profesion}")

    # metodo pasar saludo
    def pasar_saludo(self, nombreotrapersona):
return f"Hola, {self.nombre}, te manda saludar {nombreotrapersona}
print(persona1.saludarA(persona2.nombre)


# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 30, "Masculino", "Ingeniero")
persona2 = Persona("Juan", 19, "Masculino", "Estudiante")
persona3 = Persona("Victor", 24, "Masculino", "Docente")
# Utilizar los métodos de la clase
persona1.mostrar_info()  # Mostrar información de la persona
persona1.hablar("¡Hola a todos!")  # Hacer que la persona hable
persona1.cambiar_estado_animo("Feliz")  # Cambiar el estado de ánimo
persona1.celebrar_cumpleaños()  # Celebrar el cumpleaños
persona1.cambiar_profesion("Programador")  # Cambiar la profesión
