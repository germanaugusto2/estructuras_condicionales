# input

gasto_fijo=10000

gast_mensual=int(input("gasto mensual del agua: "))

if gast_mensual <=50:
    costo_agua_mensual=gasto_fijo
else:
    if gast_mensual <= 200:
        costo_agua_mensual=gasto_fijo+2000*(gast_mensual-50)
    else:
        costo_agua_mensual=gasto_fijo+3000*(gast_mensual-50)


print(costo_agua_mensual)