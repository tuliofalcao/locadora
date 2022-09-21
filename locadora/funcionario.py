funcionarios = []

class Funcionario:
    
    def __init__(self,nome,sobrenome,login,senha):
        
        self.nomeFuncionario = nome
        self.sobrenomeFuncionario = sobrenome
        self.loginFuncionario = login
        self.senhaFuncionario = senha
        
    def getNomeFuncionario(self):
        return self.nomeFuncionario
    
    def getSobrenomeFuncionario(self):
        return self.sobrenomeFuncionario
    
    def getLoginFuncionario(self):
        return self.loginFuncionario
    
    def getSenhaFuncionario(self):
        return self.senhaFuncionario
    
    def setNomeFuncionario(self,value):
        self.nomeFuncionario = value
    
    def setSobrenomeFuncionario(self,value):
        self.sobrenomeFuncionario = value
    
    def setLoginFuncionario(self,value):
        self.loginFuncionario = value
    
    def setSenha(self,value):
        self.senhaFuncionario = value
        