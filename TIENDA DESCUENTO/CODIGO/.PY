nombre = input("Ingrese el nombre del cliente:")
valor_compra= float(input("Ingrese el valor de la compra: "))

#Establecer condiciones

if valor_compra <80:
    print(f'hola, {nombre}. El valor a pagar es: $ {valor_compra}')
elif 80<= valor_compra < 150:
    descuento=0.1
elif 150<= valor_compra <= 300:
    descuento=0.15
elif 300<= valor_compra < 500:
    descuento=0.2

#obtener el precio final usando la formula indicada en el problema

precio_final = valor_compra - (valor_compra * descuento)

#imprima los resultados

print(f'Compra sin descuento: {valor_compra} . \nCompra con descuento: {precio_final} ')

