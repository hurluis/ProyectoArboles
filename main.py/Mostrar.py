from Hospital import Hospital
from Paciente import Paciente

class Mostrar:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        
    def mostrarPaciente(self):
        current = self.hospital.removeMin()
        print(f"\n- El paciente que continua es: {current.nombre}.\n")
        print(f"- Su identificador único es: {current.numeroPaciente}.\n")
        print(f"- De genero: {current.genero}.\n")
        print(f"- De {current.Edad} año(s).\n")
        print(f"- Esta en el triaje {current.Triaje}.\n")
        
        self.hospital.insert(current)
       
            



