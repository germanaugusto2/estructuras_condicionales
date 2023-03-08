# ejercico_2
# Definición de la función de préstamo
def solicitar_prestamo():
    ingresos = float(input("Ingrese sus ingresos mensuales: "))
    deudas = float(input("Ingrese el total de sus deudas pendientes: "))
    
    # Verificación de los requisitos
    if ingresos > 945200 and deudas == 0:
        monto = float(input("Ingrese el monto a solicitar: "))
        print("Su préstamo ha sido aprobado por un monto de ${:.2f}".format(monto))
    else:
        print("Lo sentimos, no cumple con los requisitos para obtener un préstamo.")
    
# Llamada a la función de préstamo
solicitar_prestamo()
