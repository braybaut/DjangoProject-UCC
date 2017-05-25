from funtions	import articulo,client,empeno,empenoarticulo
#articulo("iphone6",2)
#DATE="2017-11-28"
#empeno(DATE,1,3)
#empenoarticulo(200000,1,3)
#articulo("celular",2)


NOMBRE="andres"
APELLIDO="bautista"
DOCUMENTO="1032486499"
NOMBREARTICULO="motoz"
PRECIO="1800000"
FECHAVENCIMIENTO="2018-02-15"
TIPOARTICULO="1"
USUARIO="1"

## Insert data to client table and return the ID
IDCLIENT=client(NOMBRE,APELLIDO,DOCUMENTO)

IDEMPENO=empeno(FECHAVENCIMIENTO,IDCLIENT,USUARIO)
IDARTICULO=articulo(NOMBREARTICULO,TIPOARTICULO)

empenoarticulo(PRECIO,IDEMPENO,IDARTICULO)