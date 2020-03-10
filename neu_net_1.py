"""video aula sobre criação de redes neurais
 link: https://www.youtube.com/watch?v=kft1AJ9WVDk&t=502s
 a filosofia eh a seguinte:
 1- criamos um vetor com msm numero de pesos das entradas, por exmplo se as entradas necessitam 6 digitps, ciramos um vetor aleatorio com 6 digitos, não importa quantos exemplos diferentes de entradas 
 2 - multiplicamos o peso aleatoio com os valores das entradas e jogamos o peso na sigmoide para descobrir o output
 3 - calculamos o erro, subtraindo o valor gerado no output da sigmoide comm a saida conhecida
"""
import numpy as np
#import math
from numpy import exp, array, random, dot
treino_entrada = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
saida_treino = array([[0,1,1,0]]).T
random.seed(1)#aqui ele usa a random seed para que tenhamos valores esecificos ṕara os primeiros testes, isso para termos um desenvolvimento em ambiente controlado
peso_sinapse = (2*np.random.random((3,2))-1) #maneira de se criar um vetor com valores aleatorios de zero a um

def sigmoid(x):
	return 1/(1+exp(-x))

def derivada_sigmoid(x):
	return x*(1-x)

print("Peso aleatorio das sinapses: ")
print(peso_sinapse)

for iteracao in range(5000):
	camada_entrada = treino_entrada
	
	saida=sigmoid(np.dot(camada_entrada , peso_sinapse))#multiplica a linha de cada entrada vezes o peso e ja joga na sigmoid, para ver o resultado
	erro = saida_treino -saida
	ajuste = erro*derivada_sigmoid(saida)
	peso_sinapse += np.dot(camada_entrada.T,ajuste) 



print ("saida das sinapses pos treino: ")
print(peso_sinapse)

print ("saida pos treino: ")
print(saida)
