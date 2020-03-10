#criando meu primeiro jogo em python 2
#cirando uma tela
# usando turtle mod
#/usr/bin/python
#!coding=utf-8
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
cane_front.penup() #por default a caneta inicia no meio da tela, isso serve para desencostar a caneta da tela
cane_front.setposition(-270,-270)
cane_front.pendown()
cane_front.pensize(3) #tamanho tela

for size in range(4):
    cane_front.fd(540)
    cane_front.lt(90)

cane_front.hideturtle

#criando o jogador  
jog1= turtle.Turtle()
jog1.speed(0) #velocidade desenho da linha dos limites 
jog1.color("blue") 
jog1.penup() #por default a caneta inicia no meio da tela, isso 
jog1.shape("triangle") 
jog1.setposition(0,-250)

#jog1.lt(90) gira o objeto 90 graus, todavia
jog1.setheading(90) #orientacao inicial do personagem

#movimentacao do personagem

vel_jog1=10



'''
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

'''
#criando inimigo:

inimigo= turtle.Turtle()
inimigo.speed(0) #velocidade desenho da linha dos limites 
inimigo.color("red") 
inimigo.penup() #por default a caneta inicia no meio da tela, isso 
inimigo.shape("circle") 
inimigo.setposition(-200,250)

vel_inimigo= 2
#### criar varios inimigos, primeiro selecionar o numero de inimigos
num_inimigos = 5
### criar uma lista vazia de inimigos




#criar municao do jogador
bala= turtle.Turtle()
bala.speed(0) #velocidade desenho da linha dos limites 
bala.color("yellow") 
bala.penup() #por default a caneta inicia no meio da tela, isso 
bala.shape("triangle")
bala.setheading(90)
bala.shapesize(.2,.9) #nova funcao, diminui pela metade as caracteristicas do objeto  
#bala.setposition(-200,250)
bala.hideturtle()
vel_bala=20
#Definicao do estado da bala(pronta ou disparando)
estado_bala="pronto"

#movimentacao da bala
''' movimentacao do projetil, autoral, problemas
def move_bala():
	bala.showturtle();
	bala.setposition(jog1.xcor(),jog1.ycor())
	while bala.ycor()<250:
		bala.sety(bala.ycor()+vel_bala)
	bala.hideturtle()
'''
def move_bala():
	global estado_bala #definindo como global, para que se altere o valor dentro e fora da funcao
	if estado_bala == "pronto":
		estado_bala="disparando"
		bala.setposition(jog1.xcor(),jog1.ycor()+10)
		bala.showturtle()


#ffuncao para conferir distnacia entre inimigo e bala
def ehcolisao(t1,t2):
	if ((t1.ycor()-t2.ycor())**2 + (t1.xcor()-t2.xcor())**2)**0.5 <15:
		return True
	else:
		return False
#movimentacao esquerda e direita
def move_esquerda():
	if jog1.xcor() > -250:	jog1.setx(jog1.xcor()-vel_jog1)  # esquerda
def move_direita():
	if jog1.xcor() < 250:	jog1.setx(jog1.xcor()+vel_jog1)  # direita
#movimentacao vertical
def move_frente():
	if jog1.ycor() < 250:	jog1.sety(jog1.ycor()+vel_jog1)  # frente
def move_tras():
	if jog1.ycor() > -250:	jog1.sety(jog1.ycor()-vel_jog1)  # tras

#criando as ligacoes entre as teclas e objetos
turtle.listen()
turtle.onkey(move_esquerda, "Left")
turtle.onkey(move_direita, "Right")
turtle.onkey(move_frente, "Up")
turtle.onkey(move_tras, "Down")

turtle.onkey(move_bala, "a")

#main game loop


while True:
	#move inimigo
	inimigo.setx(inimigo.xcor()+vel_inimigo)
	if inimigo.xcor() > 250 :
		vel_inimigo *= -1
		inimigo.sety(inimigo.ycor()-20)
	if inimigo.xcor() < -250:
		vel_inimigo *= -1
		inimigo.sety(inimigo.ycor()-20)
###########    moviemntacao bala
	if estado_bala == "disparando" :	
		bala.sety(bala.ycor()+vel_bala)	#movimentacao bala, 

	if bala.ycor() > 250 :	
		estado_bala = "pronto"
		bala.hideturtle() #esconder bala, apos a movimentacao
###########    reacao projetil e objeto
	if ehcolisao(bala, inimigo) == True:
		bala.hideturtle()
		estado_bala = "pronto"
		bala.setposition(0,-400)
		inimigo.setposition(-200,250)
##########	colisao entre jogador e inimigo
	if ehcolisao(jog1, inimigo) == True:
		print ("Game over!!!")
		exit
'''	solucao autoral para movimentaxao e choque entre projetil e inimigo
		disBalIni_tot=((inimigo.ycor()-bala.ycor())**2 + (inimigo.xcor()-bala.xcor())**2)**0.5
		if disBalIni_tot <15:	inimigo.hideturtle()
		----------------------------------------------------------------
	if bala.ycor() < 250 :	
		bala.sety(bala.ycor()+vel_bala)	#movimentacao bala, 
		estado_bala="disparando"
	if bala.ycor() >= 250 :	
		estado_bala= "pronto"
		bala.hideturtle() #esconder bala, apos a movimentacao

'''

 

















delay =input("press enter")

