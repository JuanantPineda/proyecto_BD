def menuDB():
    menu = '''Bien venido al menu de la Bases de datos
    1. MariaDB
    2. Postgres
    3. Oracle
    4. Salir
    '''
    print(menu)
    while True:
        try:
            opcion = int(input("Elija un numero para ingresar en la base de datos: "))
            while opcion > 4:
                print("Tienes que elejir una opcion que este disponible")
                opcion = int(input("Elija un numero para ingresar en la base de datos: "))
            break
        except ValueError:
            print ("Debes introducir un número")

    return opcion

def menuCRUD():
    menu = '''Bien venido al menu CRUD
    1. Listar todo el contenido de la tabla material
    2. Mostrar los alumnos que tenga cierto nombre
    3. Mostrar los alumnos que hay en cierta aula
    4. Insertar datos en la tabla Material
    5. Elimina un matrial por su titulo
    6. Hacer un decuento de la tarifa a cierto niño
    7. Salir
    '''

    print(menu)

    while True:
        try:
            opcion = int(input("Elija un numero para probar la consulta: "))
            while opcion > 7:
                print("Tienes que elejir una opcion que este disponible")
                opcion = int(input("Elija un numero para probar la consulta: "))
            break
        except ValueError:
            print ("Debes introducir un número")

    return opcion

