respuesta='si'
print('Quieres realizar tu total')


while respuesta=='si':
    cuenta=float(input('Dame el total de tu compra: $'))
    iva=cuenta*.16respuesta='si'

while respuesta=='si':
    print('Programa de operaciones básicas')
    print('1)Suma')
    print('2)Resta')
    print('3)Multiplicación')
    print('4) División')
    print('5) Salir')


    op=int(input('Dime el numero de la operación 1-5: '))
    if op<5: 
        num1=float(input('Dame un numero: '))
        num2=float(input('Dame otro numero: '))

    	if op==1: #Suma
        resultado=num1+num2
        print(f'El resultado de la operacion  es : {resultado:.2f}')

    	elif op==2: #Resta
        resultado=num1-num2
        print(f'El resultado de la operacion  es : {resultado:.2f}')

    	elif op==3: #Multiplicación
        resultado=num1*num2
        print(f'El resultado de la operacion  es : {resultado:.2f}')

    	elif op==4: #División
        if num2!=0:
            resultado=num1/num2
            print(f'El resultado de la operacion  es : {resultado:.2f}')
        else:
            print('No es posible dividir entre cero')


    elif op==5: #salir
        print('Hasta luego')
        
        break

    else:
        print('Seleccion incorrecta, por favor selecciona correctamente la respuesta 1-5 ')
    
    respuesta=input('Quieres hacer otra operación si/no? ')
        
print('Termino el programa....')

    cuenta=cuenta+iva
    print (f'El iva es de ${iva:.2f} y el total de tu compra es de ${cuenta:.2f}')
    
    respuesta=input('Quieres hacer otra operación si/no? ')




hola=1

while hola<=10:
    print('Hola a todos',hola)
    hola=hola+1
print('Hasta luego :D')

suma=0
meses=1

while meses<=12:
    cantidad=float(input('Dame la cantidad ahorrada este mes: $'))
    suma=suma+cantidad
    meses=meses+1
print(f'El ahorro total despues de 12 meses es:{suma:.2f}')
