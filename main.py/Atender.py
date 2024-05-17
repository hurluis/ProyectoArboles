from Hospital import Hospital
from Paciente import Paciente

class Atender:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        
    def atenderPaciente(self):
        current = self.hospital.removeMin()
        print("\n====================================================")
        print("HA SIDO ATENDIDO CON ÉXITO:")
        print("====================================================\n")
        print(f"\n- El paciente de nombre: {current.nombre}.\n")
        print(f"- Identificado por: {current.numeroPaciente}.\n")
        print(f"- Genero: {current.genero}.\n")
        print(f"- De {current.Edad} año(s).\n")
        print(f"- En el triaje: {current.Triaje}.\n")
        

       