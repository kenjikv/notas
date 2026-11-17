from notas import promedio, aprobado, rango, mejor

notas = [80, 65, 90, 45, 72]
print("Reporte de notas")
print("----------------")
print("Promedio:", promedio(notas))
print("Aprobado:", aprobado(promedio(notas)))
print("Rango:", rango(notas))
print("Mejor nota:", mejor(notas))
