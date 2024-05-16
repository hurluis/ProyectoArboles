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

        if self.hospital.value is None:
            paciente = Paciente(numeroPaciente, genero, nombre, edad, triaje)
            self.hospital.insert(paciente)
            print(self.hospital.insert(paciente))
        elif self.hospital.value is not None:
            iteraciones = 0
            for elementoHospital in self.biblioteca:
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
                    print(self.hospital.insert(paciente))
                    break
        
    