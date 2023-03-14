mayor = 0
residuo = 0
num1 = int(input("Ingrese su primer numero: "))
num2 =  int(input("Ingrese su segundo numero: "))
if num1 > num2:
        mayor = num1
        print(mayor)
elif num2 > num1:
        mayor = num2
        print(mayor)
else:
    print(f'{num1} y {num2} son iguales')
    mayor = num1