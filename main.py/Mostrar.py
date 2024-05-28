from Hospital import Hospital
from Paciente import Paciente
from Registrar import Registrar
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
       

    def mostrarHospital(self):
        print("\n====================================================")
        print("HOSPITAL:")
        print("====================================================\n")
        print("\nEsta presentado por el nombre del paciente y su respectivo triaje: ")
        print("\n")
        self.hospital.printTree()
        


    def mostrarTriaje(self, triaje):
        print(f"Pacientes con triaje {triaje}:")
        print("====================================================\n")
        self.consultar_pacientes_por_triaje_recursivo(self.hospital, triaje)

    def consultar_pacientes_por_triaje_recursivo(self, node, triaje):
        if node is None:
            return

        if node.value is not None and node.value.Triaje == triaje:
            print(node.value)
            print("\n")

        if node.leftchild is not None:
            self.consultar_pacientes_por_triaje_recursivo(node.leftchild, triaje)
        if node.rightchild is not None:
            self.consultar_pacientes_por_triaje_recursivo(node.rightchild, triaje)

        if node.leftchild and node.rightchild is None:
            print("Lo sentimos, NO se ENCONTRO un paciente con dicho triaje")
            print("\n")
            



"""paciente1 = Paciente(1, 'M', 'Pedro', 67, 4)       
paciente2 = Paciente(2, 'F', 'Teresa', 45, 2)
paciente3 = Paciente(3, 'M', 'Julio', 75, 1)
paciente4 = Paciente(4, 'F', 'Sofia', 15, 4)

sistema = Hospital()
sistema.insert(paciente1)
sistema.insert(paciente2)
sistema.insert(paciente3)
sistema.insert(paciente4)
Mostrartriaje = Mostrar(sistema)
Mostrartriaje.mostrarTriaje(4)
"""
