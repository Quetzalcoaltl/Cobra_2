#criando meu primeiro jogo em python 2
#cirando uma tela
# usando turtle mod

import turtle
import os
import math

#criar tela

wn = turtle.Screen() #cria a tela e chama de wn
#wn.screensize(700,700)
wn.bgcolor("black") # definindo cor do backgroun
wn.title("space invaders") #titulo

#desenhar as fronteiras do meu role
cane_front= turtle.Turtle()
cane_front.speed(0) #velocidade desenho da linha dos limites 
cane_front.color("white") 
cane_front.penup() #por default a caneta inicia no meio da tela, isso serve para retirar
cane_front.setposition(-50,-50)
cane_front.pendown()
cane_front.pensize(3) #tamanho tela
forma_geometrica=int(input("digite a quantidade de lados da sua forma geometrica:"))
#print"forma_geometrica", forma_geometrica
ld=int(100*math.sqrt(2)*math.sin(3.14159265/forma_geometrica))
for size in range(forma_geometrica):
    cane_front.fd(ld)
    cane_front.lt(int(360/forma_geometrica))
cane_front.hideturtle

delay =raw_input("press enter")
