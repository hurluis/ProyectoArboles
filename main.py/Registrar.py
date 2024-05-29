from Hospital import Hospital
from Paciente import Paciente

class Registrar:
    def __init__(self, hospital:Hospital):
        self.hospital=hospital


    def agregarPaciente(self):
        numeroPaciente: int = input("Ingresa el identificador único del paciente: ")
        genero: str = input("Ingresa el género del paciente: ")
        nombre: str = input("Ingresa el nombre del paciente: ")
        edad: int = int(input("Ingresa la edad del paciente: "))
        triaje: int = int(input("Ingresa el triaje de prioridad del paciente: "))

        paciente = Paciente(numeroPaciente, genero, nombre, edad, triaje)
        

        self.hospital.insert(paciente)
        print("paciente añadido\n")
        
        
        
# paciente1 = Paciente(1, 'M', 'Pedro', 67, 4)       
# paciente2 = Paciente(2, 'F', 'Teresa', 45, 2)
# paciente3 = Paciente(3, 'M', 'Julio', 75, 1)
# paciente4 = Paciente(4, 'F', 'Sofia', 15, 4)

# sistema = Hospital()
# sistema.insert(paciente1)
# sistema.insert(paciente2)
# sistema.insert(paciente3)
# sistema.insert(paciente4)

# sistema.printTree()

