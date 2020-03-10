import numpy as np
#import math
from numpy import exp, array, random, dot
treino_entrada = array([[0,0,0,0], [0,0,0,1], [0,0,1,1], [0,1,1,1]])
saida_treino = array([[0,0,0,0],[0,0,0,1], [0,0,1,0],[0,0,1,1]])
#random.seed(1)#aqui ele usa a random seed para que tenhamos valores esecificos ṕara os primeiros testes, isso para termos um desenvolvimento em ambiente controlado
peso_sinapse = (2*np.random.random((4,4))-1) #maneira de se criar um vetor com valores aleatorios de zero a um
peso_sinapse2= (2*np.random.random((4,4))-1)

def sigmoid(x):
	return 1/(1+exp(-x))

def derivada_sigmoid(x):
	return x*(1-x)

print("Peso aleatorio das sinapses: ")
print(peso_sinapse)
'''
	for iteracao in range(50000):
	camada_entrada = treino_entrada
	
	saida=sigmoid(np.dot(camada_entrada , peso_sinapse))#multiplica a linha de cada entrada vezes o peso e ja joga na sigmoid, para ver o resultado
	erro = saida_treino -saida
	ajuste = erro*derivada_sigmoid(saida)
	peso_sinapse += np.dot(camada_entrada,ajuste) 
    
	'''

for iteracao in range(1000000):
	camada_entrada = treino_entrada.T
	camada_escondida=sigmoid(np.dot(camada_entrada , peso_sinapse))
	saida=sigmoid(np.dot(camada_escondida , peso_sinapse2))#multiplica a linha de cada entrada vezes o peso e ja joga na sigmoid, para ver o resultado
	erro = saida_treino - saida
	ajuste = erro*derivada_sigmoid(camada_escondida)
	ajuste1 = erro*derivada_sigmoid(saida)
	peso_sinapse2 += np.dot(camada_escondida,ajuste) 
	peso_sinapse += np.dot(camada_entrada,ajuste1)
    

print ("saida das sinapses pos treino: ")

print ("saida pos treino: ")
print(saida)


teste=([1,1,1,0])
print('teste?')
camada_escondida=sigmoid(np.dot(teste , peso_sinapse))
saida=sigmoid(np.dot(camada_escondida , peso_sinapse2))#multiplica a linha de cada entrada vezes o peso e ja joga na sigmoid, para ver o resultado
	
#print(sigmoid(np.dot(teste, peso_sinapse)))
print(saida)