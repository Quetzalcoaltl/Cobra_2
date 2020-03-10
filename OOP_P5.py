'''aula 4 corey Schafer,Python OOP Tutorial 4: Inheritance - Creating Subclasses
https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

    
'''

import DAdosMotor
class Empregado:    
    
    aumento_salario= 1.04
    numero_empregado=0
    senhas = ["pi31415","alfa","beta","dudu3493","mortadela123","pao13"]
   
    def __init__(self, primeiro_nome, ultimo_nome, pagamento): 
        self.primeiro_nome= primeiro_nome
        self.ultimo_nome= ultimo_nome
        self.pagamento=pagamento
        self.email=primeiro_nome+'.'+ultimo_nome+"@empresa.com"
        Empregado.numero_empregado +=1 
  
    def NomeCompleto(self):
        return ("{} {} ".format(self.primeiro_nome, self.ultimo_nome))
    #operar um aumento na classe
   
    def AplicaAumento(self):    
        self.pagamento=int(self.pagamento*self.aumento_salario)   

emp_1=Empregado("Jonas", "Souza", 10000)
emp_2=Empregado("Marcel", "Schunteberg", 12000)
import datetime
minha_data=datetime.date(2019,3,30)
print(Empregado.dia_servico(minha_data))

Empregado.set_autmento(1.06) 