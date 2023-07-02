import pygame
import random

def water(self):
    return "water"
# creo el tablero, por el momento solo contiene agua, algunos valores cambiaran en barcos dependiendo de como pongan los barcos 
def mapa(): # agregar numeros y letras
    pygame.draw.rect(screen,(255,0,0,0),(0,0,500,500),5)
    pygame.display.flip()
# pygame.event.wait()
    cuad=[0,0,50,50]
    for i in range (0,10):
        cuad[0]=0
        for j in range(0,10):
            pygame.draw.rect(screen,(255,0,0,0),tuple(cuad),2)
            cuad[0] +=50
        cuad[1]+=50
    pygame.display.flip()
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render('GeeksForGeeks', True, (0,0,0), (255,255,255))
    # textRect = text.get_rect()
    # textRect.center=(0,100)
    # blit(text, textRect)
    pygame.display.flip()

def barcos(ships): #asigna los barcos dependiendo de la entrada manual del usuario
    barcos=list(ships.keys())
    for i in range (0,7):
        #comprobar que las posicioes son correctas
        aux=0
        # print(str(i)+"º barco")
        while aux<=0:
            # print("Hola")
            posIni=int(input("posicion inicia barco"))
            dir=int(input("direccion 0= derecha 1= arriba 2= izquierda 3= abajo")) ## modificar para poder poner direccioes a izquierda o abajo
            (posIni,posFin)=Pfinal(posIni,dir,ships,i)
            aux= position(posIni,posFin,ships.get(barcos[i])) #si no es valido da -1 si es valido da 1
        # print("ciao")
    for i in range (99):## ver una forma menos costosa (sin bucle) de hacer esto
        if not tablero[i]=="water":
            y=int(i/10) *50
            x=i%10 *50
            a= pygame.draw.rect(screen,(120,120,120),(x,y,50,50),0) 
            pygame.display.flip()
def barcosAleatorios(ships):
    #asigna los barcos aleatoriamente
    barcos=list(ships.keys())
    for i in range (0,7):
        #comprobar que las posicioes son correctas
        aux=0
        while aux<=0:
            posIni=random.randint(0,99)
            dir=random.randint(0,1)
            (posIni,posFin)=Pfinal(posIni,dir,ships,i)
            aux= position(posIni,posFin,ships.get(barcos[i])) #si no es valido da -1 si es valido da 1
            
        # print(barcos[i])
        positions(posIni,posFin,ships.get(barcos[i]),barcos[i])


    for i in range (99):## ver una forma menos costosa (sin bucle) de hacer esto 
        if not tablero[i]=="water":
            y=int(i/10) *50
            x=i%10 *50
            a= pygame.draw.rect(screen,(120,120,120),(x,y,50,50),0)
    pygame.display.flip()


def Pfinal(posIni,dir,ships,i):
    barcos=list(ships.keys())

    aux=1
    if dir==0: #si esta de lado la posicion sera posicion inicial mas largo del barco
        if ships.get(barcos[i])+posIni%10>9:
            aux=-1
           # print("izquierda")
    elif dir==1:
        if ships.get(barcos[i])+ int(posIni/10)>9:
            aux=-10
           # print("arriba")
        else:
            aux=10
           # print("abajo")
    else :
        print("unexpeted error")
    posFin=posIni+ aux*ships.get(barcos[i])

    if posIni>posFin:
        aux=posFin
        posFin=posIni
        posIni=aux
    return (posIni,posFin)

def position(posIni,posFin,largo):# le das posicion y verifica que sea una posicion valida. Si es valida lo rellena en el tablero, de no serlo devolvera una nueva posicion
    k=0
    while k<largo:
        if posIni-posFin<10:
            if tablero[posIni+k]!="water":
                return -1
        else:
            if tablero[posIni+k*10]!="water":
                return -1
        k+=1
        return 1

def positions(posIni,posFin,largo,barco): 
## rellena el mapa con los barcos
    aux=0
    #print("Pf= "+str(posFin))
    #print("Pi= "+str(posIni))
    #print(posIni-posFin)
    if posFin-posIni>=10:
        aux=10
    else:
        aux=1
    for i in range (largo):
            #print("estamos : "+ str(posIni))
            tablero[posIni]=barco
            posIni+=aux

