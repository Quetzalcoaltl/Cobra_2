#!/home/victor/anaconda3/bin/python3
import DAdosMotor
#!clear
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

    @classmethod #alterea a classe como primeiro argumento ao inves da instancia
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
''' def cria_de_string2(self,vetor_string):
            primeiro, ultimo, salario= vetor_string.split("-")
            return self(primeiro, ultimo,salario)
            não funciona porque esse metodo retorna a intancia que ainda não foi criada, e ela não
            pode ser passada como metodo de criação de objeto, é uma redundancia que impede a criação 
            antes de ser criado, não pode utilzar o metodo da instancia, mas pode usar o metodo da classe'''
        
"""    def  set_autmento(cls,quantidade):
        x=input("digite tua senha:")
        if x in cls.senhas:
            cls.aumento_salario = quantidade
            print("aumento de classe realizado")
        else:
            print("não foi possivel alterar o valor do aumento, senha incorreta")
        teste para verificar modelos de segurança e verificação de senha dentro de claase"""

    #escrever a linha acima é o msm que escrever: Empregado.aumento_salario= 1.06 
    # no fim das contas estamos alterando a classe, não a instancia, 
#emp_1.set_autmento(1.05)
    #tanto que msm chamando a função pela instancia, ainda assim podemos alterar o valor contido na classe
    #isso é interessante, pois fica uma margem gigantesca para utilização, afinal o objeto esta alterabdi, 
    # configurações referentes a claase, 
    #nas palavras do corey, vc pode rodar class methods nas intances tbm, mas isso não faz muito sentido
saida=["sair","logout", "quit", "nao quero mais","nao"]
opera=['dentro hahah']
login_funcionario=["entrar","log_func"]

x_funcionarios=[]
while opera not in saida:
    opera = input("deseja cadastrar novo funcionario(Sim/Nao):")
    if opera =="sim":
        primeiro=input("Primeiro nome do escravo: ")
        ultimo=input("ultimo nome do escravo:")
        sala=int(input("qual  mixaria: "))
        aux=Empregado(primeiro,ultimo,sala)
        x_funcionarios.append(aux)
    
print("\n foram cadastrado(s):", Empregado.numero_empregado, " funcionario(s)")
i=0
while i < len(x_funcionarios):
    print(x_funcionarios[i].email)
    print(Empregado.NomeCompleto(x_funcionarios[i]))
    #print(x_funcionarios[i]. NomeCompleto()])
    i+=1