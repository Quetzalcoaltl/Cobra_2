import DAdosMotor
from DAdosMotor import conjugado
import flask
import turtle
#print('conjugado para motor de 20kW e 1700RPM eh', DAdosMotor.Conj_nom(20,1700))
#print('tempo de aceleração do motor eh', DAdosMotor.tempo_aceleracao(j,w1,w2,cam)

wn = turtle.Screen() #cria a tela e chama de wn.screensize(700,700)
wn.bgcolor("black") # definindo cor do background
wn.title("space grafico") #titulo
polos =4
vth=266
rth=0.133
xth=0.497
r2=0.1
x2=0.2
pot=37 
rot=1766
ws=DAdosMotor.conversor_N_(rot,polos)
ConMax=DAdosMotor.conj_max(3,vth,ws,rth,xth,x2)
#conj2=DAdosMotor.conjugado(3,vth,ws,s,rth,r2,xth,x2)

cane_front = turtle.Turtle()
cane_front.speed(0) #velocidade desenho da linha dos limites 
cane_front.color("white") 
cane_front.penup() #por default a caneta inicia no meio da tela, isso serve para desencostar a caneta da tela
cane_front.setposition(-270,-270)
cane_front.pendown()
cane_front.pensize(3) #tamanho tela
x1=-270
y1=-270

for size in range(2):
    cane_front.fd(600)
    cane_front.setposition(x1,y1)
    cane_front.lt(90)
#cane_front.hideturtle
cane_front.lt(180)
inicio=0
esp=.001
inicio1=1
x=[]
#S=DAdosMotor.cria_vetor(inicio,1,esp)
S=DAdosMotor.cria_vetor(esp,1,esp)
con_mx=0
while inicio1 >=esp:
    #print(conj2)
    a=conjugado(3,vth,ws,inicio1,rth,r2,xth,x2)
    x.append(a)
    #x.append(conjugado(3,vth,ws,inicio1,rth,r2,xth,x2))
    #x.append(3*r2*pow(vth,2)/(inicio*ws*(pow((rth+r2/inicio),2) +pow((xth+x2),2 ))))
    #print(3*r2*pow(vth,2)/(inicio*ws*(pow((rth+r2/inicio),2) +pow((xth+x2),2 ))))
    if a>=con_mx: con_mx=a
    inicio1 -=esp

print('quantidade de dados',len(x))
print('escorregamento',len(S))
print("conjugado maximo aqui eh:",con_mx)
print("conjugado maximo medido eh", ConMax)
print("não confio", DAdosMotor.conj_max(3,vth,ws,rth,xth,x2))
tamanho_vetor=len(x)
cane_front.pendown()
cane_front.setposition(x1,y1)
for size in range(tamanho_vetor):
    x1=-270+S[size]*600
    y1=-270+x[size]/2
    #cane_front.setposition(x1+S[size]*600, y1+x[size-len(x)]*.5 )
    cane_front.setposition(x1, y1 )


delay =input("press enter")
