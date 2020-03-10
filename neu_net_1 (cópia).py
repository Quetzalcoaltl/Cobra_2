import numpy as np
import math
from numpy import exp, array, random, dot

treino_entrada = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
saida_treino = array([[0,1,1,0]]).T

random.seed(1)#aqui ele usa a random seed para que tenhamos valores esecificos ṕara os primeiros testes, isso para termos um desenvolvimento em ambiente controlado
peso_sinapse = (2*np.random.random((3,1))-1) #maneira de se criar um vetor com valores aleatorios de zero a um

"""essa forma não funciona
peso_sinapse=array([0, 0, 0])
for i in range(2):
	peso_sinapse[i,1]=random.random()-1"""


def sigmoid(x):
	return 1/(1+exp(-x))

def derivada_sigmoid(x):
	return x*(1-x)

#treino_entrada = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1] ])

print("Peso aleatorio das sinapses: ")
print(peso_sinapse)

for iteracao in range(1):
	camada_entrada = treino_entrada
	#aux=dot(treino_entrada , peso_sinapse)
	saida=sigmoid(np.dot(camada_entrada , peso_sinapse))
	#erro = saida_treino -saida
	#ajuste = erro*derivada_sigmoid(saida)
	#peso_sinapse += np.dot(camada_entrada.T,ajuste)  #argumento T serve para transpor matriz
	
"""
gambiarra para funcionar, 
for iteracao in range(1):
	#camada_entrada = treino_entrada
	aux=dot(treino_entrada , peso_sinapse)
	saida = 1/(1+exp(-aux))

print ("saida das sinapses pos treino: ")
print(peso_sinapse)
"""
print ("saida pos treino: ")
print(saida)
print(treino_entrada)