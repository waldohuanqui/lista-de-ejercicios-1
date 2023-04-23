# Definimos la lista de DNIs y la lista de datos
dnis = ['11111111A', '22222222B', '33333333C']
datos = [['Juan', 25, 'Cusco', 'Datux', 'Curso de Python'],
         ['Ana', 20, 'Lima', 'Datux', 'Curso de SQL'],
         ['Pedro', 30, 'Tacna', 'Datux', 'Curso de Power BI']]

# Pedimos al usuario que ingrese su DNI
dni = input("Ingrese su DNI: ")

# Validamos que el DNI esté en la lista
if dni in dnis:
    # Obtenemos la posición del DNI en la lista
    posicion = dnis.index(dni)
    # Obtenemos los datos del usuario en la posición correspondiente
    datos_usuario = datos[posicion]
    # Validamos que el usuario tenga más de 18 años y que esté en el curso de Python
    if datos_usuario[1] > 18 and datos_usuario[3] == 'Fisica' and datos_usuario[4] == 'Curso de Python':
        print("Bienvenido/a,", datos_usuario[0])
    else:
        print("No cumple con los requisitos para el curso de Python")
else:
    print("No está autorizado/a para ingresar al curso")