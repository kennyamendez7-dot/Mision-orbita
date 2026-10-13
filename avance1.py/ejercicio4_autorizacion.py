# Archivo: ejercicio4.py 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrante: Kennya Mendez 
# Fecha: 13/10/2026        
# Versión:3.0 
# Descripción: Autorización inicial de lanzamiento

# ============================================================

# 1. Entrada de datos
combustibleDisponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustibleIda = int(input("Ingrese la cantidad de combustible requerida para llegar al destino: "))
combustibleRegreso = int(input("Ingrese la cantidad de combustible requerida para regresar: "))
oxigenoDisponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigenoRequerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
energiaDisponible = int(input("Ingrese la cantidad de energía disponible: "))
energiaRequerida = int(input("Ingrese la cantidad de energía requerida: "))
provisionesDisponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisionesRequeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# 2. Cálculo del combustible total requerido
combustibleTotalRequerido = combustibleIda + combustibleRegreso + 10

# 3. Verificación de condiciones
if (combustibleDisponible >= combustibleTotalRequerido and
    oxigenoDisponible >= oxigenoRequerido and
    energiaDisponible >= energiaRequerida and
    provisionesDisponibles >= provisionesRequeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")