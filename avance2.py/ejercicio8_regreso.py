# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrante: Kennya Mendez
# Fecha: 08/11/2026
# Versión: 5.0
# Descripción: Evalúa los recursos disponibles para el regreso
# de la tripulación a la Tierra y calcula los días de supervivencia
# en caso de que la nave no pueda regresar.

# ============================================================


# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrante: Kennya Mendez
# Fecha: 08/11/2026
# Versión: 1.0
# Descripción: Evalúa el regreso de la tripulación a la Tierra
# y calcula su supervivencia cuando no puede regresar.

# ============================================================

# Constantes del consumo diario de recursos
FUEL_COST_DAY = 8
OXYGEN_COST_PERSON_DAY = 2
ENERGY_COST_DAY = 5
SUPPLIES_COST_PERSON_DAY = 1

# Mensaje de bienvenida
print(
    "Bienvenido a la Misión Órbita #2.\n\n"
    "En esta etapa se evaluará si la tripulación puede regresar a la Tierra.\n"
    "Si hay suficiente combustible, se simulará el viaje de regreso.\n"
    "Si no hay suficiente combustible, se calculará el tiempo de supervivencia.\n"
)

# Datos de entrada
crewMembers = int(input("¿Cuántos tripulantes tiene la nave? "))
travelDays = int(input("¿Cuántos días duró el viaje de ida? "))
fuelAvailable = int(input("¿Cuánto combustible tiene disponible la nave? "))
oxygenAvailable = int(input("¿Cuánto oxígeno tiene disponible la nave? "))
energyAvailable = int(input("¿Cuánta energía tiene disponible la nave? "))
suppliesAvailable = int(input("¿Cuántas provisiones tiene disponible la nave? "))

# Cálculo del combustible necesario para regresar
fuelRequired = travelDays * FUEL_COST_DAY

# Consumo diario según la cantidad de tripulantes
dailyOxygen = crewMembers * OXYGEN_COST_PERSON_DAY
dailySupplies = crewMembers * SUPPLIES_COST_PERSON_DAY

# Decisión sobre el regreso de la nave
if fuelAvailable >= fuelRequired:

    # Caso A: La nave tiene combustible para iniciar el regreso
    print("La nave inicia el viaje de regreso a la Tierra.")

    completedDays = 0
    returnActive = True

    # Ciclo para simular cada día del regreso
    while completedDays < travelDays and returnActive:

        # Verificación de los cuatro recursos necesarios
        if (fuelAvailable >= FUEL_COST_DAY and
            oxygenAvailable >= dailyOxygen and
            energyAvailable >= ENERGY_COST_DAY and
            suppliesAvailable >= dailySupplies):

            # Descuento de los recursos consumidos durante el día
            fuelAvailable -= FUEL_COST_DAY
            oxygenAvailable -= dailyOxygen
            energyAvailable -= ENERGY_COST_DAY
            suppliesAvailable -= dailySupplies

            # Actualización del contador de días completados
            completedDays += 1

            # Estado de los recursos después de cada día
            print(
                f"Día {completedDays} | "
                f"Combustible: {fuelAvailable} | "
                f"Oxígeno: {oxygenAvailable} | "
                f"Energía: {energyAvailable} | "
                f"Provisiones: {suppliesAvailable}"
            )

        else:
            # El regreso se interrumpe si algún recurso no alcanza
            returnActive = False

    # Evaluación del resultado del viaje
    if completedDays == travelDays:

        print("La tripulación regresó exitosamente a la Tierra.")
        print(f"Combustible restante: {fuelAvailable} unidades")
        print(f"Oxígeno restante: {oxygenAvailable} unidades")
        print(f"Energía restante: {energyAvailable} unidades")
        print(f"Provisiones restantes: {suppliesAvailable} unidades")

    else:
        # Identificación del día que no pudo completarse
        interruptedDay = completedDays + 1

        print(f"El regreso se interrumpió en el día {interruptedDay}.")

        # Identificación de los recursos insuficientes
        if oxygenAvailable < dailyOxygen:
            print("Recurso insuficiente: oxígeno")

        if energyAvailable < ENERGY_COST_DAY:
            print("Recurso insuficiente: energía")

        if suppliesAvailable < dailySupplies:
            print("Recurso insuficiente: provisiones")

        print("La tripulación no completó el regreso.")

else:
    # Caso B: No existe combustible suficiente para regresar
    print("La tripulación quedó varada en el destino.")

    # Cálculo de los días completos de supervivencia por recurso
    oxygenDays = oxygenAvailable // dailyOxygen
    energyDays = energyAvailable // ENERGY_COST_DAY
    suppliesDays = suppliesAvailable // dailySupplies

    print(f"Días por oxígeno: {oxygenDays}")
    print(f"Días por energía: {energyDays}")
    print(f"Días por provisiones: {suppliesDays}")

    # Determinación del menor número de días de supervivencia
    survivalDays = oxygenDays

    if energyDays < survivalDays:
        survivalDays = energyDays

    if suppliesDays < survivalDays:
        survivalDays = suppliesDays

    print(f"Supervivencia estimada: {survivalDays} días")

    # Identificación de todos los recursos limitantes
    limitingResources = ""

    if oxygenDays == survivalDays:
        limitingResources = "oxígeno"

    if energyDays == survivalDays:
        if limitingResources != "":
            limitingResources += ", "
        limitingResources += "energía"

    if suppliesDays == survivalDays:
        if limitingResources != "":
            limitingResources += ", "
        limitingResources += "provisiones"

    print(f"Recurso(s) limitante(s): {limitingResources}")
