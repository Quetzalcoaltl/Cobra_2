""" formulas para acionamentos
    oara truncar os numeros, 
    http://turing.com.br/pydoc/2.7/tutorial/floatingpoint.html"""
import math
from math import pow, sqrt
def cria_vetor(inicio, fim, espaco):
    x=[]
    while inicio <=fim:
        x.append(inicio)
        inicio +=espaco
    return x



def conjugado(m1 ,Vth ,ws, s, Rth, R2, Xth, X2):
    return m1*R2*pow(Vth,2)/(s*ws*(pow((Rth+R2/s),2) +pow((Xth+X2),2 )))
def Conj_nom(P,n):
    return 9550*P/n
def escorre_max(r2,rth,xth,x2):
    return r2/math.sqrt(rth**2+(xth+x2)**2)
def conversor_N_(n,polos):
    return 4*math.pi*60/polos
def escorregamento(x):
    return (1-x/1800)*100
def tempo_aceleracao(j,w1,w2, cam):
    return j*(w2-w1)/cam
        #w1=velocidade partida 
        #w2=velocidade chegada
        #Cam= conjugado acelaração medio
        #j= momento de inercia da massa movimentada
def tempo_frenagem(j,w2,w1,Crm,Cfm):
    return j*(w2-w1)/(Crm-Cfm)
def conj_max(m1,Vth,ws,Rth,Xth,X2):
    return m1*pow(Vth,2)/(2*ws* (Rth+sqrt(pow(Rth,2)+(pow((Xth+X2),2)) )))

"""aprender http para fazer comunicação com servidor, dica top alex"""
"""
    pot=float( input("qual a potencia do role?: "))
    rot=float( input("qual a rotacao, em rpm, do role?: "))
    s=float( input("qual a rotacao do eixo do motor: "))"""

if __name__ == "__main__":
    pass
    polos =4
    vth=266
    rth=0.133
    xth=0.497
    r2=0.1
    x2=0.2
    pot=37 
    rot=1766
    s=escorregamento(rot)
    conj=Conj_nom(pot,rot)
    ws=conversor_N_(rot,polos)
    ConMax=conj_max(3,vth,ws,rth,xth,x2)
    conj2=conjugado(3,vth,ws,s,rth,r2,xth,x2)
    S=cria_vetor(0.1,1,.1)
    #Vetor_conj=conjugado(3,vth,ws,S,rth,r2,xth,x2)
    #
    # conMax= 3*pow(vth,2)/(2*ws* (pow(rth,2)+(pow((xth+x2),2)) ))
    #conMx=3*vth**2/( 2*ws*(rth+math.sqrt(rth**2+(xth+x2)**2)) )
    max_escorre=escorre_max(r2,rth,xth,x2 )
    print("\n o conjugado fs normal eh:", conj)

    print("\n o conjugado fs normal eh:", conj2)
    print("\n o escorregamento eh:", s)
    print("\n o conjugado maximo eh:", ConMax)
    print("\n o escorregamento maximo eh:", max_escorre)
    '''print(cria_vetor(0,5,0.1))
    '''
    #print(len(Vetor_conj))
    inicio=0.1
    x=[]
    while inicio <=1:
        x.append(3*r2*pow(vth,2)/(inicio*ws*(pow((rth+r2/inicio),2) +pow((xth+x2),2 ))))
        inicio +=.01


