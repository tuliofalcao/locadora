livros = []

class Livro:
    
    def __init__(self,autor,titulo):
        
        self.autor = autor
        self.titulo = titulo
        
    def getAutor(self):
        return self.autor
    
    def getTitulo(self):
        return self.titulo
    
    def setAutor(self,value):
        self.autor = value
        
    def setTitulo(self,value):
        self.titulo = value
    
