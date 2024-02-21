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

def insertarDatos(db):

    titulo = input("Ingrese el titulo del materia: ")
    formato = input("Ingrese el formato del material: ")

    estadoMaterial = input("Ingrese el estado funcional del material (usado o nuevo): ").lower()
    while estadoMaterial not in ['usado', 'nuevo']:
        print("Estado funcional del material no válido. Por favor, ingrese uno de los siguientes valores: usado o nuevo")
        estadoMaterial = input("Ingrese el estado funcional del material nuevamente: ").lower()

    estadoFuncional = input("Ingrese el estado del material (bueno, excelente, inutilizable, usado o regular): ").lower()
    while estadoFuncional not in ['bueno', 'excelente', 'inutilizable', 'usado', 'regular']:
        print("Estado del material no válido. Por favor, ingrese uno de los siguientes valores: bueno, excelente, inutilizable, usado o regular")
        estadoFuncional = input("Ingrese el estado del material nuevamente: ").lower()

    comentario= input("Ingrese un comentario del material: ")

    while True:
        try:
            numEjemplares = int(input("Ingrese el numero de ejemplares que tiene ese material: "))
            while numEjemplares <= 0:
                print("Tienes que poner un numero acorde")
                numEjemplares = int("Ingrese el numero de ejemplares que tiene ese material: ")
            break
        except ValueError:
            print ("Debes introducir un número")

    tipoMaterial = input("Ingrese el tipo de material que es: ")

    cursor = db.cursor()
    sql="insert into material values ('%s','%s','%s','%s','%s',%d,'%s')" % (titulo,formato,estadoMaterial,estadoFuncional,comentario,numEjemplares,tipoMaterial)
    print (sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("No se ha ingresado ningun dato")
        db.rollback()

def eliminarMaterial(db):
    titulo = input("Ingrese el titulo a eliminar: ")

    cursor=db.cursor()
    sql=(f"delete from material where titulo = '{titulo}'")

    try:
        cursor.execute(sql)
        db.commit()
        if cursor.rowcount==0:
            print("No hay valores con ese dato")
        else:
            print("Se ha eliminado",titulo,"de la tabla material")
    except :
        print("No se ha eliminado ningun dato")
        db.rollback()

def actualizarTarifa(db):

    descuento = int(input("Ingresa el descuento para la tarifa"))
    idNinino = input("Ingrese el identificador del niño")

    sql=(f"UPDATE ninios SET Tarifa = Tarifa * ((100-{descuento}*0.01)*0.01) WHERE Id_ninio = '{idNinino}' ")
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print("Se ha actualizado correctamente los datos")
    except Exception as e:
        print("Error ", e)