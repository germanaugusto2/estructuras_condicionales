#input

a = int(input("Digite el valor del coeficiente a:"))
b = int(input("Digite el valor del coeficiente b:"))
c = int(input("Digite el valor del coeficiente c:"))

#processing

d = (b**2 - 4*a*c)
if d == 0:
    x = (-b/2*a)
    x2 = x
    print (x, x2)
if d > 0:           
    x = (-b + math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print (x, x2)
else:
    print ("La solución es imaginaria")