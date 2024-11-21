class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = None
        self.__edad = None
        self.__dni = None
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)


    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre.strip()
        else:
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")

    def set_edad(self, edad):
        if isinstance(edad, int) and 0 <= edad <= 150:
            self.__edad = edad
        else:
            raise ValueError("No es mayor de edad")

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni.strip()) > 0:  
            self.__dni = dni.strip()
        else:
            raise ValueError("El DNI debe ser una cadena de texto no vacía.")

    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18


try:
    persona = Persona("Oscar Reyes", 16, "12345678X")
    persona.mostrar()  
    print("¿Es mayor de edad?", persona.es_mayor_de_edad()) 

    persona.set_edad(-5) 
except ValueError as e:
    print(f"Error: {e}")
