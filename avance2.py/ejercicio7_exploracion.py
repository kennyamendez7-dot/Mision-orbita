# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrante: Kennya Mendez
# Fecha: 06/11/2026
# Versión: 8.0
# Descripción: Simula las actividades de exploración científica,
# calcula el consumo de recursos y acumula los puntos científicos.

# ============================================================

# Actividad 1: Analizar terreno
ENERGY_COST_ACT1 = 8
SUPPLIES_COST_ACT1 = 0
SCIENTIFIC_POINTS_ACT1 = 10

# Actividad 2: Recolectar muestra
ENERGY_COST_ACT2 = 12
SUPPLIES_COST_ACT2 = 2
SCIENTIFIC_POINTS_ACT2 = 20

# Actividad 3: Realizar observación
ENERGY_COST_ACT3 = 5
SUPPLIES_COST_ACT3 = 0
SCIENTIFIC_POINTS_ACT3 = 8

# Actividad 4: Finalizar exploración
ENERGY_COST_ACT4 = 0
SUPPLIES_COST_ACT4 = 0
SCIENTIFIC_POINTS_ACT4 = 0

#Acumuladores
scientificPoints = 0
completedActivities = 0
collectedSamples = 0


print(
    "Bienvenido a la Misión Orbita #2.\n\n"
    "A continuación, se presentan las actividades que puede realizar en el planeta.\n"
    "Cada actividad tiene un costo de energía y provisiones, además de otorgar puntos científicos.\n"
    "Si no tiene suficiente energía o provisiones, no podrá realizar la actividad seleccionada y el programa va a finalizar.\n"
)

energyAvailable = int (input("Cual es la energia diaponible al llegar al destino? "))
provisionsAvailable = int (input("Cuantas provisiones tienen diaponibles al momento de llegar al destino? "))

#Ciclo para realizar actividades hasta que el usuario decida salir
continueChoice = True
while continueChoice:

    #Datos de entrada

    print(
        "Actividades que puede realizar en el planeta:\n"
        "Actividad 1: Analizar terreno\n"
        "Actividad 2: Recolectar muestra\n"
        "Actividad 3: Realizar observación\n"
        "Actividad 4: Finalizar exploración\n\n"
    )
    activity = int(input("Ingrese el número correspondiente de la actividad que desea realizar: "))

    #Verificación de la actividad seleccionada y actualización de los acumuladores
   
    if activity == 1:
        if energyAvailable >= ENERGY_COST_ACT1 and provisionsAvailable >= SUPPLIES_COST_ACT1:
            energyAvailable -= ENERGY_COST_ACT1
            provisionsAvailable -= SUPPLIES_COST_ACT1
            scientificPoints += SCIENTIFIC_POINTS_ACT1
            completedActivities += 1
            print("Actividad realizada: Analizar terreno. Puntos obtenidos:", SCIENTIFIC_POINTS_ACT1, "\n")
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continueChoice = False


    elif activity == 2:
        if energyAvailable >= ENERGY_COST_ACT2 and provisionsAvailable >= SUPPLIES_COST_ACT2:
            energyAvailable -= ENERGY_COST_ACT2
            provisionsAvailable -= SUPPLIES_COST_ACT2
            scientificPoints += SCIENTIFIC_POINTS_ACT2
            completedActivities += 1
            collectedSamples += 1
            print("Actividad realizada: Recolectar muestra. Puntos obtenidos:", SCIENTIFIC_POINTS_ACT2, "\n")
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continueChoice = False

    
    elif activity == 3:
        if energyAvailable >= ENERGY_COST_ACT3 and provisionsAvailable >= SUPPLIES_COST_ACT3:
            energyAvailable -= ENERGY_COST_ACT3
            provisionsAvailable -= SUPPLIES_COST_ACT3
            scientificPoints += SCIENTIFIC_POINTS_ACT3
            completedActivities += 1
            print("Actividad realizada: Realizar observación. Puntos obtenidos:", SCIENTIFIC_POINTS_ACT3, "\n")
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continueChoice = False


    elif activity == 4:
        print("Exploración finalizada por la tripulación.")
        continueChoice = False

    if activity < 1 or activity > 4:
        print("Actividad inválida. Por favor, seleccione una actividad válida (1-4).")

# Resumen de la exploración
print("Resumen de la exploración:")
print(f"Actividades realizadas: {completedActivities}")
print(f"Muestras recolectadas: {collectedSamples}")
print(f"Puntos científicos: {scientificPoints}")
print(f"Energía restante: {energyAvailable} unidades")
print(f"Provisiones restantes: {provisionsAvailable} unidades")

