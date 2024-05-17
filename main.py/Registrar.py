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

        paciente = Paciente(numeroPaciente, genero, nombre, edad, triaje)
        
        if self.hospital.length==0:
            paciente = Paciente(numeroPaciente, genero, nombre, edad, triaje)
            self.hospital.insert(paciente)
        elif self.hospital.length>0:
            iteraciones = 0
            for elementoHospital in self.hospital:
                iteraciones += 1
                if  elementoHospital.value.numeroPaciente == numeroPaciente:
                    print("\nEl identificador del paciente ya ha sido agregado.")
                    print("\nIngrese un identificador diferente.\n")
                    self.agregarPaciente()
                    break
                elif elementoHospital.value.numeroPaciente != numeroPaciente and self.hospital.length > iteraciones:
                    pass
                elif elementoHospital.value.numeroPaciente != numeroPaciente and self.hospital.length == iteraciones:
                    paciente = Paciente(numeroPaciente, genero, nombre, edad, triaje)
                    self.hospital.insert(paciente)
                    break

        print("\n====================================================")
        print("HOSPITAL:")
        print("====================================================\n")
        print("\nEsta presentado por el nombre del paciente y su respectivo triaje: ")
        print("\n")
        self.hospital.printTree()
        
    