from Paciente import Paciente
from Hospital import Hospital
from Registrar import Registrar
from Mostrar import Mostrar
from Atender import Atender
from Eliminar import Eliminar
from NivelPaciente import NivelPaciente

class Menu:

    def __init__(self):
        self.hospital = Hospital()
        paciente1 = Paciente(1, 'M', 'Pedro', 67, 4)       
        paciente2 = Paciente(2, 'F', 'Teresa', 45, 2)
        paciente3 = Paciente(3, 'M', 'Julio', 75, 1)
        paciente4 = Paciente(4, 'F', 'Sofia', 15, 4)
        paciente5 = Paciente(5, 'M', 'Juan', 12, 3)
        paciente6 = Paciente(6, 'F', 'Sofia', 35, 1)
        paciente7 = Paciente(7, 'M', 'Jonh', 40, 5)

        self.hospital.insert(paciente1)
        self.hospital.insert(paciente2)
        self.hospital.insert(paciente3)
        self.hospital.insert(paciente4)
        self.hospital.insert(paciente5)
        self.hospital.insert(paciente6)
        self.hospital.insert(paciente7)
        self.mostrarMenu()
    # def __init__(self):
    #     self.hospital = Hospital()
        
    #     self.mostrarMenu()
        

    def mostrarMenu(self):
        print("\n====================================================")
        print("BIENVENIDO AL HOSPITAL")
        print("====================================================\n")
        if self.hospital.length == 0:
            self.mostrarOpcionesHospitalVacio()
        elif self.hospital.length > 0:
            self.mostrarOpcionesHospitalConPacientes()
        self.mostrarMenu()

    def mostrarOpcionesHospitalVacio(self):    
            
        print("1. Agregar un paciente al hospital.")
        seleccionarOpcion: int = int(input("\nIngresa tu opción: "))
        if seleccionarOpcion == 1:
            self.opcionSeleccionada1()
        
        else:    
            print("\nIngresa una opción válida.\n")
            self.mostrarOpcionesHospitalVacio()
    
    def mostrarOpcionesHospitalConPacientes(self):
           
            print("1. Agregar un nuevo paciente.")
            print("2. Consultar paciente que sigue por atender.")
            print("3. Atender paciente.")
            print("4. Consultar los pacientes que estan en el hospital.")
            print("5. Consultar paciente por Triaje.")
            print("6. Retirar paciente por nombre y/o Id.")
            print("7. Buscar nivel del paciente en el árbol.")
            seleccionarOpcion: int = int(input("\nIngresa tu opción: "))

            if seleccionarOpcion == 1:
                self.opcionSeleccionada1()
            elif seleccionarOpcion == 2:
                self.opcionSeleccionada2()
            elif seleccionarOpcion == 3:
                self.opcionSeleccionada3()
            elif seleccionarOpcion == 4:
                self.opcionSeleccionada4()
            elif seleccionarOpcion == 5:
                self.opcionSeleccionada5()
            elif seleccionarOpcion == 6:
                self.opcionSeleccionada6()
            elif seleccionarOpcion ==7:
                self.opcionSeleccionada7()
            else:
                print("\nIngresa una opción válida\n")
                self.mostrarOpcionesHospitalConPacientes()
    #No valida cuando hay un repetido y aun asi lo agrega(el repetido se comprueba por el numero unico)
    def opcionSeleccionada1(self):
        print("\n================= Agregar un paciente al hospital =================")
        AgregarPaciente = Registrar(self.hospital)
        AgregarPaciente.agregarPaciente()


    def opcionSeleccionada2(self):
        print("\n================= Siguiente paciente en espera =================")

        MostrarPaciente = Mostrar(self.hospital)
        MostrarPaciente.mostrarPaciente()
    

    def opcionSeleccionada3(self):
        print("\n================= Vamos a atender a un paciente =================")

        AtenderPaciente = Atender(self.hospital)
        AtenderPaciente.atenderPaciente()


#DE ACA PARA ABAJO SON LOS QUE FALTAN

    #se escribe en mostrar
    def opcionSeleccionada4(self):
        print("\n================= Consultemos los pacientes del hospital =================")
        Mostrarhospital = Mostrar(self.hospital)
        Mostrarhospital.mostrarHospital()
    #se escribe en mostrar
    
    def opcionSeleccionada5(self):
        print("\n================= Consultemos los pacientes por triaje =================")
        Triaje = int(input("Ingrese el Triaje a consultar"))      
        Mostrarportriaje = Mostrar(self.hospital)
        Mostrarportriaje.mostrarTriaje(Triaje)

    #Este se escribe en el modulo Eliminar
    def opcionSeleccionada6(self):
        print("\n================= Retiremos un paciente del hospital =================")
        numeroPaciente: int = int(input("Ingresa el identificador único del paciente: "))

        EliminaPaciente = Eliminar(self.hospital)
        EliminaPaciente.eliminar_paciente(numeroPaciente)

    def opcionSeleccionada7(self):
        print("\n================= Buscar nivel del paciente en el árbol =================")
        numeroPaciente = input("Ingresa el identificador único del paciente: ")
        buscador = NivelPaciente(self.hospital)
        nivel = buscador.buscarNivel(numeroPaciente)
        if nivel >= 0:
            print(f"El paciente con identificador {numeroPaciente} se encuentra en el nivel {nivel} del árbol.")
        else:
            print(f"No se encontró el paciente con identificador {numeroPaciente} en el árbol.")
        
        

menu = Menu()
menu