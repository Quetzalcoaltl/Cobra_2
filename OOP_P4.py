'''aula 3 corey Schafer, Python OOP Tutorial 3: classmethods and staticmethods
    metodos de classe e metodos estaticos
    programação orientada ao objeto
    https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
    diferença entre:
        regular metods: automamaticamente pega a instancia como primeiro argumento(self)
        class metods: passam a classe como primeiro argumento
        estatic methods: não passa nada automaticamente, eles operam como funções normais
        entretanto como são ligados  logicamente pela classe, ainda são metodos operacionais de classe,
        uma maneira simples de saber qual metodo utilizar, é observar: estou utilizando alguma variavel da
        classe(class.variavel)? se não então não é um metodo de classe, e o raciocinio é o msm para o Regular method, 
        se não estiver usando "self.variavel" então provavelmente não é um metodo regular, 
        nesse caso, quando não utiliza essas variaveis externas então provavelmente é um metodo estatico
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

    @classmethod #altera a classe como primeiro argumento ao inves da instancia
    def  set_autmento(cls,quantidade):
            cls.aumento_salario = quantidade
    
    @classmethod
    def cria_de_string(cls,vetor_string):
        primeiro, ultimo, salario= vetor_string.split("-")
        return cls(primeiro, ultimo,salario)
        #a ideia aqui foi a de criar uma maneira gerenerica para se realizar a 
        # criação de funcionarios a partir do vetor string, foi utilizado, o conceito de cls, 
        # para criar a string, pois se o metodo fosse regular ia passar a instancia e, como ela 
        # nesse ponto ainda não foi criada, é um tanto quanto impossivel fazer dessa forma, segue 
        # abaixo uma tentativa desse outro metodo 
    
    @staticmethod
    def dia_servico(dia):
        if dia.weekday()== 5 or dia.weekday()== 6:
            return False
        return True

'''
    def cria_de_string2(self,vetor_string):
            primeiro, ultimo, salario= vetor_string.split("-")
            return self(primeiro, ultimo,salario)
            não funciona porque esse metodo retorna a intancia que ainda não foi criada, e ela não
            pode ser passada como metodo de criação de objeto, é uma redundancia que impede a criação 
            antes de ser criado, não pode utilzar o metodo da instancia, mas pode usar o metodo da classe'''
"""
    def  set_autmento(cls,quantidade):
        x=input("digite tua senha:")
        if x in cls.senhas:
            cls.aumento_salario = quantidade
            print("aumento de classe realizado")
        else:
            print("não foi possivel alterar o valor do aumento, senha incorreta")
        teste para verificar modelos de segurança e verificação de senha dentro de claase"""

emp_1=Empregado("Jonas", "Souza", 10000)
emp_2=Empregado("Marcel", "Schunteberg", 12000)
import datetime
minha_data=datetime.date(2019,3,30)
print(Empregado.dia_servico(minha_data))

Empregado.set_autmento(1.06) 
    #escrever a linha acima é o msm que escrever: Empregado.aumento_salario= 1.06 
    # no fim das contas estamos alterando a classe, não a instancia, 

#emp_1.set_autmento(1.05)
    #tanto que msm chamando a função pela instancia, ainda assim podemos alterar o valor contido na classe
    #isso é interessante, pois fica uma margem gigantesca para utilização, afinal o objeto esta alterabdi, 
    # configurações referentes a claase, 
    #nas palavras do corey, vc pode rodar class methods nas intances tbm, mas isso não faz muito sentido

 #print(Empregado.aumento_salario)
 #print(emp_1.aumento_salario)
 #print(emp_2.aumento_salario)
'''    
    print("\n", emp_1.pagamento)
    print("\n", emp_2.pagamento)'''
#print("\n foram cadastrado(s):", Empregado.numero_empregado, " funcionario(s)")
 #emp_1.set_autmento(1.07)
'''
    x=input("digite tua senha:")
    #print(x*2)
    senhas = ["pi31415","alfa","beta","dudu3493"]

    while x not in senhas:
        x=input("senha errada:")

    print("configurações de admin")'''
'''
    emp_str_1="angelo-bismark-13500"
    emp_str_2="luis-markus-17500"
    emp_str_3="leandro-isurik-19500"'''

#primeiro, ultimo, salario= emp_str_1.split("-")# função split é autoesplicativa
    #novo_emp_1=Empregado(primeiro, ultimo,salario)
    #novo_emp_1=Empregado.cria_de_string(emp_str_1)
    #novo_emp_2=Empregado( emp_str_2.split('-')) ------ não funciona(infelizmente)
'''
    print(novo_emp_1.email)
    print(novo_emp_1.NomeCompleto())
    saida=["sair","logout", "quit", "nao quero mais","nao"]
    opera=['dentro hahah']
    i=0
    x_funcionarios=[]
    while opera not in saida:
        opera = input("deseja cadastrar novo funcionario(Sim/Nao):")
        if opera =="sim":
            primeiro=input("Primeiro nome do escravo: ")
            ultimo=input("ultimo nome do escravo:")
            sala=int(input("qual  mixaria: "))
            aux=Empregado(primeiro,ultimo,sala)
            x_funcionarios.append(aux)
            i+=1
    
    x=DAdosMotor.cria_vetor(0,5,1)

    x[1]=Empregado('mario','andrade',500)
    x[0]=emp_1
    print(x[1].email)
    print(x[0].email)'''
print("\n foram cadastrado(s):", Empregado.numero_empregado, " funcionario(s)")
