# TRABAJO PRÁCTICO N°7 - ESTRUCTURAS DE DATOS COMPLEJOS

#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Precios actualizados
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista
# que contenga únicamente las frutas sin los precios.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Punto 3: Crear lista con solo las frutas
frutas = list(precios_frutas.keys())

print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

# diccionario vacío para los contactos
contactos = {}

print("=== Cargar 5 contactos ===")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el teléfono de {nombre}: ")
    contactos[nombre] = telefono

print("\nContactos cargados correctamente!")
print(contactos)

print("\n=== Consultar contacto ===")
nombre_buscar = input("Ingrese el nombre a buscar: ")

if nombre_buscar in contactos:
    print(f"El teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"El contacto {nombre_buscar} no existe en la agenda")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

# 1) Palabras únicas usando set
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# diccionario con la cantidad de veces que aparece cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1  # si ya existe, sumar 1
    else:
        recuento[palabra] = 1   # si no existe, inicializar en 1

print(f"Recuento: {recuento}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

print("=== Cargar datos de 3 alumnos ===")
for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    
    nota1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
    
    # Guardamos las notas como tupla
    alumnos[nombre] = (nota1, nota2, nota3)
    
print("\n=== Promedios ===")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Estudiantes que aprobaron cada parcial
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 105, 106, 107}

# 1) Los que aprobaron ambos parciales
ambos = parcial1 & parcial2
print(f"Aprobaron ambos: {ambos}")

# 2) Los que aprobaron al menos un parcial
solo_uno = parcial1 ^ parcial2
print(f"Aprobaron solo uno: {solo_uno}")

# 3) totos los que aprobaron algo (juntamos los dos sets)
todos = parcial1 | parcial2
print(f"Aprobaron al menos uno: {todos}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario con algunos productos
stock = {
    "Manzanas": 50,
    "Bananas": 30,
    "Naranjas": 40
}

print("=== Sistema de Stock ===")
print("Stock inicial:", stock)

while True:
    print("\n--- OPCIONES ---")
    print("1. Consultar stock")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    
    opcion = input("\nSeleccione una opción (1-4): ")
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]} unidades")
        else:
            print(f"El producto {producto} no existe")
    
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock:
            cantidad = int(input(f"¿Cuántas unidades agregar a {producto}? "))
            stock[producto] += cantidad
            print(f"Nuevo stock de {producto}: {stock[producto]} unidades")
        else:
            print(f"El producto {producto} no existe. Use la opción 3 para agregarlo.")
    
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto in stock:
            print(f"El producto {producto} ya existe. Use la opción 2 para agregar unidades.")
        else:
            cantidad = int(input(f"¿Cuántas unidades de {producto}? "))
            stock[producto] = cantidad
            print(f"Producto {producto} agregado con {cantidad} unidades")
    
    elif opcion == "4":
        print("Stock final:", stock)
        break
    
    else:
        print("Opción inválida. Intente nuevamente.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos

agenda = {
    ("lunes", "10:00"): "Trabajo",
    ("martes", "15:00"): "Clase de Programación",
    ("miércoles", "09:00"): "Dentista",
    ("jueves", "18:00"): "Gimnasio",
    ("viernes", "12:00"): "Parcial 2 de Programación"
}

print("=== AGENDA ===")
for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora}: {evento}")

# evento específico
print("\n=== CONSULTAR EVENTO ===")
dia_buscar = input("Ingrese el día: ")
hora_buscar = input("Ingrese la hora: ")

# Creamos tupla con los datos ingresados
clave = (dia_buscar, hora_buscar)

if clave in agenda:
    print(f"Evento: {agenda[clave]}")
else:
    print("No hay eventos en ese día y hora")

# Agregar un nuevo evento
print("\n=== AGREGAR EVENTO ===")
dia_nuevo = input("Ingrese el día: ")
hora_nueva = input("Ingrese la hora: ")
evento_nuevo = input("Ingrese el evento: ")

agenda[(dia_nuevo, hora_nueva)] = evento_nuevo
print(f"Evento agregado: {dia_nuevo} a las {hora_nueva} - {evento_nuevo}")

# agenda actualizada
print("\n=== AGENDA ACTUALIZADA ===")
for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora}: {evento}")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# Diccinario: país -> capital
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

# Diccionario invertido: capital -> país
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Original:", original)
print("Invertido:", invertido)