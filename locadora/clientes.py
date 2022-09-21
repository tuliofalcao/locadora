clientes = []
locados = []
carro = []
locacao = {}
valor = 4
total = 0

class Cliente:
    
    def __init__(self,nomeCliente,cpfCliente):
        
        self.nomeCliente = nomeCliente
        self.cpfCliente = cpfCliente
    
    def getNomeCliente(self):
        return self.nomeCliente
    
    def getCpfCliente(self):
        return self.cpfCliente
    
    def setNomeCliente(self,value):
        self.nomeCliente = value
    
    def setCpfCliente(self,value):
        self.cpfCliente = value
        
    def locar():
        pass