"""
Segunda video aula, utilzacao da rede neural em neu_net_1.py 

https://www.youtube.com/watch?v=Py4xvZx-A1E
"""
#import math
import numpy as np
from numpy import exp, array, random, dot
#import "/home/victor/codigos/python/neu_net_1.py"
#import neu_net_1

class RedeNeural(): #criada uma classe rede neural, eh um pensador  par operar o role todo, mas sem caracteristicas, somente o metodo operante
    def __init__(self):#self definida como variavel standard, o que significa que no futuro variaveis serao utilizadas dentro e fora da rede
       # np.random.seed(1)
        self.peso_sinapse = (2*np.random.random((3,1))-1) #maneira de se criar um vetor com valores aleatorios de zero a um
    
    def sigmoid(self,x):
        return 1/(1+exp(-x))

    def derivada_sigmoid(self, x):
        return x*(1-x)
	
    def treino(self, entrada_treino, saida_treino, iteracao_treino):
        iteracao=0
        while iteracao <=iteracao_treino:
            saida=self.pensamento(entrada_treino)
            erro = saida_treino -saida
            ajuste = np.dot(entrada_treino.T, erro*self.derivada_sigmoid(saida))
            #print(iteracao)
            self.peso_sinapse +=ajuste
    
    def pensamento(self, entradas):
        entradas=entradas.astype(float)
        saida=self.sigmoid(np.dot(entradas, self.peso_sinapse))
        return saida
    
if __name__ =="__main__":
    rede_neural= RedeNeural()
    print(rede_neural.peso_sinapse)
    #criada o objeto rede neural, podemos desenvolver 
    treino_entrada= array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
    saida_treino = array([[0,1,1,0]]).T
    rede_neural.treino(treino_entrada,saida_treino,5000)
    print("peso das sinapses depois do treino: ", rede_neural.peso_sinapse)
    A=input("valor do 1 termo: ")
    B=input("valor do 2 termo: ")
    C=input("valor do 3 termo: ")
    print("nova entrada:", A, B, C)
    print("saida :")
    print( rede_neural.pensamento( (np.array([A, B, C])).T ))
