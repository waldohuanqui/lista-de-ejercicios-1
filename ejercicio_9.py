# Creamos las tres listas vacías
lista_python = []
lista_sql = []
lista_power_bi = []

# Mostramos las opciones al usuario
print("Opciones:")
print("1. Agregar a lista de Python")
print("2. Agregar a lista de SQL")
print("3. Agregar a lista de Power BI")

# Pedimos al usuario que seleccione una opción
opcion = int(input("Seleccione una opción (1-3): "))

# Pedimos al usuario que ingrese un elemento para la lista correspondiente
if opcion == 1:
    elemento = input("Ingrese un elemento para la lista de Python: ")
    lista_python.append(elemento)
elif opcion == 2:
    elemento = input("Ingrese un elemento para la lista de SQL: ")
    lista_sql.append(elemento)
elif opcion == 3:
    elemento = input("Ingrese un elemento para la lista de Power BI: ")
    lista_power_bi.append(elemento)
else:
    print("Opción no válida")

# Mostramos las tres listas
print("Lista de Python:", lista_python)
print("Lista de SQL:", lista_sql)
print("Lista de Power BI:", lista_power_bi)