import sys
import MySQLdb

def conexionMariaDB():
    try:
        db = MySQLdb.connect("localhost","pineda","pineda","proyecto" )
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)
    print("Conexión correcta.")
    
    return db

def cerrarConexion(db):
    print("Se ha cerrado la conexion")
    db.close()

#Listar el titulo de todos los materiales de la tabla materiales

def listarMaterial(db):
    sql="select Titulo from material"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        if cursor.execute(sql) > 0:
            registros = cursor.fetchall()
            print("El contenido de la tabla material son los siguientes:")
            print("Nombre Material:")
            for registro in registros:
                print("-",registro[0])
            print("Número de registros seleccionados:", cursor.rowcount)
        else:
             print("No hay registros")
    except:
        print("Error en la consulta")

#Listar el nombre de los alumnos que se pide por pantalla de la tabla alumnos
        
def listarNombre(db):

    cad= input("Introduzca el nombre del alumno: ")

    sql=(f"select Nombre,Apellidos,DNI from ninios where nombre = '{cad}'")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        if cursor.execute(sql) > 0:
            registros = cursor.fetchall()
            print("El contenido de la tabla ninios son los siguientes:")
            print(("{:<30}{:<30}{:<30}".format("Nombre","Apellidos","DNI")))
            for registro in registros:
                print("{:<30}{:<30}{:<30}".format(registro[0],registro[1],registro[2]))
        else:
            print("No hay registros")

    except:
        print("Error en la consulta")