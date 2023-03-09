# ejercico_4
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / altura**2

if imc < 16:
    print("Su IMC es", imc, "y se encuentra en el criterio de ingreso en hospital.")
elif imc >= 16 and imc < 17:
    print("Su IMC es", imc, "y se encuentra en infrapeso.")
elif imc >= 17 and imc < 18:
    print("Su IMC es", imc, "y se encuentra en bajo peso.")
elif imc >= 18 and imc < 25:
    print("Su IMC es", imc, "y se encuentra en peso normal (saludable).")
elif imc >= 25 and imc < 30:
    print("Su IMC es", imc, "y se encuentra en sobrepeso (obesidad de grado I).")
elif imc >= 30 and imc < 35:
    print("Su IMC es", imc, "y se encuentra en sobrepeso crónico (obesidad de grado II).")
elif imc >= 35 and imc < 40:
    print("Su IMC es", imc, "y se encuentra en obesidad premórbida (obesidad de grado III).")
else:
    print("Su IMC es", imc, "y se encuentra en obesidad mórbida (obesidad de grado IV).")