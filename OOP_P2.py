"""
 aula de orientação ao objeto, 
 https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=21s
 """
#entender a classe como um blueprint de empregado, sera preenchido o conceito de classe 
class Empregado:      #essa é o esqueleto, blueprint, para criar a instancia Empregado, logo a classe
    def __init__(self, primeiro_nome, ultimo_nome, pagamento): #inicializador da minha classe, 
        self.primeiro_nome= primeiro_nome   #atributo da clase 
        self.ultimo_nome= ultimo_nome
        self.pagamento=pagamento
        self.email=primeiro_nome+'.'+ultimo_nome+"@empresa.com"
    # a partir do momento que eu começo outra função dentro de uma classe, essa é uma nova instancia de 
     #da classe, logo irei criar uma aqui para representar o nome compleo do usuario, 
    def NomeCompleto(self): #metodo da classe empregado, ele gera uma informação a partir de atributos presentes na estrutra self=empregado
        return ("{} {} ".format(self.primeiro_nome, self.ultimo_nome))

"""nome_completo= self.primeiro_nome +self.ultimo_nome        esse formato aqui não da certo 
         pois eh necessario identificar a origem dos atributos do meu objeto
         print(nome_completo, )"""
"""pass""" #   deixar uma função ou classe vazia, função pass
    #uma classe é um blueprint, cada vez que eu chamo minha classe em uma variavel, por exemplo,
    #cada uma dessas variaveis seŕa um instancia da classe(instance of the class)
#os proximos serão intancias de classe
"""considerando que eu tenha mantido minha classe empregado vazia
 emp_1=Empregado()
 emp_2=Empregado()
 print(emp_1)
 print(emp_2)
 emp_1.first= "corey"
 emp_1.ultimo_nome="anderson" 
 emp_2.first="laure"
 emp_1.ultimo_nome="anderson" """
#a partir desse momento, em diante, como a blueprint ja tem por default essas configurações então só encaixa las na função empregado
 #nome=input(" Primeiro nome funcionario:")
 #ultimoNome= input("ultimo nome funcionario: ")
 #salario=int(input("digite a miseria"))
nome="Marcel"
ultimoNome= "Costa"
salario=50000

emp_1=Empregado("Jonas", "Souza", 10000)
emp_2=Empregado(nome, ultimoNome, salario)


print("\n o email de ", emp_1.primeiro_nome,"eh", emp_1.email)
print("\n o email de ", emp_2.primeiro_nome,"eh", emp_2.email)

#print("o nome completo do funcionario eh: ",emp_1.NomeCompleto())
# notar a presença dos parenteses ao chamar NomeCompleto, isso se deve em função de nome completo ser um
 #metodo, não um atributo, dessa forma precisa ser escrito corretamente
 #print("\n seu salario anual eh", emp_2.pagamento*13,"\n")
##############################
 #Como imprimir dois atributos seguidos de um objeto:
 #guardar essa forma de escrita porque é bem conveniente
 #print(" o ultimo nom de {} eh {} \n ".format(emp_1.primeiro_nome, emp_1.ultimo_nome))
"""importante:
 não importa que a minha instancia esteja do formato emp_.NomeCompleto(), a referncia do objeto sempre
 sera passada, dito isso explica a necessidade de se colocar "self" na definição da instancia quando
 se esta criando a classe"""
### forma paliativa de se obter o msm metodo:

"""print("\n",Empregado.NomeCompleto(emp_1))
   print("\n",emp_1.NomeCompleto())"""
Empregado.NomeCompleto(emp_1)   #como se chamou o metodo, mas o objeto não foi especificado,
                                    # esse precisa ser passado como argumento para que seja 
                                    # associado a self e retorne os valores correpondente dos
                                    #  objeto
emp_1.NomeCompleto()    #desse modo não eh necessario se escrever o argumento, porque ele ja entende 
                            #o objeto como "self"
            
"""a proxima aula é uma continuação direta dessa, porem para não sobrecarregar o codigo com
 muitos comentarios, decidi continuar a partir de um novo programa com o mesmo codigo, porem 
 esse novo esta sem os comentarios aqui atribuidos"""
