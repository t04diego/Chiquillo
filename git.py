def leer_archivo(nombre_archivo):
    file = open(nombre_archivo, 'r', encoding='utf-8')
    contenido = file.readlines()
    file.close()

    m = []
    cont = 0
    for renglon in contenido:
        renglon = renglon.strip()

        # Agregar número de fila y encabezado a la primera línea
        if cont == 0:
            renglon = 'No\t' + renglon
        else:
            renglon = str(cont) + '\t' + renglon

        # Convertir a lista
        lista = renglon.split('\t')
        m.append(lista)
        cont += 1

    return m

# Función para buscar y modificar un concepto específico
def buscar_y_modificar_concepto(m, concepto_buscar, concepto_reemplazar):
    for f in range(1, len(m)): 
        if m[f][3].strip().lower() == concepto_buscar.lower():
            m[f][3] = concepto_reemplazar
    return m

# Función para seleccionar transacciones por tipo de movimiento
def seleccionar_por_tipo(m, tipo_movimiento):
    seleccionados = []
    for fila in m[1:]: 
        if fila[3].strip().lower() == tipo_movimiento.lower():
            seleccionados.append(fila)
    return seleccionados

# Función para modificar
def modificar_factor(m, columna, factor):
    for f in range(1, len(m)):
        valor = m[f][columna]
        if (str(valor).replace('.', '', 1).isdigit() and str(valor).count('.') < 2):
            m[f][columna] = float(valor) * factor
    return m

# Función para escribir los resultados en un archivo
def escribir_archivo(nombre_archivo, m):
    file = open(nombre_archivo, 'wt')
    for fila in m:
        file.write('\t'.join(map(str, fila)) + '\n')
    file.close()

def funcion():
    archivo_entrada = 'datos_financieros completo.txt'
    archivo_salida = 'resultados.txt'

    # Leer el archivo de entrada
    m = leer_archivo(archivo_entrada)

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Seleccionar transacciones por tipo de movimiento")
        print("2. Buscar y modificar un concepto")
        print("3. Modificar factor y recalcular valores")
        print("4. Guardar y salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            # Seleccionar transacciones por tipo de movimiento
            tipo_movimiento = input('Selecciona el tipo de movimiento (Compra/Venta/Depósito/Retiro): ')
            transacciones_seleccionadas = seleccionar_por_tipo(m, tipo_movimiento)
            print("Transacciones seleccionadas:", transacciones_seleccionadas)
        
        elif opcion == '2':
            # Buscar y modificar un concepto
            concepto_buscar = input('Ingresa el concepto a buscar (Compra/Venta/Depósito/Retiro): ')
            concepto_reemplazar = input('Ingresa el nuevo concepto para reemplazar: ')
            m = buscar_y_modificar_concepto(m, concepto_buscar, concepto_reemplazar)
            print(f"Conceptos '{concepto_buscar}' modificados a '{concepto_reemplazar}' correctamente.")
        
        elif opcion == '3':
            # Modificar un factor
            columna_modificar = int(input('Ingresa el número de columna a modificar: ')) - 1
            factor = float(input('Ingresa el factor de ajuste: '))
            m = modificar_factor(m, columna_modificar, factor)
            print("Valores modificados con el factor proporcionado.")
        
        elif opcion == '4':
            # Salida
            escribir_archivo(archivo_salida, m)
            print("Operaciones completadas. Archivo guardado.")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Llamar a la función principal
funcion()