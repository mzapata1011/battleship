import random
#TODO: insertar barcos usando raton y teclado
#TODO: arreglar la indexacion al insertar a tablero
#TODO: terminar barcos_aleatorios basandose en añade barco
#TODO: quitar metodos superfluos


class Tablero():
    "Modeliza un tablero"
    def __init__(self) -> None:
        self.tablero=[]
        self.Tamaño=None
        "Inicializa el tablero"
    def __init__(self,tamaño:int, value:str)->None:
        "Inicializa un tablero vacio con el valor de vacio del juego"
        self.Tamaño=tamaño
        self.tablero=[value]*tamaño
    def print_tablero(self)->None:
        " Usaba para hacer pruebas"
        print(self.tablero)
    def inserta_ficha(self, index:int, value:int)->None:
        " pone una ficha dado su indice"
        self.tablero[index]= value
    
class flota(Tablero):
    " Modeliza los barcos de cada equipo y las acciones que pueden hacer"
    def __init__(self)->None:
        "Inicializa la flota en el tablero"
        self.tablero=[]
        self.Tamaño=None
    def __init__(self,tamaño:int, value: str)->None:
        "Inicializa dando valor al vacio y al tamaño del tablero"
        self.Tamaño=tamaño
        self.tablero=[value]*tamaño
    ships={
        "Portaviones": 5,
        "Buque": 4,
        "submarino" : 3,
        "acorazado" : 3,
        "Destructor": 2,
        "destructor1": 2,
        "lancha": 1
        }

    def Barcos_aleatorios(self)->None:
        "Asigna una posicio aleatoria a los barcos de la flota"
        barcos=list(self.ships.keys())
        for i in range(0,len(barcos)-1):
            aux=0
            while aux>=0:
                posicion_inicial=random.randint(0,99)
                dir=random.randint(0,3)

    def verificar_barco_direccion(self,longitud_barco:int,casilla_inicial: int,direccion:str)-> int :
        """Verifica que la posicion del barco sea valida
        devuelve -1 si no es valido devuelve la casilla incial si valido
        El tablero de juego va de 1 a 100 => cambiar indexacion"""
        desfase=self.direccion(direccion)
        casilla_inicial-=1
        casilla_final=casilla_inicial+desfase*longitud_barco
        if casilla_inicial==0:
            return -1
        if not (int(casilla_inicial/10)==int(casilla_final/10)) or (casilla_final-casilla_inicial)%10==0:
            return -1
        
        i=0
        while i<longitud_barco:
            if self.tablero[casilla_inicial+desfase*i]!="Water":
                return -1
            i+=1

        casilla_inicial+=1
        casilla_final+=1
        return casilla_inicial
    
    def verificar_barco(self,casilla_inicial:int, casilla_final:int)->int:
        """verifica que un barco se pueda situar dada las posiciones del barco
        si no se puede devolvera -1
        Asumo que casilla_final>casilla inicial"""
        if casilla_inicial>100 or casilla_inicial<0 or casilla_final>100 or casilla_final<0:
            return -1
        else:
            if casilla_final-casilla_inicial<10:
                return self.verificar_barco_direccion(casilla_final-casilla_inicial,casilla_inicial,"Derecha")
            else:
                return self.verificar_barco_direccion(int(casilla_final-casilla_final)/10,casilla_inicial,"Abajo")
        
    def añade_barco(self, barco:str)->None:
        """hace la verificacion acorde y añade el barco"""
        valido= False
        casilla=0
        direccion=""

        while not valido:

            casilla_inicial=int(input("en que casilla quieres el "+ barco+"?"))
            direccion=input("En que direccion? ") #Derecha, Arriba, Abajo,Izquierda
            casilla=self.verificar_barco_direccion(self.ships[barco],casilla_inicial,direccion)

            if casilla>-1: valido=True
            else: print("casilla invalida, intenta de nuevo ")
        self.insertar_barco(barco,casilla,direccion)
    def añade_barcos(self)->None:
        """hace la verificacion acorde y añade el barco"""

        barcos=list(self.ships.keys())
        for i in range(len(barcos)):
            """llama a los 5 barcos"""
            self.añade_barco(barcos[i])
            self.print_tablero()
        


        
    def insertar_barco(self,barco:str,casilla_inicial:int,casilla_final:int)->None :
        """Inserta el barco en el tablero usando insertar fichas"""

        print(casilla_final-casilla_inicial)
        if casilla_final-casilla_inicial<10:
            desfase=1
        else:
            desfase=10
        for i in range(0,self.ships[barco]): 
            self.inserta_ficha((casilla_inicial+(i)*desfase)-1,barco)

    def insertar_barco(self,barco:str,casilla_inicial:int,direccion:str)-> None:
        """Inserta el barco en el tablero dando una posicion y una direccion"""
        desfase=self.direccion(direccion)
        casilla_inicial-=1
        casilla_final=casilla_inicial+desfase*self.ships[barco]
        for i in range(0, self.ships[barco]):
            print(" en "+ str(casilla_inicial+i)+ " va "+ barco)
            self.inserta_ficha((casilla_inicial+i*desfase),barco)

    def direccion(self,direccion:str)->int:
        """Dada una direccion devuelve el desfase a tomar en cuenta en l tablero"""
        direccion=direccion.lower()
        if direccion=="derecha":
            return 1

        elif direccion=="izquierda":
            return -1

        elif direccion=="abajo":
            "abajo"
            return 10

        elif direccion=="arriba":
            "arriba"
            return -10  
        



    

if __name__=="__main__":
    Bt=flota(100,"Water")
    Bt.añade_barcos()
    Bt.print_tablero()
    # print(Bt.verificar_barco_direccion(5,0,"Derecha"))
    # # Bt.insertar_barco("Portaviones",99,"Derecha")
    # Bt.insertar_barco("Portaviones",0,"Derecha")
    # print(Bt.verificar_barco_direccion(5,0,"abajo"))
    # Bt.insertar_barco("Buque",11,"Derecha")
    # Bt.insertar_barco("submarino",21,"Derecha")
    # Bt.insertar_barco("acorazado",31,"Derecha")
    # Bt.insertar_barco("Destructor",41,"Derecha")
    # Bt.insertar_barco("destructor1",51,"Derecha")
    # Bt.insertar_barco("lancha",61,"Derecha")
    # Bt.print_tablero()

    