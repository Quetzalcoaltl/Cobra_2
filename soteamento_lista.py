'''
realizar sorteamento do role de maneira mais topper '''
import numpy
import plot_graf
from numpy import array
#import plot_graf
#vetor=array([7,0,8,14, 87 ,7,1,3,123 ,1234,22 ,2,43,72,7,83,94,47,26,40,55,79,25,0,13,22,53])
vetor=plot_graf.vetor
i=0
tamanho_vetor=len(vetor)
print(tamanho_vetor)
contador=0
while i < tamanho_vetor-1:
    contador+=1
    if vetor[i] > vetor[1+i]:
        aux=vetor[i]
        vetor[i]=vetor[1+i]
        vetor[1+i]=aux
        i=0
    i+=1

print(vetor)
print("quantidade de iterações", contador)
#???????????????????????????????????
# cara, como fazer isso...
# o importante pra mim é criar um sistema para parar o sistema, 
# dito isso, sabendo que o primeiro pode sera comparado com todos os itens então,
# meu contador sera zera 
# zerado, mas como evitar que o role não .
