import menusdef
import mariadbdef

bandera = True
banderaCRUD = True

while bandera == True:
    #Me muestr el menu para la conexion de la base de datos
    opcion = menusdef.menuDB()
    banderaCRUD = True
    if opcion == 1:
        while banderaCRUD == True:
            conexion = mariadbdef.conexionMariaDB()
            #Me muestra el menudCRUD
            numero = menusdef.menuCRUD()
            # Me conecta a MariaDB
            if numero == 7:
                mariadbdef.cerrarConexion(conexion)
                banderaCRUD = False