# Programa que lea las coordenadas cartesianas (x, y) 

x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante.")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuarto cuadrante.")
elif x == 0 and y != 0:
    print("El punto se encuentra sobre el eje y.")
elif x != 0 and y == 0:
    print("El punto se encuentra sobre el eje x.")
else:
    print("El punto se encuentra en el origen.")