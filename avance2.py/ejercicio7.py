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
    "Bienvenido a la Misión Orbita #2.\n"
    "A continuación, se presentan las actividades que puede realizar en el planeta.\n"
    "Cada actividad tiene un costo de energía y provisiones, además de otorgar puntos científicos.\n\n"
    "Actividad 1: Analizar terreno\n"
    "Actividad 2: Recolectar muestra\n"
    "Actividad 3: Realizar observación\n"
    "Actividad 4: Finalizar exploración\n\n"
    "Si no tiene suficiente energía o provisiones, no podrá realizar la actividad seleccionada.\n"
)

energyAvailable = float(input("Cual es la energia diaponible al llegar al destino? "))
provisionsAvailable = float(input("Cuantas provisiones tienen diaponibles al momento de llegar al destino? "))

#Ciclo para realizar actividades hasta que el usuario decida salir
continueChoice = "s"
while continueChoice.lower() == "s":

    #Datos de entrada
    activity = float(input("Ingrese el número correspondiente de la actividad que desea realizar: "))

    #Verificación de la actividad seleccionada y actualización de los acumuladores
    activity == 1
    if activity == 1:
        if energyAvailable >= ENERGY_COST_ACT1 and provisionsAvailable >= SUPPLIES_COST_ACT1:
            energyAvailable -= ENERGY_COST_ACT1
            provisionsAvailable -= SUPPLIES_COST_ACT1
            scientificPoints += SCIENTIFIC_POINTS_ACT1
            completedActivities += 1
            print("Actividad 1 completada. Puntos científicos obtenidos:", SCIENTIFIC_POINTS_ACT1)
        else:
            print("No tiene suficiente energía o provisiones para realizar la actividad 1.")


    activity == 2
    if activity == 2:
        if energyAvailable >= ENERGY_COST_ACT2 and provisionsAvailable >= SUPPLIES_COST_ACT2:
            energyAvailable -= ENERGY_COST_ACT2
            provisionsAvailable -= SUPPLIES_COST_ACT2
            scientificPoints += SCIENTIFIC_POINTS_ACT2
            completedActivities += 1
            collectedSamples += 1
            print("Actividad 2 completada. Puntos científicos obtenidos:", SCIENTIFIC_POINTS_ACT2)
        else:
            print("No tiene suficiente energía o provisiones para realizar la actividad 2.")

    activity == 3
    if activity == 3:
        if energyAvailable >= ENERGY_COST_ACT3 and provisionsAvailable >= SUPPLIES_COST_ACT3:
            energyAvailable -= ENERGY_COST_ACT3
            provisionsAvailable -= SUPPLIES_COST_ACT3
            scientificPoints += SCIENTIFIC_POINTS_ACT3
            completedActivities += 1
            print("Actividad 3 completada. Puntos científicos obtenidos:", SCIENTIFIC_POINTS_ACT3)
        else:
            print("No tiene suficiente energía o provisiones para realizar la actividad 3.")

    activity == 4
    if activity == 4:
        if energyAvailable >= ENERGY_COST_ACT4 and provisionsAvailable >= SUPPLIES_COST_ACT4:
            energyAvailable -= ENERGY_COST_ACT4
            provisionsAvailable -= SUPPLIES_COST_ACT4
            scientificPoints += SCIENTIFIC_POINTS_ACT4
            completedActivities += 1
            print("Actividad 4 completada. Puntos científicos obtenidos:", SCIENTIFIC_POINTS_ACT4)
        else:
            print("No tiene suficiente energía o provisiones para realizar la actividad 4.")    

    if activity < 1 or activity > 4:
        print("Actividad inválida. Por favor, seleccione una actividad válida (1-4).")
    if energyAvailable <= 5 or provisionsAvailable <= 2:
        print("No tiene suficiente energía o provisiones para continuar con las actividades, su unica opcion es finalizar la exploración, por favor, no continue con el programa.")


# Confirmación para continuar o salir del ciclo
    continueChoice = input("¿Desea realizar otra actividad? (s/n): ")

# Resumen de la exploración
print("Resumen de la exploración:")
print(f"Actividades realizadas: {completedActivities}")
print(f"Muestras recolectadas: {collectedSamples}")
print(f"Puntos científicos: {scientificPoints}")
print(f"Energía restante: {energyAvailable} unidades")
print(f"Provisiones restantes: {provisionsAvailable} unidades")

"""
{
    "Actividad 1: Analizar el terreno": {"costoEnergia": 8, "costoProvisiones": 0, "puntosCientificos": 10},
    "Actividad 2: Recolectar muestras": {"costoEnergia": 12, "costoProvisiones": 2, "puntosCientificos": 20},
    "Actividad 3: Realizar observacion": {"costoEnergia": 5, "costoProvisiones": 0, "puntosCientificos": 8},
    "Actividad 4: Fninalizar exploracion": {"costoEnergia": 0, "costoProvisiones": 0, "puntosCientificos": 0},
}

for actividad, detalles in actividades.items():
    print(f"{actividad}: Costo de Energia: {detalles['costoEnergia']}, Costo de Provisiones: {detalles['costoProvisiones']}, Puntos Cientificos: {detalles['puntosCientificos']}, ]}")
    """




