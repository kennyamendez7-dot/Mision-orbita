# Archivo: ejercicio3.py 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrante: Kennya Mendez 
# Fecha: 13/10/2026        
# Versión: 2.0 
# Descripción: Verificación del soporte para la tripulación 

# ============================================================

# 1. Entrada de datos
oxigenoDisponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigenoRequerido = int(input("Ingrese la cantidad de oxígeno requerida: "))
provisionesDisponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisionesRequeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# 2. Condisiones de verificación
if oxigenoDisponible >= oxigenoRequerido and provisionesDisponibles >= provisionesRequeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
