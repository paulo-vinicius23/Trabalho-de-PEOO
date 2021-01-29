from RPG_Ficha import ficha
from random import randint
class guerreiro(ficha): # Classe Descendente da Abstrata
    def status(self): # Atributos
        self.vida = 200
        self.mana = 160
        self.arma = 'Espada e Escudo'
    def habilidade(self): # Poderes dos Jogadores
        self.poder,self.dano,self.man,self.mda = [],[],[],[]
        self.poder.extend(('Golpear' ,'Escudada', 'Investida', 'Levantar Escudo', 'Raiva Interior'))
        self.dano.extend((25, 15, 60, 0, 0))
        self.man.extend((0, 0, 40, 20, 20))
        self.mda.extend((60, 80, 70, 75, 75))
        self.levantar_escudo,self.staks_le=0,0
        self.raiva_interior,self.staks_ri=0,0
    def mostrar_informaçoes(self): # Prints de Habilidades
        ficha.mostrar_informaçoes(self)
        print('1-|{}\t\t|{}\t|{}\t|'.format(self.poder[0], self.dano[0], self.man[0]))
        print('2-|{}\t\t|{}\t|{}\t|'.format(self.poder[1], self.dano[1], self.man[1]))
        print('3-|{}\t\t|{}\t|{}\t|'.format(self.poder[2], self.dano[2], self.man[2]))
        print('4-|{}\t|{}\t|{}\t|'.format(self.poder[3], self.dano[3], self.man[3]))
        print('5-|{}\t|{}\t|{}\t|'.format(self.poder[4], self.dano[4], self.man[4]))
        print('')
    def mostrar_habilidade(self):
        print('-'*80)
        print(f'1 - {self.poder[0]}: Golpeia Um Alvo Com Sua Espada\n')
        print(f'2 - {self.poder[1]}: Acerta o Alvo Com Seu Escudo\n')
        print(f'3 - {self.poder[2]}: Vai Com Toda Sua Força Para Cima do Alvo\n')
        print(f'4 - {self.poder[3]}: Aumenta a Proteção do Usuário\n')
        print(f'5 - {self.poder[4]}: Aumenta o Poder do Usuário')
        print('-'*80, '\n')
    def ação(self,players,n_habilidade,alvo): # Métodos de Ataque
        if (self.mana >= self.man[n_habilidade]):
            saving_thrown=randint(1,101)
            self.mana-=self.man[n_habilidade]
            print(f'\nMana atual de {self.nome}: {self.mana}')
            if (self.poder[n_habilidade]=='Raiva Interior' and self.mda[n_habilidade]>=saving_thrown):
                if (self.staks_ri<5):
                    print(f'\n{self.nome} Diz: Ninguém Pode Conter Minha Raiva!')
                    print(f'Habilidade {self.poder[n_habilidade]} Ativada\nDano Almentado Em 10%')
                    self.raiva_interior+=0.1
                    self.staks_ri+=1
                    print(f'Número de Staks: {self.staks_ri}\n(Staks Máximos: 5)\n')
                else:
                    print('\nNúmero de Staks Máximo Atingido\n')
                return
            if (self.poder[n_habilidade]=='Levantar Escudo' and self.mda[n_habilidade]>=saving_thrown):
                if (self.staks_le<5):
                    print(f'\n{self.nome} Diz: Armadura Reforçada!')
                    print(f'Habilidade {self.poder[n_habilidade]} Ativada\nDefesa Almentada Em 10%')
                    self.levantar_escudo+=0.1
                    self.staks_le+=1
                    print(f'Número de Staks: {self.staks_le}\n(Staks Máximos: 5)\n')
                else:
                    print('\nNúmero de Staks Máximo Atingido\n')
                return
            if (self.mda[n_habilidade] >= saving_thrown and players[alvo].nome != self.nome):
                print(f"{self.nome} atacou {players[alvo].nome} com {self.poder[n_habilidade]}")
                if(players[alvo].classe == "guerreiro"):
                    print("\nHabilidade especial do guerreiro ativada : Carcaça de Ferro")
                    print(f"{players[alvo].nome} Diz: Isso É Tudo Que Você Tem?")
                    print('Dano Reduzido Em 10 Pontos\n')
                    players[alvo].vida-=(self.dano[n_habilidade]+int(self.dano[n_habilidade]*self.raiva_interior)-int(self.dano[n_habilidade]*players[alvo].levantar_escudo)-10)
                elif(players[alvo].classe == "mago" and players[alvo].barreira_de_gelo == True):
                    print("\nBarreira de gelo ativada\nDano reduzido em 100%\n")
                    players[alvo].barreira_de_gelo = False
                else:
                    players[alvo].vida-=self.dano[n_habilidade]+int(self.dano[n_habilidade]*self.raiva_interior)
                print(f"\nVida atual de {players[alvo].nome}: {players[alvo].vida}\n")
                return 
            else:
                print(f"\n{self.nome} Errou!\n")
                if (players[alvo].classe == "arqueiro"):
                    print("\nHabilidade especial do arqueiro ativada : Tiro de Tocaia")
                    print(f"{players[alvo].nome} Diz: Vou Caçar Você") 
                    print(f'{self.nome} Diz: Ha! Inútil\n')
                    print(f"\nvida atual de {self.nome}: {self.vida}\n")
                    return
        else:
            print('\nMana Insuficiente\n')
            return