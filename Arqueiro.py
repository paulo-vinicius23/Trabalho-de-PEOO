from RPG_Ficha import ficha
from random import randint
class arqueiro(ficha): # Classe Descendente da Abstrata
    def status(self): # Atributos
        self.vida = 280
        self.mana = 280
        self.arma = 'Arco e Flechas'
    def habilidade(self): # Poderes dos Jogadores
        self.poder = []
        self.dano = []
        self.man = []
        self.mda = []
        self.poder.extend(('Atirar' ,'Tiro em Espiral', 'Tiro Explosivo', 'Tiro Fatal','Crescente Mira Certa'))
        self.dano.extend((20, 30, 75, 60, 0))
        self.man.extend((0, 10, 20, 25, 40))
        self.mda.extend((85, 80, 75, 50, 75))
        self.crescente_mira_certa=False
    def mostrar_informaçoes(self):# Prints de Habilidades
        ficha.mostrar_informaçoes(self)
        print('1-|{}\t\t|{}\t|{}\t|'.format(self.poder[0], self.dano[0], self.man[0]))
        print('2-|{}\t|{}\t|{}\t|'.format(self.poder[1], self.dano[1], self.man[1]))
        print('3-|{}\t|{}\t|{}\t|'.format(self.poder[2], self.dano[2], self.man[2]))
        print('4-|{}\t\t|{}\t|{}\t|'.format(self.poder[3], self.dano[3], self.man[3]))
        print('5-|{}\t|{}\t|{}\t|'.format(self.poder[4], self.dano[4], self.man[4]))
        print('')
    def mostrar_habilidade(self):
        print('-'*80)
        print(f'1 - {self.poder[0]}: Atira Uma Flecha Em Um Alvo\n')
        print(f'2 - {self.poder[1]}: Atira Em Um Alvo Num Tiro Em Espiral\n')
        print(f'3 - {self.poder[2]}: Atira Uma Bomba Em Um Alvo, AVISO: Estilhaços da Bomba\n')
        print(f'4 - {self.poder[3]}: Uma Flecha Que Acerta No Ponto Fraco do Alvo\n')
        print(f'5 - {self.poder[4]}: Aumenta o Foco Fazendo Acertar o Proximo Ataque')
        print('-'*80, '\n')
    def ação(self,players,n_habilidade,alvo): # Métodos de Ataque
        if (self.mana >= self.man[n_habilidade]):
            crit=int(self.mda[n_habilidade]/4) # Resolução de Acerto Crítico
            if (self.crescente_mira_certa==True):
                saving_thrown=randint(1,50)
                self.crescente_mira_certa=False
            else:
                saving_thrown=randint(1,100)
            self.mana-=self.man[n_habilidade]
            print(f'\nMana atual de {self.nome}: {self.mana}')
            if (self.poder[n_habilidade] == 'Crescente Mira Certa' and self.mda[n_habilidade] >= saving_thrown):
                print(f'\n{self.nome} Diz: O Alvo Ta Na Mira')
                print(f'Habilidade {self.poder[n_habilidade]} Ativada\nPróximo ataque terá o acerto de 100%\n')
                self.crescente_mira_certa=True
                return
            if (self.poder[n_habilidade] == 'Tiro Explosivo' and players[alvo].nome != self.nome):
                print(f"{self.nome} atacou {players[alvo].nome} com {self.poder[n_habilidade]}")
                if(players[alvo].classe == "guerreiro"):
                    print("\nHabilidade especial do guerreiro ativada : Carcaça de Ferro")
                    print(f"{players[alvo].nome} Diz: Isso É Tudo Que Você Tem?")
                    print('Dano Reduzido Em 10 Pontos\n')
                    if (crit>=saving_thrown):
                        print('\nAcerto Crítico!\nDano Dobrado!\n')
                        players[alvo].vida-=((self.dano[n_habilidade]-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)*2)
                    else:
                        players[alvo].vida-=(self.dano[n_habilidade]-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)
                elif(players[alvo].classe == "mago" and players[alvo].barreira_de_gelo == True):
                    print("\nBarreira de gelo ativada\nDano reduzido em 100%\n")
                    players[alvo].barreira_de_gelo = False
                else:
                    if (crit>=saving_thrown):
                        print('\nAcerto Crítico!\nDano Dobrado!\n')
                        players[alvo].vida-=self.dano[n_habilidade]*2
                    else:
                        players[alvo].vida-=self.dano[n_habilidade]
                if(self.mda[n_habilidade] <= saving_thrown):
                    self.vida-=self.dano[n_habilidade]
                    print(f'{self.nome} foi atingido pelos estilhaços!')
                    print(f"\nVida atual de {self.nome}: {self.vida}")
                print(f"\nVida atual de {players[alvo].nome}: {players[alvo].vida}\n")
                return
            if(self.mda[n_habilidade] >= saving_thrown and players[alvo].nome != self.nome):
                print(f"{self.nome} atacou {players[alvo].nome} com {self.poder[n_habilidade]}")
                if(players[alvo].classe == "guerreiro"):
                    print("\nHabilidade especial do guerreiro ativada : Carcaça de Ferro")
                    print(f"{players[alvo].nome} Diz: Isso É Tudo Que Você Tem?\n")
                    print('Dano Reduzido Em 10 Pontos\n')
                    if (crit>=saving_thrown):
                        print('\nAcerto Crítico!\nDano Dobrado!\n')
                        players[alvo].vida-=((self.dano[n_habilidade]-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)*2)
                    else:
                        players[alvo].vida-=(self.dano[n_habilidade]-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)  
                elif(players[alvo].classe == "mago" and players[alvo].barreira_de_gelo == True):
                    print("\nBarreira de gelo ativada\nDano reduzido em 100%\n")
                    players[alvo].barreira_de_gelo = False
                else:
                    if (crit>=saving_thrown):
                        print('\nAcerto Crítico!\nDano Dobrado!\n')
                        players[alvo].vida-=self.dano[n_habilidade]*2
                    else:
                        players[alvo].vida-=self.dano[n_habilidade]
                print(f"\nVida atual de {players[alvo].nome}: {players[alvo].vida}\n")
                return
            else:
                print(f"\n{self.nome} Errou!\n")
                if (players[alvo].classe == "arqueiro" and players[alvo].nome != self.nome):
                    print("\nHabilidade especial do arqueiro ativada : Tiro de Tocaia")
                    print(f"{players[alvo].nome} Diz: Vou Caçar Você\n") 
                    self.vida-=10
                    print(f"\nvida atual de {self.nome}: {self.vida}\n")
                    return
        else:
            print('\nMana Insuficiente\n')
            return