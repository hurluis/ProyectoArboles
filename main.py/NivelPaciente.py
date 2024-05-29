from Hospital import Hospital
from Paciente import Paciente

class NivelPaciente:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital

    def encontrarNivelValor(self, nodo, valor, nivel=0):
        if nodo is None:
            return -1  # Retorna -1 si no encuentra el valor

        if nodo.value.numeroPaciente == valor:
            return nivel

        nivel_izquierdo = self.encontrarNivelValor(nodo.leftchild, valor, nivel + 1)
        if nivel_izquierdo != -1:
            return nivel_izquierdo

        nivel_derecho = self.encontrarNivelValor(nodo.rightchild, valor, nivel + 1)
        return nivel_derecho

    def buscarNivel(self, valor):
        return self.encontrarNivelValor(self.hospital.root, valor)