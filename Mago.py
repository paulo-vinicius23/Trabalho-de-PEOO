from RPG_Ficha import ficha
from random import randint
class mago(ficha): # Classe Descendente da Abstrata
    def status(self): # Atributos
        self.vida = 260
        self.mana = 300
        self.arma = 'Cajado Velho'
    def habilidade(self): # Poderes dos Jogadores
        self.poder,self.dano,self.man,self.mda = [],[],[],[]
        self.poder.extend(('Cajadada' ,'Bola de Fogo', 'Barreira de Gelo', 'Eletrocutar','Intelecto Arcano'))
        self.dano.extend((10, 70, 0, 30, 0))
        self.man.extend((0, 60, 50, 30, 0))
        self.mda.extend((85, 80, 50, 70, 60))
        self.vinculo_de_mana=False
        self.barreira_de_gelo=False
    def mostrar_informaçoes(self): # Prints de Habilidades
        ficha.mostrar_informaçoes(self)
        print('1-|{}\t\t|{}\t|{}\t|'.format(self.poder[0], self.dano[0], self.man[0]))
        print('2-|{}\t\t|{}\t|{}\t|'.format(self.poder[1], self.dano[1], self.man[1]))
        print('3-|{}\t|{}\t|{}\t|'.format(self.poder[2], self.dano[2], self.man[2]))
        print('4-|{}\t\t|{}\t|{}\t|'.format(self.poder[3], self.dano[3], self.man[3]))
        print('5-|{}\t|{}\t|{}\t|'.format(self.poder[4], self.dano[4], self.man[4]))
        print('')
    def mostrar_habilidade(self): 
        print('-'*80)
        print(f'1 - {self.poder[0]}: Da Uma Cajadada Em Um Alvo a Sua Escolha\n')
        print(f'2 - {self.poder[1]}: Lança Uma Bola de Energia Que Queima o Adiversário\n')
        print(f'3 - {self.poder[2]}: Se Cobre Em Uma Camada de Gelo Fortificado\n')
        print(f'4 - {self.poder[3]}: Solta Uma Rajada de Raios Em Cima do Alvo\n')
        print(f'5 - {self.poder[4]}: Regenera 40 Pontos de Mana')
        print('-'*80, '\n')
    def ação(self,players,n_habilidade,alvo): # Métodos de Ataque
        if (self.barreira_de_gelo == True):
            print('\nBarreira de Gelo Ativada\nImpossível Alguma Ação\nProteção de 100%\n')
            return
        if (self.mana >= self.man[n_habilidade]):
            if (self.vinculo_de_mana == True):
                self.mana-=int(self.man[n_habilidade]-(self.man[n_habilidade]*0.2))
                self.vinculo_de_mana=False
            else:
                self.mana-=self.man[n_habilidade]
            print(f'\nMana atual de {self.nome}: {self.mana}')
            crit=int(self.mda[n_habilidade]/4)
            saving_thrown=randint(1,100)
            if(self.poder[n_habilidade] == 'Intelecto Arcano' and self.mda[n_habilidade] >= saving_thrown):
                print(f'\n{self.nome} Diz: Minha Mana Se Revigora!')
                print(f'Habilidade {self.poder[n_habilidade]} Ativada\nMana Regenera Em 40 Pontos\n')
                self.mana+=40
                print(f'Sua mana atual é de: {self.mana}\n')
            elif(self.poder[n_habilidade] == 'Barreira de Gelo' and self.mda[n_habilidade] >= saving_thrown):
                print('\nBarreira de Gelo Ativada\nProteção de 100%\n')
                self.barreira_de_gelo = True
            elif(self.mda[n_habilidade] >= saving_thrown and players[alvo].nome != self.nome):
                print(f"{self.nome} atacou {players[alvo].nome} com {self.poder[n_habilidade]}")
                if (players[alvo].classe == "guerreiro"):
                    print("\nHabilidade especial do guerreiro ativada : Carcaça de Ferro")
                    print(f"{players[alvo].nome} Diz: Isso É Tudo Que Você Tem?\n")
                    print('Dano Reduzido Em 10 Pontos\n')
                    if (crit>=saving_thrown):
                        print('\nAcerto Crítico!\nDano Dobrado!\n')
                        players[alvo].vida-=((self.dano[n_habilidade]-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)*2)
                    else:    
                        players[alvo].vida-=(self.dano[n_habilidade]-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)
                elif (players[alvo].classe=='mago' and players[alvo].barreira_de_gelo == True):
                    print("\nBarreira de gelo ativada\nDano reduzido em 100%\n")
                    players[alvo].barreira_de_gelo = False
                else:
                    if (crit>=saving_thrown):
                        print('\nAcerto Crítico!\nDano Dobrado!\n')
                        players[alvo].vida-=self.dano[n_habilidade]*2
                    else:
                        players[alvo].vida-=self.dano[n_habilidade]
                print(f"\nVida atual de {players[alvo].nome}: {players[alvo].vida}\n")
            else:
                print(f"\n{self.nome} Errou!\n")
                if (players[alvo].classe == "arqueiro"):
                    print("\nHabilidade especial do arqueiro ativada : Tiro de Tocaia")
                    print(f"{players[alvo].nome} Diz: Vou Caçar Você\n") 
                    self.vida-=10
                    print(f"\nSua vida atual: {self.vida}\n")
                return
            if((randint(1,100))>=75 and self.mda[n_habilidade] >= saving_thrown):
                self.vinculo_de_mana=True
                print("\nVinculo de Mana ativado\nPróxima habilidade custará 20% menos de mana")
                print(f"{self.nome} Diz: Minha Magia Despedaçará Você!\n")
                return
        else:
            print('\nMana Insuficiente\n')
            return