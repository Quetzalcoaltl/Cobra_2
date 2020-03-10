"""
implementando rede neural, 
https://www.youtube.com/watch?v=gwitf7ABtK8&index=4&list=PLxt59R_fWVzT9bDxA76AHm3ig0Gg9S3So
"""
import numpy
from numpy import exp, random
#m são os dados, w é o peso, b é o bias(passagem, verificador, entende como quiser)
def NN(m1,m2, w1, w2, b ):
    z =m1*w1 +m2*w2 + b
    return sigmoid(z)
w1=2*random.randn()-1
w2=2*random.randn()-1
b =2*random.randn()-1

def sigmoid(x):
    return 1/(1+exp(-x))


print(NN(3,1.5,w1,w2,b))
