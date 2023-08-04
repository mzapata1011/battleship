from tablero import *
from mapa import *
"""#TODO: conectar tablero a la clase grafica
los disparos se deben de escribir en tablero
y los barcos se deben de guardar tambien"""

if __name__=="__main__":
    Usuario=flota(100,"Water")
    computer=flota(100,"Water")
    mapa=Mapa(960,960)
    
    while not window_should_close():
        
        if(is_key_pressed(KEY_SPACE)):
            mapa.state=1
        if(is_key_pressed(KEY_R)):
            mapa.state=2
        # if(is_key_pressed(KEY_R)):
        
        begin_drawing()
        # mapa.mapa_inicial()
        if mapa.state==0:
            mapa.mapa_inicial()
        elif mapa.state==1:
            """Estado 1: dibuja los barcos"""
            mapa.dibuja_barco(5,95,"derecha")
            mapa.dibuja_barco(4,20,"abajo")
            mapa.dibuja_barco(3,3,"abajo")
            mapa.dibuja_barco(3,5,"derecha")
            mapa.dibuja_barco(2,0,"derecha")
            mapa.dibuja_barco(2,55,"abajo")
            mapa.dibuja_barco(1,79,"abajo")

        elif mapa.state==2:
            """Estado 2: dibuja los disparos"""
            # mapa_inicial()
            mapa.dibuja_disparo(0,"boom")
            mapa.dibuja_disparo(33,"boom")
            mapa.dibuja_disparo(60,"boom")
            mapa.dibuja_disparo(99,"boom")
            mapa.dibuja_disparo(100,"boom")
            mapa.dibuja_disparo(1,"boom")
        elif mapa.state==3:
            "nada"
        end_drawing()
    close_window()


