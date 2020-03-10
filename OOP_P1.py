from abc import ABCMeta, abstractmethod

class Transacao(metaclass = ABCMeta):
    @abstractmethod
    def execute(self):
        pass
        


class SELECT(Transacao):
    def __init__(self, transacao):
        self.trans =transacao
    def execute(self):
        self.trans.SELECT()


class  INSIRA(Transacao):
    def __init__(self, transacao):
        self.trans =transacao
    def execute(self):
        self.trans.INSIRA()


class ATUALIZACAO(Transacao):
    def __init__(self, transacao):
        self.trans =transacao
    def execute(self):
        self.trans.ATUALIZACAO()

class Gerenciador_Transacao:
    def SELECT(self):
        print("realizando operação SELECAO ")
    
    def INSIRA(self):
        print("realizando operação INSIRA ")
    
    def ATUALIZACAO(self):
        print("realizando operação ATUALIZACAO ")

class Quebra_Transacao:
    def __init__(self):
        self.__fila_transacao=[]

    def chama_transacao(self, transacao):
        self.__fila_transacao.append(transacao)
        transacao.execute()

if __name__ == "__main__":
    traction= Gerenciador_Transacao()
    tr_selecao= SELECT(traction)
    tr_insercao= INSIRA(traction)
    tr_atualiza= ATUALIZACAO(traction)

    quebra=Quebra_Transacao() 
    quebra.chama_transacao(tr_selecao)
    quebra.chama_transacao(tr_insercao)
    quebra.chama_transacao(tr_insercao)
    quebra.chama_transacao(tr_selecao)
    quebra.chama_transacao(tr_atualiza)
    quebra.chama_transacao(tr_insercao)
    quebra.chama_transacao(tr_atualiza)



