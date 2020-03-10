#criando meu primeiro jogo em python 2
#cirando uma tela
# usando turtle mod
#/usr/bin/python
#!coding=utf-8
import turtle
import os
import math
import threading
import time
from turtle import listen

#criar tela

wn = turtle.Screen() #cria a tela e chama de wn
#wn.screensize(700,700)
wn.bgcolor("yellow") # definindo cor do background
wn.title("space invaders") #titulo

#desenhar as fronteiras do meu role
cane_front= turtle.Turtle()
cane_front.speed(0) #velocidade desenho da linha dos limites 
cane_front.color("white") 
cane_front.penup() #por default a caneta inicia no meio da tela, isso serve para desencostar a caneta da tela
cane_front.setposition(-270,-270)
cane_front.pendown()
cane_front.pensize(3) #tamanho tela

for size in range(4):
    cane_front.fd(540)
    cane_front.lt(90)

cane_front.hideturtle

#criando o jogador 1 
jog1= turtle.Turtle()
jog1.speed(0) #velocidade desenho da linha dos limites 
jog1.color("green") 
jog1.penup() #por default a caneta inicia no meio da tela, isso 
jog1.shape("turtle") 
jog1.setposition(0,-250)
jog1.shapesize(10,10)

#jog1.lt(90) gira o objeto 90 graus, todavia
jog1.setheading(90) #orientacao inicial do personagem

#movimentacao do personagem

vel_jog1=10

#movimentacao esquerda e direita
'''
 def move_esquerda(): 
 	xis = jog1.xcor() #okay, aqui pegamos a componente xcor de jog1 e atribuo o valor atual a x
 			#x = x - vel_jog1 #atribuo menos a velocidade do jogador para a posicao e o novo valor eh atribuido a x, modo arcaico de se 				fazer// funcao objeto.xcor retorna a posicao em x do objeto
 	
 	#xis -= vel_jog1 #subtraio vel_jog1 de x
 	jog1.setx(xis-vel_jog1) # funcao posiciona o objeto(jog1) no eixo x na posicao xis
 
 def move_direita(): #movimentar objeti para a direita
	xis = jog1.xcor() 
	
	xis += vel_jog1 
	jog1.setx(xis) 

 #movimentacao vertical
 def move_frente(): #movimentar objeti para a direita
  	yis = jog1.ycor() 
	
	yis += vel_jog1 
	jog1.sety(yis) 

 def move_tras(): #movimentar objeti para a direita
	yis = jog1.ycor() 
	
	yis -= vel_jog1 
	jog1.sety(yis)


 jog1.setheading(90)

		criando sistema de bordas convencional:
 ----------------------------------------
 def move_esquerda():
	xis = jog1.xcor() #okay, aqui pegamos a componente xcor de jog1 e atribuo o valor atual a x
			#x = x - vel_jog1 #atribuo menos a velocidade do jogador para a posicao e o novo valor eh atribuido a x, modo arcaico de 				se fazer// funcao objeto.xcor retorna a posicao em x do objeto
	#xis -= vel_jog1 #subtraio vel_jog1 de x
	if xis <= -240:	jog1.setx(-240)
	else:	jog1.setx(xis-vel_jog1) # funcao posiciona o objeto(jog1) no eixo x na posicao xis

 def move_direita(): #movimentar objeti para a direita
	xis = jog1.xcor() 
	xis += vel_jog1 
	if xis >= 240:	jog1.setx(240)
	else:	jog1.setx(xis) 
 #movimentacao vertical
 def move_frente(): #movimentar objeti para a direita
	yis = jog1.ycor() 
	yis += vel_jog1 
	if yis >= 240:	jog1.sety(240)
	else:	jog1.sety(yis) 
 
 def move_tras(): #movimentar objeti para a direita
	yis = jog1.ycor() 
	yis -= vel_jog1 
	if yis <= -240:	jog1.sety(-240)	
	else: jog1.sety(yis)
 
 -------------------------------------------
		sistema de bordas alterado:		
 def move_esquerda():
	if jog1.xcor() > -250:	jog1.setx(jog1.xcor()-vel_jog1)  # esquerda
 def move_direita():
	if jog1.xcor() < 250:	jog1.setx(jog1.xcor()+vel_jog1)  # direita
 #movimentacao vertical
 def move_frente():
	if jog1.ycor() < 250:	jog1.sety(jog1.ycor()+vel_jog1)  # frente
 def move_tras():
	if jog1.ycor() > -250:	jog1.sety(jog1.ycor()-vel_jog1)  # tras


 def gira_esquerda():	jog1.setheading(jog1.heading()+vel_jog1)  #esquerda
 def gira_direita():     jog1.setheading(jog1.heading()-vel_jog1)  # direita

 #movimentacao geral sem bordas
 def move():     
	jog1.sety(jog1.ycor()+ (math.sin(jog1.heading()*0.01745329)*vel_jog1) )  # eixo y
 #def move_x():    
	jog1.setx(jog1.xcor()+ (math.cos(jog1.heading()*0.01745329)*vel_jog1) )  # eixo x

 #---------------------------

 movimentacao geral com bordas

 def gira_esquerda():	jog1.setheading(jog1.heading()+vel_jog1)  #esquerda
 def gira_direita():     jog1.setheading(jog1.heading()-vel_jog1)  # direita

 def move():    
	if math.fabs(jog1.xcor()) < 250:jog1.setx(jog1.xcor()+ (math.cos(jog1.heading()*0.01745329)*vel_jog1) )  # eixo x
	if math.fabs(jog1.ycor()) < 250:jog1.sety(jog1.ycor()+ (math.sin(jog1.heading()*0.01745329)*vel_jog1) )  # eixo y

 '''
 #------------------------MODO CONVENCIONAL-------------------
