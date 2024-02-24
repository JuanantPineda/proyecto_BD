import funciones

banderaCRUD = True

while banderaCRUD == True:
    #Me muestra el menu para la conexion de la base de datos
    conexion = funciones.conexionPostgres()
    numero = funciones.menuCRUD()
    print()
    if numero == 1:
        #Listamos el contenido de material
        funciones.listarMaterialPostgres(conexion)
        print()
    elif numero == 2:
        funciones.listarNombrePostgres(conexion)
        print()
    elif numero == 3:
        funciones.listarAlumnosPostgres(conexion)
        print()
    elif numero == 4:
        funciones.insertarDatos(conexion)
        print()
    elif numero == 5:
        funciones.eliminarMaterial(conexion)
        print()
    elif numero == 6:
        funciones.actualizarTarifa(conexion)
        print()
    elif numero == 7:
        #Cerramos la conexion de MariaDB
        funciones.cerrarConexion(conexion)
        banderaCRUD = False