import menusdef
import mariadbdef

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
            elif numero == 4:
                mariadbdef.insertarDatos(conexion)
            elif numero == 7:
                #Creeamos la conexion de MariaDB
                mariadbdef.cerrarConexion(conexion)
                banderaCRUD = False
                print()
    elif opcion == 4:
        bandera = False