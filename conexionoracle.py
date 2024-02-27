import funcionesoracle

banderaCRUD = True

while banderaCRUD == True:
    #Me muestra el menu para la conexion de la base de datos
    conexion = funcionesoracle.conexionOracle()
    numero = funcionesoracle.menuCRUD()
    print()
    if numero == 1:
        #Listamos el contenido de material
        funcionesoracle.listarMaterial(conexion)
        print()
    elif numero == 2:
        funcionesoracle.listarNombre(conexion)
        print()
    elif numero == 3:
        funcionesoracle.listarAlumnos(conexion)
        print()
    elif numero == 4:
        funcionesoracle.insertarDatos(conexion)
        print()
    elif numero == 5:
        funcionesoracle.eliminarMaterial(conexion)
        print()
    elif numero == 6:
        funcionesoracle.actualizarTarifa(conexion)
        print()
    elif numero == 7:
        #Cerramos la conexion de MariaDB
        funcionesoracle.cerrarConexion(conexion)
        banderaCRUD = False