'''
 def gira_esquerda():	jog1.setheading(jog1.heading()+vel_jog1)  #esquerda
 def gira_direita():     jog1.setheading(jog1.heading()-vel_jog1)  # direita

 #movimentacao geral sem bordas
 def move():
        x= jog1.ycor()+ (math.sin(jog1.heading()*0.01745329)*vel_jog1)     
	if math.fabs(x)<250:	jog1.sety(x)  # eixo y
	y= jog1.xcor()+ (math.cos(jog1.heading()*0.01745329)*vel_jog1)
	if math.fabs(y)<250:	jog1.setx(y)  # eixo x


 #criando as ligacoes entre as teclas e objetos
 turtle.listen()
 turtle.onkey(gira_esquerda, "a")
 turtle.onkey(gira_direita, "d")
 turtle.onkey(move, "w")
'''
#-----------------------UTILIZANDO THREADS PARA MOVIMENTO SIMUNTANEO
#turtle.listen()
listen()

def gira_esquerda():	jog1.setheading(jog1.heading()+vel_jog1)  #esquerda
def gira_direita():     jog1.setheading(jog1.heading()-vel_jog1)  # direita

#movimentacao geral sem bordas
def move():
	x= jog1.ycor()+ (math.sin(jog1.heading()*0.01745329)*vel_jog1)     
	if math.fabs(x)<250:jog1.sety(x)  #eixo y
	y= jog1.xcor()+ (math.cos(jog1.heading()*0.01745329)*vel_jog1)
	if math.fabs(y)<250:jog1.setx(y)  #eixo x

def ehcolisao(t1,t2):
	if ((t1.ycor()-t2.ycor())**2 + (t1.xcor()-t2.xcor())**2)**0.5 <15:
		return True
	else:
		return False
#criando as ligacoes entre as teclas e objetos
 
''' modo classico de movimentacao
	turtle.onkey(move, "Up")
	turtle.onkey(gira_esquerda, "Left")
	turtle.onkey(gira_direita, "Right")'''
################################# movimento alterado

turtle.onkey(move, "Up")
turtle.onkey(gira_esquerda, "Left")
turtle.onkey(gira_direita, "Right")

#turtlr.onkey( , "a")
#turtle.onkey(move_x, "Up")
#criando inimigo:

inimigo= turtle.Turtle()
inimigo.speed(0) #velocidade desenho da linha dos limites 
inimigo.color("red") 
inimigo.penup() #por default a caneta inicia no meio da tela, isso 
inimigo.shape("circle") 
inimigo.setposition(-200,250)

vel_inimigo= 2
#main game loop


while True:
	#move inimigo
	inimigo.setx(inimigo.xcor()+vel_inimigo)
	if inimigo.xcor() > 250 :
		vel_inimigo *= -1
		inimigo.sety(inimigo.ycor()-4)
	elif inimigo.xcor() < -250:
		vel_inimigo *= -1
		inimigo.sety(inimigo.ycor()-4)
	if ehcolisao(jog1, inimigo) == True:
		print ("Game over!!!")
		exit()
	
 




















delay =raw_input("press enter")

