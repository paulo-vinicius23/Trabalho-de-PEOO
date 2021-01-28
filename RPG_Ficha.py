from abc import ABC 
from abc import abstractmethod 
class ficha(ABC): # Classe Abstrata
    def __init__(self, nome, classe,mana=0,vida=0,arma=None): # Construtor
        self.__nome = nome
        self.__classe = classe
        self.__vida = vida
        self.__mana = mana
        self.arma = arma
    @abstractmethod 
    def status(self):
        pass
    @abstractmethod            
    def habilidade(self):
        pass
    def mostrar_informaçoes(self): # Prints Informações
        print(f'\nNome : {self.__nome}')
        print(f'Classe: {self.__classe.capitalize()}')
        print(f'Vida : {self.__vida}')
        print(f'Mana : {self.__mana}')
        print(f'Arma : {self.arma}\n')
        print('#-|Nome:\t\t|Dano:\t|Mana:\t|')
        print('-----------------------------------------')
    @abstractmethod 
    def mostrar_habilidade(self):
        pass
    @abstractmethod
    def ação(self,players,n_habilidade,alvo):
        pass
    # Atributos de Encapsulados (linha 31-54)     
    @property
    def nome(self):
        return(self.__nome)
    @nome.setter
    def nome(self,nome):
        self.__nome=nome
    @property
    def classe(self):
        return(self.__classe)
    @classe.setter
    def classe(self,classe):
        self.__classe=classe
    @property
    def vida(self):
        return(self.__vida)
    @vida.setter
    def vida(self,vida):
        self.__vida=vida
    @property
    def mana(self):
        return(self.__mana)
    @mana.setter
    def mana(self,mana):
        self.__mana=mana