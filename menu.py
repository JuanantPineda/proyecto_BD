import menusdef
import mariadbdef
import postgresdef

bandera = True
banderaCRUD = True

while bandera == True:
    #Me muestr el menu para la conexion de la base de datos
    opcion = menusdef.menuDB()
    banderaCRUD = True
    if opcion == 1:
        conexion = mariadbdef.conexionMariaDB()
        print()
        while banderaCRUD == True:
            #Me muestra el menudCRUD
            numero = menusdef.menuCRUD()
            print()
            # Me conecta a MariaDB
            if numero == 1:
                #Listamos el contenido de material
                mariadbdef.listarMaterial(conexion)
                print()
            elif numero == 2:
                mariadbdef.listarNombre(conexion)
                print()
            elif numero == 3:
                mariadbdef.listarAlumnos(conexion)
                print()
            elif numero == 4:
                mariadbdef.insertarDatos(conexion)
                print()
            elif numero == 5:
                mariadbdef.eliminarMaterial(conexion)
                print()
            elif numero == 6:
                mariadbdef.actualizarTarifa(conexion)
                print()
            elif numero == 7:
                #Cerramos la conexion de MariaDB
                mariadbdef.cerrarConexion(conexion)
                banderaCRUD = False
                print()
    elif opcion == 2:
        conexion2 = postgresdef.conexionPostgres()
        print()
        while banderaCRUD == True:
            numero2 = menusdef.menuCRUD()
            print()
            if numero2 == 1:
                #Listamos el contenido de material
                postgresdef.listarMaterial(conexion2)
                print()
            elif numero2 == 2:
                postgresdef.listarNombre(conexion2)
                print()
            elif numero2 == 3:
                postgresdef.listarAlumnos(conexion2)
                print()
            elif numero2 == 4:
                postgresdef.insertarDatos(conexion2)
                print()
            elif numero2 == 5:
                postgresdef.eliminarMaterial(conexion2)
                print()
            elif numero2 == 6:
                postgresdef.actualizarTarifa(conexion2)
                print()
            elif numero2 == 7:
                #Cerramos la conexion de MariaDB
                postgresdef.cerrarConexion(conexion2)
                banderaCRUD = False
                print()
    elif opcion == 4:
        bandera = False