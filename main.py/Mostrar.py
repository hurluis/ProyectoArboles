from Hospital import Hospital
from Paciente import Paciente

class Mostrar:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        
    def mostrarPaciente(self):
        current = self.hospital.removeMin()
        print(f"\nEl paciente que continua es: {current.nombre}.\n")
        self.hospital.insert(current)
       
            