def shoot(posDisparo,ships):
    barcos=list(ships.keys())
    #print(tablero[posDisparo])
    if tablero[posDisparo]=="water":
        print("disparo fallado")
        tablero[posDisparo]="Fallo"
        y=int(posDisparo/10) *50
        x=posDisparo%10 *50
        a= pygame.draw.rect(screen,(255,255,255),(x,y,50,50),0)
        pygame.display.flip()
        return 1
    elif tablero[posDisparo]=="Fallo":
        print("Try again")
        return -1
    elif tablero[posDisparo]=="Boom":
        print("ya le diste bro")
        return -1
    else:
        ships[tablero[posDisparo]]-=1 # le quita una vida al barco
        print(" le quedan "+str(ships[tablero[posDisparo]])+" vidas")
        y=int(posDisparo/10) *50
        x=posDisparo%10 *50
        a= pygame.draw.rect(screen,(255,0,0),(x,y,50,50),0)
        pygame.display.flip()
        if  ships[tablero[posDisparo]]==0:
            print("murio")
            return 100
        else:
            tablero[posDisparo]="Boom"
            return 1       


def disparo(ships):
    a=0
    while a!=1:
        posDisparo=int(input("Donde disparas?"))
        a=shoot(posDisparo,ships)
    return
    
def shootAleatorio(ships):
    a=0
    while a!=1:
        posDisparo=random.randint(0,99)
        a=shoot(posDisparo,ships)
    return
def superShoot(ships):
    a=0
    while a!=1:
        posDisparo=random.randint(0,99)
        print("disparo en "+ str(posDisparo))
        a=shoot(posDisparo,ships)
    aux=1
    k=0
    pos=posDisparo
    if tablero[posDisparo]!="Fallo":
        x=0
        print("Voy con tod bruja")
        while x<5: #a!=100: 
            a=0
            print("intento numero "+ str(x))  
            if posDisparo%10==9 and k==0:
                aux=-1
                k+=1
            if posDisparo/10==9 and k==2:
                aux==-10
                k+=1
            if posDisparo&10==0 and k==1:
                k+=1
                aux=10
            while a!=1:
                print("aux= "+ str(aux))
                posDisparo+=aux
                print("disparo en "+ str(posDisparo))
                a=shoot(posDisparo,ships) 
            if tablero[posDisparo]=="Fallo": # si falla un disparo
                k+=1
                print("k = "+ str(k))
                posDisparo=pos # se recupera la posicion de disparo original
                # pos-=aux*x #posicion de disparo original es igual a la actual menos x veces se sumo aux
                if k==1:
                    print("voy a la izquierda")
                    aux=-1
                elif k==2:
                    print("voy abajo")
                    aux=10
                elif k==3:
                    print("voy arriba")
                    aux=-10
            x+=1

    return    
        #     posDisparo+=1
        #     a=shoot(posDisparo,ships)
        # else: 
        #     posDisparo-=1
        #     a=shoot(posDisparo,ships)

        # if tablero[posDisparo]!="water":
        #     if posDisparo%10<9:
        #         posDisparo+=1
        #         a=shoot(posDisparo,ships)
        # el
        #     posDisparo-=1
        #     a=shoot(posDisparo,ships)
        



pygame.init()
screen= pygame.display.set_mode((750,700))
numeros= range(100)
tablero= list(map(water,numeros))   
ships={
    "Portaviones": 5,
    "Buque": 4,
    "submarino" : 3,
    "acorazado" : 3,
    "Destructor": 2,
    "destructor1": 2,
    "lancha": 1
}

pygame.display.set_caption("Battleship")
screen.fill((0,0,255))
pygame.display.flip()

done= False

mapa()
# barcos(ships)
barcosAleatorios(ships)
# print(tablero)
# disparo(ships)
# for i in range (100):
#         if not tablero[i]=="water":
#             y=int(i/10) *50
#             x=i%10 *50
#             a= pygame.draw.rect(screen,(120,120,120),(x,y,50,50),0)

# print(tablero[99])
# shootAleatorio(ships)
for i in range (7):
   superShoot(ships)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

