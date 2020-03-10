import turtle

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


for size in range(4):
    cane_front.fd(540)
    cane_front.lt(90)
a=.4
b=2
cor="black"
p1=-200
p2=200
A= turtle.Turtle()
A.speed(0) #velocidade desenho da linha dos limites 
A.color(cor) 
A.penup() #por default a caneta inicia no meio da tela, isso 
A.shape("square")
A.shapesize(a,b) 
A.setposition(p1,p2-5)

B= turtle.Turtle()
B.speed(0) #velocidade desenho da linha dos limites 
B.color(cor) 
B.penup() #por default a caneta inicia no meio da tela, isso 
B.shape("square")
B.shapesize(b,a) 
B.setposition(p1+20,p2-25)

C= turtle.Turtle()
C.speed(0) #velocidade desenho da linha dos limites 
C.color(cor) 
C.penup() #por default a caneta inicia no meio da tela, isso 
C.shape("square")
C.shapesize(b,a) 
C.setposition(p1+20,p2-70)

D= turtle.Turtle()
D.speed(0) #velocidade desenho da linha dos limites 
D.color(cor) 
D.penup() #por default a caneta inicia no meio da tela, isso 
D.shape("square")
D.shapesize(a,b) 
D.setposition(p1,p2-90)

E= turtle.Turtle()
E.speed(0) #velocidade desenho da linha dos limites 
E.color(cor) 
E.penup() #por default a caneta inicia no meio da tela, isso 
E.shape("square")
E.shapesize(b,a) 
E.setposition(p1-20,p2-70)

F= turtle.Turtle()
F.speed(0) #velocidade desenho da linha dos limites 
F.color(cor) 
F.penup() #por default a caneta inicia no meio da tela, isso 
F.shape("square")
F.shapesize(b,a) 
F.setposition(p1-20,p2-25)
#jog1.setheading(90) #orientacao inicial do personagem

G= turtle.Turtle()
G.speed(0) #velocidade desenho da linha dos limites 
G.color(cor) 
G.penup() #por default a caneta inicia no meio da tela, isso 
G.shape("square")
G.shapesize(a,b) 
G.setposition(p1,p2-51)
cor1="red"
'''
A.color(cor1)
B.color(cor1)
C.color(cor1)
D.color(cor1)
E.color(cor1)
F.color(cor1)
G.color(cor1)'''
while True:
    n=int(input("digite o numero \n" ))
    if n == 1:
        A.color(cor)
        B.color(cor1)
        C.color(cor1)
        D.color(cor)
        E.color(cor)
        F.color(cor)
        G.color(cor)
    if n == 2:
        A.color(cor1)
        B.color(cor1)
        C.color(cor)
        D.color(cor1)
        E.color(cor1)
        F.color(cor)
        G.color(cor1)
    if n == 3:
        A.color(cor1)
        B.color(cor1)
        C.color(cor1)
        D.color(cor1)
        E.color(cor)
        F.color(cor)
        G.color(cor1)
    if n == 4:
        A.color(cor)
        B.color(cor1)
        C.color(cor1)
        D.color(cor)
        E.color(cor)
        F.color(cor1)
        G.color(cor1)
    if n == 5:
        A.color(cor1)
        B.color(cor)
        C.color(cor1)
        D.color(cor)
        E.color(cor)
        F.color(cor1)
        G.color(cor1)
    if n == 6:
        A.color(cor1)
        B.color(cor)
        C.color(cor1)
        D.color(cor1)
        E.color(cor1)
        F.color(cor1)
        G.color(cor1)
    if n == 7:
        A.color(cor1)
        B.color(cor1)
        C.color(cor1)
        D.color(cor)
        E.color(cor)
        F.color(cor)
        G.color(cor)
    if n == 8:
        A.color(cor1)
        B.color(cor1)
        C.color(cor1)
        D.color(cor1)
        E.color(cor1)
        F.color(cor1)
        G.color(cor1)
    if n == 9:
        A.color(cor1)
        B.color(cor1)
        C.color(cor1)
        D.color(cor)
        E.color(cor)
        F.color(cor1)
        G.color(cor1)
    if n == 0:
        A.color(cor1)
        B.color(cor1)
        C.color(cor1)
        D.color(cor1)
        E.color(cor1)
        F.color(cor1)
        G.color(cor)
    
    
        
    
    





espera=raw.input('')