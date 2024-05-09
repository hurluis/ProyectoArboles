from Paciente import Paciente


class Menu:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.librosParaAlquilar = Biblioteca()
        self.librosAlquilados = Biblioteca()
        self.historialLibrosAlquilados = Biblioteca()

        self.mostrarMenu()
        

    def mostrarMenu(self):
        print("\n====================================================")
        print("BIENVENIDO AL MENÚ DE LA BIBLIOTECA")
        print("====================================================\n")
        if self.biblioteca.length == 0:
            self.mostrarOpcionesBibliotecaVacia()
        elif self.biblioteca.length > 0:
            self.mostrarOpcionesBibliotecaIniciada()
        self.mostrarMenu()

    def mostrarOpcionesBibliotecaVacia(self):    
        print("1. Agregar un libro.")
        print("2. Ingresos totales por alquileres de libros hasta el momento.")
        seleccionarOpcion: int = int(input("\nIngresa tu opción: "))
    
        if seleccionarOpcion == 1:
            self.opcionSeleccionada1()
        elif seleccionarOpcion == 2:
            self.opcionSeleccionada14()
        else:
            print("\nIngresa una opción válida.\n")
            self.mostrarOpcionesBibliotecaVacia()
    
    def mostrarOpcionesBibliotecaIniciada(self):
        print("1. Agregar un libro.")
        print("2. Eliminar un libro.")
        print("3. Buscar un libro por su género.")
        print("4. Buscar un libro por su título.")
        print("5. Buscar un libro por su autor.")
        print("6. Buscar un libro por su año de publicación.")
        print("7. Mirar libros disponibles para alquilar.")
        print("8. Mirar libros alquilados.")
        print("9. Mirar libros disponibles para alquilar por género.")
        print("10. Mirar libros alquilados por género.")
        print("11. Alquilar libro por su género.")
        print("12. Alquilar libro.")
        print("13. Devolver libro.")
        print("14. Ingresos totales por alquileres de libros hasta el momento.")
        print("15. Intercambiar un libro deteriorado por un libro nuevo.")
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
        elif seleccionarOpcion == 7:
            self.opcionSeleccionada7()
        elif seleccionarOpcion == 8:
            self.opcionSeleccionada8()
        elif seleccionarOpcion == 9:
            self.opcionSeleccionada9()
        elif seleccionarOpcion == 10:
            self.opcionSeleccionada10()
        elif seleccionarOpcion == 11:
            self.opcionSeleccionada11()
        elif seleccionarOpcion == 12:
            self.opcionSeleccionada12()
        elif seleccionarOpcion == 13:
            self.opcionSeleccionada13()
        elif seleccionarOpcion == 14:
            self.opcionSeleccionada14()
        elif seleccionarOpcion == 15:
            self.opcionSeleccionada15()
        else:
            print("\nIngresa una opción válida\n")
            self.mostrarOpcionesBibliotecaIniciada()

    def opcionSeleccionada1(self):
        print("\n================= Ingresemos el libro =================")
        funcionesBiblioteca = FuncionalidadesBiblioteca(self.librosParaAlquilar, self.biblioteca)
        funcionesBiblioteca.agregarLibro()

    def opcionSeleccionada2(self):
        print("\n================= Eliminemos el libro =================")
        numeroLibro: str = input("Ingresa el número del libro que quieres eliminar: ")

        funcionesBiblioteca = FuncionalidadesBiblioteca(self.librosParaAlquilar, self.biblioteca)
        funcionesBiblioteca.eliminarLibro(numeroLibro)
    
    def opcionSeleccionada3(self):
        print("\n================= Busquemos el libro =================")
        generoLibro: str = input("Ingesa el género del libro: ")

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorGenero(generoLibro)

    def opcionSeleccionada4(self):
        print("\n================= Busquemos el libro =================")
        tituloLibro: str = input("Ingesa el título del libro: ")

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorTitulo(tituloLibro)

    def opcionSeleccionada5(self):
        print("\n================= Busquemos el libro =================")
        autorLibro: str = input("Ingesa el autor del libro: ")

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorAutor(autorLibro)

    def opcionSeleccionada6(self):
        print("\n================= Busquemos el libro =================")
        añoPublicacion: int = int(input("Ingesa el año de publicación del libro: "))

        buscadorDeLibros = Buscador(self.biblioteca, self.librosParaAlquilar)
        buscadorDeLibros.buscarLibroPorAñoPublicacion(añoPublicacion)

    def opcionSeleccionada7(self):
        print("\n================= Libros disponibles para alquilar =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosDisponiblesParaAlquilar()

    def opcionSeleccionada8(self):
        print("\n================= Libros alquilados =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosAlquilados()

    def opcionSeleccionada9(self):
        print("\n================= Libros disponibles para alquilar por género =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosDisponiblesPorGeneroParaAlquilar()

    def opcionSeleccionada10(self):
        print("\n================= Libros alquilados por género =================")
        listados = Listados(self.librosParaAlquilar, self.librosAlquilados)
        listados.enlistarLibrosAlquiladosPorGenero()

    def opcionSeleccionada11(self):
        print("\n================= Alquilemos un libro por su género =================")
        generoLibro: str = input("Ingesa el género del libro: ")

        if self.librosParaAlquilar.length > 0:
            alquiler = Alquiler(self.librosParaAlquilar, self.librosAlquilados, self.historialLibrosAlquilados)
            alquiler.alquilarLibroPorGenero(generoLibro)

        else:
            print(f"\nNo hay libros para alquilar con el género {generoLibro}")


    def opcionSeleccionada12(self):
        print("\n================= Alquilemos un libro =================")
        numeroLibro: str = input("Ingesa el número del libro: ")

        if self.librosParaAlquilar.length > 0:
            alquiler = Alquiler(self.librosParaAlquilar, self.librosAlquilados, self.historialLibrosAlquilados)
            alquiler.alquilarLibro(numeroLibro)

        else:
            print(f"\nNo hay un libro para alquilar con el número de libro: {numeroLibro}")

    def opcionSeleccionada13(self):
        print("\n================= Devolvamos un libro =================")
        numeroLibro: str = input("Ingesa el número del libro: ")

        if self.librosAlquilados.length > 0:
            devolver = Devolucion(self.librosParaAlquilar, self.librosAlquilados, self.biblioteca)
            devolver.devolverLibro(numeroLibro)

        else:
            print(f"\nNo hay un libro para devolver con el número de libro: {numeroLibro}")
    
    def opcionSeleccionada14(self):
        print("\n================= Finanzas de la biblioteca =================")
        
        if self.historialLibrosAlquilados.length > 0:
            finanzasBiblioteca = Finanzas(self.historialLibrosAlquilados)
            print(f"Los ingresos totales de la biblioteca son: {finanzasBiblioteca.calcularIngresosTotalesPorAlquileres()}")
        
        else:
            print("No se han alquilado libros.")
            print("\nIngresos totales hasta el momento: 0")

    def opcionSeleccionada15(self):
        print("\n================= Intercambiemos un libro deteriorado =================")
        numeroLibro: str = input("Ingesa el número del libro deteriorado: ")

        intercambio = Intercambio(self.librosParaAlquilar, self.librosAlquilados, self.biblioteca)
        intercambio.saberLibroDeteriorado(numeroLibro)

menu = Menu()
menu