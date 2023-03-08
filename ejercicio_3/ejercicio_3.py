# ejercicio_3
# Pedimos al usuario que ingrese el precio de costo del artículo
precio_costo = float(input("Ingrese el precio de costo del artículo: "))

# Calculamos la ganancia en función del precio de costo
if precio_costo < 3000:
    ganancia = precio_costo * 0.15
elif precio_costo >= 3000 and precio_costo <= 6000:
    ganancia = 500
else:
    ganancia = precio_costo * 0.25

# Calculamos el precio de venta sumando la ganancia al precio de costo
precio_venta = precio_costo + ganancia

# Mostramos el precio de venta al usuario
print(f"El precio de venta del artículo es: {precio_venta}")