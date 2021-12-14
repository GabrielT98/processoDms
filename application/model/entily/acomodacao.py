class Acomodacao():
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__cidade = None
        self.__tipo =None
        self.__tvCabo =None
        self.__preco = None
        self.__avaliacao =None
        self.__wifi = None
    def setId(self,id: int):
        self.__id = id

    def setNome(self,nome: str):
        self.__nome = nome

    def setCidade(self,cidade:str):
        self.__cidade = cidade

    def setTipo(self,tipo:str):
        self.__tipo = tipo

    def setTvCabo(self,tv: bool):
        self.__tvCabo = tv

    def setPreco(self,preco:float):
        self.__preco = preco

    def setAvaliacao(self,avali:str):
        self.__avaliacao = avali

    def setWifi(self,wifi:str):
        self.__wifi = wifi

    def getId(self):
        return self.__id
    def getNome(self):
        return self.__nome
    def getCiade(self):
        return self.__cidade
    def getTipo(self):
        return self.__tipo
    def getTv(self):
        return self.__tvCabo
    def getAvaliacao(self):
        return self.__avaliacao
    def getWifi(self):
        return self.__wifi