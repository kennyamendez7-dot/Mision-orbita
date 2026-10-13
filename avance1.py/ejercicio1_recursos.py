# Archivo: ejercicio1.py 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrante: Kennya Mendez 
# Fecha: 13/10/2026        
# Versión: 6.0 
# Descripción: Calcula los recursos necesarios para una misión. 

# ============================================================

# 1. Entrada de datos
nombreMision = input("Nombre de la misión: ") 
cantidadDeTripulantes = int(input("Cantidad de tripulantes: "))
diasDeViaje = int(input("Cantidad de días estimados para llegar al destino: "))

# 2. Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE_EMERGENCIA = 10
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
TRAMOS_VIAJE = 2  # Representa el viaje de ida y regreso
RESERVA_OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_DIA = 5
RESERVA_ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
RESERVA_PROVISIONES_EMERGENCIA = 3

# 2. Cálculo de recursos requeridos 
combustibleDeIda = diasDeViaje * CONSUMO_COMBUSTIBLE_DIA
combustibleDeVuelta = diasDeViaje * CONSUMO_COMBUSTIBLE_DIA
combustibleTotal = combustibleDeIda + combustibleDeVuelta + RESERVA_COMBUSTIBLE_EMERGENCIA

oxigenoRequerido = (diasDeViaje * CONSUMO_OXIGENO_TRIPULANTE_DIA * TRAMOS_VIAJE * cantidadDeTripulantes) + RESERVA_OXIGENO_EMERGENCIA
energiaRequerida = (diasDeViaje * CONSUMO_ENERGIA_DIA * TRAMOS_VIAJE) + RESERVA_ENERGIA_EXPLORACION
provisionesRequeridas = (diasDeViaje * cantidadDeTripulantes * TRAMOS_VIAJE * CONSUMO_PROVISIONES_TRIPULANTE_DIA) + RESERVA_PROVISIONES_EMERGENCIA

# 3. Salida de datos 
print(f"Nombre de la misión: {nombreMision}")
print(f"El combustible requerido para la ida es: {combustibleDeIda} litros")
print(f"El combustible requerido para la vuelta es: {combustibleDeVuelta} litros")
print(f"El combustible total requerido es: {combustibleTotal} litros")
print(f"El oxígeno requerido es: {oxigenoRequerido} kg")
print(f"La energía requerida es: {energiaRequerida} kWh")
print(f"Las provisiones requeridas son: {provisionesRequeridas} kg")