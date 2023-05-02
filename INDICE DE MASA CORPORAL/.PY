#calculadora de indice de masa corporal (imc)

contador =0

while contador != 2:
    contador = int(input("Quieres seguir calculando el indice de masa corporal? 1.si y 2.no \n"))

    if contador ==1:
        estatura = float(input("ingrese su estatura en metros:"))
        peso = float(input("ingrese su peso en kilogramos: "))
        resultado = round(peso/(estatura ** 2), 2)

        if resultado < 18.5:
            print(f'Indice de masa corporal {resultado} = Bajo de peso')
        elif 18.5 < resultado < 24.99:
            print(f'Indice de masa corporal {resultado} = Peso normal')
        elif 25 < resultado <30:
            print(f'Indice de masa corporal {resultado} = Sobrepeso')
        elif resultado > 30:
            print(f'Indice de masa corporal {resultado} = Obesidad')
