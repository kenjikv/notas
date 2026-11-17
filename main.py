from notas import promedio, aprobado, rango, mejor, peor

notas = [80, 65, 90, 45, 72]
print("Reporte de notas")
print("----------------")
print("Promedio del curso:", promedio(notas))
print("Aprobado:", aprobado(promedio(notas)))
print("Rango:", rango(notas))
print("Mejor nota:", mejor(notas))
print("Peor nota:", peor(notas))
