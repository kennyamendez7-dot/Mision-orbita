# Archivo: ejercicio2.py 
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0 
# Integrante: Kennya Mendez 
# Fecha: 13/10/2026        
# Versión: 4.0 
# Descripción: Verificación de combustible 

# ============================================================

# 1. Entrada de datos
combustibleDisponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustibleDeIda = int(input("Ingrese la cantidad de combustible requerida para el viaje de ida: "))
combustibleDeVuelta = int(input("Ingrese la cantidad de combustible requerida para el viaje de regreso: "))

# 2. Cálculos
reservaDeEmergencia = 10
combustibleTotalRequerido = combustibleDeIda + combustibleDeVuelta + reservaDeEmergencia
combustibleAdicional = combustibleDisponible - combustibleTotalRequerido

# 3. Salida de datos
print(f"Combustible disponible: {combustibleDisponible}")
print(f"Combustible requerido para ir: {combustibleDeIda}")
print(f"Combustible requerido para regresar: {combustibleDeVuelta}")
print(f"Reserva de emergencia: {reservaDeEmergencia}")
print(f"Combustible total requerido: {combustibleTotalRequerido}")

# 4. Condicional
if combustibleAdicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")

