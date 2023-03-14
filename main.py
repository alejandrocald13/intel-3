mayor = 0
residuo = 0
residuo = mayor % 2

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

if residuo == 0:
    print(f'El número {mayor} es par porque su residuo es 0.')
else:
    print(f'El número {mayor} es impar porque su residuo es {residuo}.')
