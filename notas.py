def promedio(notas):
    return round(sum(notas) / len(notas), 2)


def aprobado(nota):
    return nota >= 60


def mejor(notas):
    return max(notas)


def peor(notas):
    return min(notas)


def rango(notas):
    return max(notas) - min(notas)


def aprobados(notas):
    return [nota for nota in notas if aprobado(nota)]


def cantidad(notas):
    return len(notas)


def desaprobados(notas):
    return [nota for nota in notas if not aprobado(nota)]
