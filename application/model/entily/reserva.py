from datetime import datetime

from application.model.entily.acomodacao import Acomodacao

class Reserva():
    def __init__(self):
        self.__id = None
        self.__qtdPessoas = None
        self.__dataEntrada = None
        self.__dataSaida = None
        self.__local = None
        self.__acomodacao = None

    def setId(self,id:int):
        self.__id = id
    def setQtdPessoas(self,pessoas:int):
        self.__qtdPessoas = pessoas
    def setEntrada(self,entrada: datetime):
        self.__dataEntrada = entrada
    def setSaida(self,saida:datetime):
        self.__dataSaida = saida
    def setLocal(self,local:str):
        self.__local = local

    def setAcomodacao(self,acomodacao: Acomodacao):
        self.__acomodacao = acomodacao

    def getId(self):
        return self.__id
    def getQtdPessoas(self):
        return self.__qtdPessoas
    def getEntrada(self):
        return self.__dataEntrada
    def getSaida(self):
        return self.__dataSaida
    def getLocal(self):
        return self.__local
    def getAcomodacao(self):
        return self.__acomodacao