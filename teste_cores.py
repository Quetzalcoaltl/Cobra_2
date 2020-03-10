import DAdosMotor
import flask
import turtle
import csv

wn = turtle.Screen() #cria a tela e chama de wn.screensize(700,700)
cor_fundo=(0,0,1)
wn.bgcolor(cor_fundo)
# definindo cor do background
wn.title("grafico merda") #titulo
turtle.listen()
turtle.onkey(sobe_r, "Up")
print("\n",cor_fundo[0])

def sobe_r():
    if cor_fundo[0]<=1:
        a=cor_fundo[0]+.01
        cor_fundo[1]=b
        cor_fundo[2]=c
        cor_fundo=(a,b,c)
        wn.bgcolor(cor_fundo)
    


delay=("Aperte Enter:")