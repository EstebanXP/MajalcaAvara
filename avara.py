class Edo :
    def __init__ ( self , nombre , padre , f ) :
        self . nombre = nombre
        self . padre = padre
        self . f = f


def miembro ( edo , lista ) :
    adentro = False
    posicion = -1
    indice =0
    for nodo in lista :
        if nodo . nombre == edo :
            adentro = True
            posicion = indice
            break
        else :
            indice = indice +1
    return adentro , posicion

def expandir ( edo , meta , proble , dlr , Abiertos , Cerrados ) :
    hijos = proble [ edo . nombre ]
    for hijo in hijos :
        mC , _ = miembro ( hijo , Cerrados )
        mA , _ = miembro ( hijo , Abiertos )
        if not mC and not mA :
            Abiertos . append ( Edo ( hijo , edo . nombre , dlr [ hijo ][ meta ])
    )
    return Abiertos

def siguiente ( Abiertos ) :
    fmejor =100
    mejor = None
    posicion = -1
    indice =0
    for nodo in Abiertos :
        if nodo .f < fmejor :
            mejor = nodo
            fmejor = nodo . f
            posicion = indice
        indice = indice +1
    del Abiertos [ posicion ]
    return Abiertos , mejor


def avara ( ini , meta , proble , dlr ) :
    Abiertos =[ Edo ( ini , ini , dlr [ ini ][ meta ]) ]
    Cerrados =[]
    listo = False
    while not listo :
        Abiertos , actual = siguiente ( Abiertos )
        if actual . nombre == meta :
            listo = True
            Cerrados . append ( actual )
        else :
            Cerrados . append ( actual )
            Abiertos = expandir ( actual , meta , proble , dlr , Abiertos ,
    Cerrados )
    return Cerrados


def getCamino ( ini , Cerrados ) :
    resp =[]
    listo = False
    actual = Cerrados [ -1]. nombre
    while not listo :
        if actual == ini :
            listo = True
            resp . insert (0 , actual )
        else :
            for nodo in Cerrados :
                if nodo . nombre == actual :
                    resp . insert (0 , actual )
                    actual = nodo . padre
                    break
    return resp


def main ( ini , meta ) :
    proble ={ 
        'A':[ 'B','C','D'] ,
        'B':[ 'A','C','E'] ,
        'C':[ 'A','B','D','E','G'] ,
        'D':[ 'A','C','F','G'] ,
        'E':[ 'B','C','F','G'] ,
        'F':[ 'D','E','G'],
        'G':['C','D','E','F']
        }

    dlr ={ 
        'A':{ 'A':0 , 'B':5 , 'C':8 , 'D':7 , 'E':13 , 'F':32,'G':18} ,
        'B':{ 'A':5 , 'B':0 , 'C':9 , 'D':14, 'E':8 , 'F':35,'G':19} ,
        'C':{ 'A':8 , 'B':9 , 'C':0 , 'D':6 , 'E':7 , 'F':26,'G':8} ,
        'D':{ 'A':7 , 'B':14 , 'C':6 , 'D':0 , 'E':16 , 'F':27,'G':12} ,
        'E':{ 'A':13, 'B':8 , 'C':7 , 'D':16 , 'E':0 , 'F':35,'G':15} ,
        'F':{ 'A':32, 'B':35 , 'C':26 , 'D':27 , 'E':35 , 'F':0,'G':15},
        'G':{ 'A':18,'B':19,'C':8,'D':12,'E':15,'F':15,'G':0}
        }
    cerrados = avara ( ini , meta , proble , dlr )
    camino = getCamino ( ini , cerrados )
    print ('la solucion segun la busqueda avara es:')
    print ( camino )

if __name__ == '__main__':
    n1=input("Ingresa el caracter de inicio: ")
    n2=input("ingresa el caracter de final: ")
    main (n1,n2)