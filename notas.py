def promedio(notas):
    return round(sum(notas) / len(notas), 2)


def aprobado(nota):
    return nota >= 51
