from Hospital import Hospital
from Paciente import Paciente

class Registrar:
    def __init__(self, hospital:Hospital):
        self.hospital=hospital


    def agregarPaciente(self):
        numeroPaciente: str = input("Ingresa el identificador único del paciente: ")
        genero: str = input("Ingresa el género del paciente: ")
        nombre: str = input("Ingresa el nombre del paciente: ")
        edad: int = int(input("Ingresa la edad del paciente: "))
        triaje: int = int(input("Ingresa el triaje de prioridad del paciente: "))

        if self.hospital
        
    