class Paciente:
    
    def __init__(self, numeroPaciente: str, genero: str, nombre: str, Edad: int, Triaje: int):
        self.numeroPaciente = numeroPaciente
        self.genero = genero
        self.nombre = nombre
        self.Edad = Edad
        self.Triaje = Triaje

    def __lt__(self, otro):
        return self.Triaje < otro.Triaje

    def __le__(self, otro):
        return self.Triaje <= otro.Triaje

    def __gt__(self, otro):
        return self.Triaje > otro.Triaje

    def __ge__(self, otro):
        return self.Triaje >= otro.Triaje

    def __eq__(self, otro):
        return self.Triaje == otro.Triaje

    def __ne__(self, otro):
        return self.Triaje != otro.Triaje

    
    def __eq__(self, otro):
        return self.numeroPaciente == otro.numeroPaciente

    def __str__(self):
        return f'{self.nombre} --- {self.Triaje}'