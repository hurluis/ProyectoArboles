from Hospital import Hospital
from Paciente import Paciente

class Eliminar:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital

    def eliminar_paciente(self, id):
        # Asume que id es el número de paciente
        if self.hospital.deleteNode(Paciente(id, "", "", 0, 0)):
            return print("Paciente ha sido retirado de la lista de espera con éxito")
        else:
            print("No se encontro el paciente a retirar")

"""paciente1 = Paciente(1, 'M', 'Pedro', 67, 4)       
paciente2 = Paciente(2, 'F', 'Teresa', 45, 2)
paciente3 = Paciente(3, 'M', 'Julio', 75, 1)
paciente4 = Paciente(4, 'F', 'Sofia', 15, 4)

sistema = Hospital()
sistema.insert(paciente1)
sistema.insert(paciente2)
sistema.insert(paciente3)
sistema.insert(paciente4)


sistema.printTree()

Mostrartriaje = Eliminar(sistema)
Mostrartriaje.eliminar_paciente(4)
sistema.printTree()"""
