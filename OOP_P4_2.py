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
    
saida=["sair","logout", "quit", "nao quero mais","nao"]
opera=['dentro hahah']
login_funcionario=["entrar","log_func"]

x_funcionarios=[]
while True:
    opera = input("o que deseja fazer? \n cadastro func - CF\n login funcionario - F\n login Admin - Admin:")
    
    if opera =="CF:
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