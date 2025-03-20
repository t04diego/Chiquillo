respuesta='si'
print('Quieres realizar tu total')

while respuesta=='si':
    cuenta=float(input('Dame el total de tu compra: $'))
    iva=cuenta*.16
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