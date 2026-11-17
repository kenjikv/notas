def promedio(notas):
    return round(sum(notas) / len(notas), 2)


def aprobado(nota):
    return nota >= 51


def mejor(notas):
    return max(notas)


def peor(notas):
    return min(notas)
