def compararTriaje(paciente1, paciente2):
    if paciente1.Triaje < paciente2.Triaje:
        return -1
    elif paciente1.Triaje > paciente2.Triaje:
        return 1
    else:
        return 0