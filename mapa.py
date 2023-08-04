from pyray import *
from raylib import *
"""#TODO: metodo que dibuje un mapa a partir de la clase tablero"""

class Mapa:
    # rectangle_width=int(min(get_screen_height(),get_screen_width())/12)
    state=0
    def __init__(self,height: int, width:int) -> None:
        init_window(960, 960, "Hello")
        self.rectangle_width=int(min(get_screen_height(),get_screen_width())/12)
        state=0
    def mapa_inicial(self)->None:
        """Dibuja el mapa al inicio del juego"""
        map_position_x,map_position_y=self.rectangle_width,self.rectangle_width
        for i in range (10):
            for j in range (10):
                draw_rectangle(map_position_x+self.rectangle_width*j,map_position_y+i*self.rectangle_width,self.rectangle_width,self.rectangle_width,BLUE)
                draw_rectangle_lines(map_position_x+self.rectangle_width*j,map_position_y+self.rectangle_width*i,self.rectangle_width,self.rectangle_width,RED)

    def dibuja_disparo(self,casilla: int, resultado:str)->None:
        """Dibuja el disparo en la casilla dependiendo del resultado
        el tablero va de 0 a 99"""
        shoot_position_x=(int(casilla%10)+1)*self.rectangle_width
        shoot_position_y=(int(casilla/10)+1)*self.rectangle_width

        if resultado!="water":
            draw_rectangle(shoot_position_x,shoot_position_y,self.rectangle_width,self.rectangle_width,RED)
        if resultado=="barco":
            draw_rectangle(shoot_position_x,shoot_position_y,self.rectangle_width,self.rectangle_width,GRAY)
        
    def dibuja_barco(self,largo_barco:int,casilla:int, direccion:str)->None:
        """"Dibuja el barco en el mapa dado una direccion y una casilla
        el manejo de errores se hace en la clase tablero"""
        # position_x=(int(casilla%10)+1)*self.rectangle_width
        # position_y=(int(casilla/10)+1)*self.rectangle_width
        # draw_rectangle(position_x,position_y,self.rectangle_width,self.rectangle_width,GRAY)
        for i in range(largo_barco):
            if direccion=="derecha":
                self.dibuja_disparo(casilla+i,"barco")
            else:
                self.dibuja_disparo(casilla+i*10,"barco")

if __name__=="__main__":
    mapa=Mapa(960,960)
    # state=0
    while not window_should_close():
        if(is_key_pressed(KEY_SPACE)):
            mapa.state=1
        if(is_key_pressed(KEY_R)):
            mapa.state=2
        # if(is_key_pressed(KEY_R)):
        

        begin_drawing()
        # clear_background(RAYWHITE)
        if mapa.state==0:
            mapa.mapa_inicial()
        elif mapa.state==1:
            mapa.dibuja_barco(3,10,"derecha")
            mapa.dibuja_barco(4,45,"abajo")
            "dibujar los barcos aleatoriamente"
        elif mapa.state==2:
            "dibuja los disparos"
            # mapa_inicial()
            mapa.dibuja_disparo(0,"boom")
            mapa.dibuja_disparo(33,"boom")
            mapa.dibuja_disparo(60,"boom")
            mapa.dibuja_disparo(99,"boom")
            mapa.dibuja_disparo(100,"boom")
            mapa.dibuja_disparo(1,"boom")
        elif mapa.state==3:
            "nada"

    # framesCounter=0
    # letterCount=0
    # alpha= 1.0 # Useful for fading

    # set_target_fps(60)




        # draw_rectangle(map_position_x,map_position_y,40,40,BLUE)
        # # map_position_x+=40
        # draw_rectangle(map_position_x+40,map_position_y,40,40,BLUE)
        # # map_position_x+=40
        # draw_rectangle(map_position_x+80,map_position_y,40,40,BLUE)
        # map_position_x+=40
        end_drawing()
    close_window()



            

