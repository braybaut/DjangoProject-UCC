import MySQLdb

##  Funtion to Save client data 

def client(ARGUMENT1,ARGUMENT2,ARGUMENT3):
 
    NOMBRE=ARGUMENT1
    APELLIDO=ARGUMENT2
    DOCUMENTO=ARGUMENT3
    db = MySQLdb.connect("localhost","ucc","UCC123.","mydb" )
    cursor = db.cursor()
    cursor.execute("insert into cliente (nombre, apellido, documento) values (%s, %s, %s)",(NOMBRE, APELLIDO, DOCUMENTO))
    db.commit()
    
    cursor.execute("select id from cliente where documento = %s" % DOCUMENTO)
    results = cursor.fetchone()
    DOCUMENTID = results[0]
    db.close
    print DOCUMENTID
    return DOCUMENTID
    

#client=client("Brayan","bautista",1032486497)

## Funtion save articule data 


#### Terminar Retorno en articulo
def articulo(ARGUMENT1,ARGUMENT2):
    NArticulo=ARGUMENT1
    TArticulo=ARGUMENT2
    db = MySQLdb.connect("localhost","ucc","UCC123.","mydb" )
    cursor = db.cursor()
    cursor.execute("insert into articulo (nombre_articulo, tipo_articulo_id) values (%s, %s)",(NArticulo, TArticulo))
    db.commit()
    cursor.execute("select id from articulo where nombre_articulo = %s and tipo_articulo_id = %s",(NArticulo,TArticulo))      
    results = cursor.fetchone()
    ARTICULOID = results[0]
    db.close
    print ARTICULOID
    return ARTICULOID

 
#valor=articulo(argum1,argum2) 

## Funtion to save Empeno and return the ID 
def empeno(FVencimiento,ClienteID,UsuarioID):
    db = MySQLdb.connect("localhost","ucc","UCC123.","mydb" )
    cursor = db.cursor()
    cursor.execute("insert into empeno (fecha_vencimiento,cliente_id,usuario_id)  values (%s, %s, %s)",(FVencimiento,ClienteID,UsuarioID))
    db.commit()
    cursor.execute("select id from empeno where fecha_vencimiento = %s and cliente_id = %s and usuario_id = %s",(FVencimiento,ClienteID,UsuarioID))
    results = cursor.fetchone()
    EMPENOID = results[0]
    db.close
    print EMPENOID
    return EMPENOID


def empenoarticulo(valorarticulo,empenoID,articuloID):
    db = MySQLdb.connect("localhost","ucc","UCC123.","mydb" )
    cursor = db.cursor()
    cursor.execute("insert into empeno_articulo (valor_articulo,empeno_id,articulo_id) values (%s, %s, %s)",(valorarticulo,empenoID,articuloID))
    db.commit()
    db.close
    