class Visitante():
    def __init__(self):
        self.__nome = None
        self.__email = None
        self.__senha = None

    def setNome(self,nome: str):
        self.__nome = nome

    def setEmail(self,email: str):
        self.__email = email

    def setSenha(self,senha:str):
        self.__senha = senha
    def getNome(self):
        return self.__nome
    def getEmail(self):
        return self.__email
    def getSenha(self):
        return self.__senha