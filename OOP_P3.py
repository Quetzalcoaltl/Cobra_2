""" 
  aula 2 de orientação ao objeto,
  Professor Corey Schafer 
  Tema Aula: Python OOP Tutorial 2: Class Variables
  https://www.youtube.com/watch?v=BJ-VvGyQxho
 """

class Empregado:    
    
    aumento_salario= 1.04
    numero_empregado=0
    def __init__(self, primeiro_nome, ultimo_nome, pagamento): 
        self.primeiro_nome= primeiro_nome
        self.ultimo_nome= ultimo_nome
        self.pagamento=pagamento
        self.email=primeiro_nome+'.'+ultimo_nome+"@empresa.com"

        Empregado.numero_empregado +=1  #essa conta foi adicionada aqui porque toda vez que um objeto
            # "funcionario" for criado __init_ roda, então podemos manter o controle de quantos foram
            #  criados

  
    def NomeCompleto(self):
        return ("{} {} ".format(self.primeiro_nome, self.ultimo_nome))
    #operar um aumento na classe
    def AplicaAumento(self):
        #self.pagamento=int( self.pagamento*Empregado.aumento_salario)  
        self.pagamento=int(self.pagamento*self.aumento_salario)    


"""operar dentro da classe com self é util quando a informaçãoa  ser manipulada é importante ao objeto,
      self.variavel_intancia
 apesar disso, quando precisamos de uma variavel de controle para a classe, por exemplo ṕara contar quantas
 vezes a classe foi chamada, então utilizamos a nomeclatura:
      classe.variavel_instancia
 """

emp_1=Empregado("Jonas", "Souza", 10000)
emp_2=Empregado("Marcel", "Schunteberg", 12000)

#print("\n",emp_1.__dict__,"\n")
    #notação para exibir detalhes intrisecos ao objeto, é importante notar que a variavel aumento salario
    # não é exibida, isso porque ela é relativa a classe Empregado, não ao objeto, entretanto, caso eu realize
    # uma alteração nessa variavel, aumenta salario essa ira ser mostrada quando esse comando acima for executado
    # isso porque a auteração foi relativa ao objeto, a variavel da classe Empregado continua a msm, 
    #    

"""
print("\n o email de ", emp_1.primeiro_nome,"eh", emp_1.email)
 print("\n o email de ", emp_2.primeiro_nome,"eh", emp_2.email)
 print("\n", Empregado.NomeCompleto(emp_1))  
 print("\n", emp_1.NomeCompleto()  )
 """
print("\n", emp_1.pagamento)
emp_1.AplicaAumento()
print("\n", emp_1.pagamento)
"""pergunta=input("voce quer alterar o aumento? (sim/não):")
    if pergunta == "sim":
    #funcionario=input("qual funcionario (sim/não):")
    inovo=float(input("qual o aumento :" ))
    emp_1.pagamento=emp_1.pagamento/emp_1.aumento_salario
    emp_1.aumento_salario=inovo
    emp_1.AplicaAumento()
    print("\n", emp_1.pagamento)
    """
print("\n foram cadastrado(s):", Empregado.numero_empregado, " funcionario(s)")
'''
    print(emp_1.numero_empregado)
    print(emp_2.numero_empregado)'''