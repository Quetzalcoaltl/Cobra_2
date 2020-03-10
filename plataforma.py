import turtle
import os
import math
#import pymunk
from turtle import listen, onkey


""" por que um objeto se movimento, okay a força se aplica sobre ele, mas o que isso signifaca de maneira empirica?

"""
gravidade=9.8 #m/s^2 , sabendo que a força é massa x aceleração, e aceleração é v
vel_jog1=5


#criar tela


wn = turtle.Screen() #cria a tela e chama de wn
#wn.screensize(700,700)
wn.bgcolor("black") # definindo cor do background
wn.title("space invaders") #titulo

#desenhar as fronteiras do meu role
cane_front= turtle.Turtle()
cane_front.speed(0) #velocidade desenho da linha dos limites 
cane_front.color("white") 
cane_front.penup() #por default a caneta inicia no meio da tela, isso serve para desencostar a caneta da tela
cane_front.setposition(-270,-270)
cane_front.pendown()
cane_front.pensize(1) #tamanho tela
p1=0
p2=0
p3=120

for size in range(4):
    cane_front.fd(540)
    cane_front.lt(90)

#cane_front.hideturtle
#suporte
'''	suporte=turtle.Turtle()
	suporte.speed(0),
	suporte.color("white")
	suporte.penup()
	suporte.shape("triangle")
	suporte.setposition(0,-250)
	suporte.setheading(90)'''
#criando o jogador 1 
jog1= turtle.Turtle()
jog1.speed(0) #velocidade desenho da linha dos limites 
jog1.color("yellow") 
jog1.penup() #por default a caneta inicia no meio da tela, isso 
jog1.shape("square")
jog1.shapesize(.1,18) 
jog1.setposition(0,-p2)
#jog1.setheading(90) #orientacao inicial do personagem

obj_1= turtle.Turtle()
obj_1.speed(0) #velocidade desenho da linha dos limites 
obj_1.color("blue") 
obj_1.penup() #por default a caneta inicia no meio da tela, isso 
obj_1.shape("square")
obj_1.shapesize(1,1) 
obj_1.setposition(-p3,-p1)

m_p1=1

#obj_1.setheading(90) 

obj_2= turtle.Turtle()
obj_2.speed(0) #velocidade desenho da linha dos limites 
obj_2.color("green") 
obj_2.penup() #por default a caneta inicia no meio da tela, isso 
obj_2.shape("square")
obj_2.shapesize(1,1) 
obj_2.setposition(p3,-p1)
m_p2=1

#obj_2.setheading(90) 

def sp1(): 
	global m_p1
	m_p1 += 1 #vel_jog1  #soma massa de peso 1 
def dp1():
	global m_p1
	if m_p1 >0:	m_p1 -= 1 #vel_jog1  #subtrai massa de objeto 1
def sp2(): 
	global m_p2
	m_p2 +=1 #vel_jog1  #soma massa de objeto 2
def dp2():
	global m_p2
	if m_p2 >0:	m_p2 -=1 #vel_jog1  #subtrai massa de objeto 2

def gira_esquerda():
	if 	jog1.heading()<45:
		jog1.setheading(jog1.heading()+vel_jog1)  #esquerda ) 
def gira_direita():     
	if 	jog1.heading()>-45:
		jog1.setheading(jog1.heading()-vel_jog1)  # direita

#movimentacao geral sem bordas

def move():
	x= jog1.ycor()+ (math.sin(jog1.heading()*0.01745329)*vel_jog1)     
	if math.fabs(x)<250:jog1.sety(x)  #eixo y
	y= jog1.xcor()+ (math.cos(jog1.heading()*0.01745329)*vel_jog1)
	if math.fabs(y)<250:jog1.setx(y)  #eixo x
'''
turtle.listen()
turtle.onkey(move, "Up")
turtle.onkey(gira_esquerda, "Left")
turtle.onkey(gira_direita, "Right")
turtle.onkey(sp1,"q")
turtle.onkey(dp1,"w")
turtle.onkey(sp1,"e")
turtle.onkey(dp1,"r")

'''
listen()
onkey(move, "Up")
onkey(gira_esquerda, "Left")
onkey(gira_direita, "Right")
onkey(sp1,"q")
onkey(dp1,"w")
onkey(sp2,"e")
onkey(dp2,"r")



#print("o tamanho do jogador eh",jog1.stretch_wid())

while True:
	obj_2.setheading(jog1.heading())
	a=p3*math.cos(jog1.heading()*3.1415/180)
	b=p3*math.sin(jog1.heading()*3.1415/180 )-p1
	obj_2.setposition(a,b)

	obj_1.setheading(jog1.heading())
	obj_1.setposition(-a,-b)
	print("peso do objeto um eh:", m_p1)

	print("peso do objeto dois eh:", m_p2)



	'''
	aux=math.cos(jog1.heading()*0.01745329)
	obj_2.xcor(aux)
	#obj_2.xcor( 100*math.cos(jog1.heading()*0.0174532925)  ) 
	obj_2.ycor(-210+100*math.sin(jog1.heading()*0.0174532925))'''

#delay=input("aperte enter")