class Paciente:
    
    def __init__(self, numeroPaciente: int, genero: str, nombre: str, Edad: int, Triaje: int):
        self.numeroPaciente = numeroPaciente
        self.genero = genero
        self.nombre = nombre
        self.Edad = Edad
        self.Triaje = Triaje

    def __str__(self):
        return f'{self.nombre} --- {self.Triaje}'
    
 