# Importando Bibliotecas
from Mago import mago
from Arqueiro import arqueiro
from Guerreiro import guerreiro
from salvar_carregar import arquivo
import random
# Lista de Jogadores e Nome de Jogadores
jogadores = []
Nomes_Jog = []


print('\n|__________A Batalha Por Gaia__________|\n') # Nome do Jogo
while True:
    try:
        print('1-Novo Jogo\n2-Carregar\n3-Sair') # Menu Principal
        menu = int(input('\nDigite Uma das Opções:\n'))
        print('-'*80)
        if (menu == 1): # Criação de Novo Jog
            N_jogadores = int(input('\nDigite o Número de Jogadores:\n'))
            if (N_jogadores < 2):
                print('\nNúmero de Jogadores Insuficiente\n')
                print('-'*80)
                continue
            i = 0
            while i < N_jogadores:
                N = input('\nDigite o Nome do Jogador:\n')
                if (N not in Nomes_Jog):
                    Nomes_Jog.append(N)
                    print('\nClasses Disponíveis:\n\n-Mago\n-Arqueiro\n-Guerreiro')
                    while True:
                        C = input('\nDigite a Classe do Jogador:\n').lower()
                        if (C=='mago'):
                            jogadores.append(mago(N,C))
                            print('\nJogador Criado!')
                            jogadores[i].status()
                            jogadores[i].habilidade()
                            jogadores[i].mostrar_informaçoes()
                            i += 1
                            break
                        elif (C=='arqueiro'):
                            jogadores.append(arqueiro(N,C))
                            print('\nJogador Criado!')
                            jogadores[i].status()
                            jogadores[i].habilidade()
                            jogadores[i].mostrar_informaçoes()
                            i += 1
                            break
                        elif (C=='guerreiro'):
                            jogadores.append(guerreiro(N,C))
                            print('\nJogador Criado!')
                            jogadores[i].status()
                            jogadores[i].habilidade()
                            jogadores[i].mostrar_informaçoes()
                            i += 1
                            break
                        else:
                            print('\nClasse Invalida\n')
                else:
                    print('\nNome Já Está Sendo Utilizado\n')
            break
        elif (menu == 2): # Carregando Jogo Salvo
            arquivo.carregar(jogadores,Nomes_Jog)
            if (len(jogadores) > 1):
                print('\nCarregado Com Sucesso\n')
                break
        elif (menu == 3): # Sair do Jogo
            print('\nSaindo...\n')
            break
        else:
            print('\nOpção Inválida\n')
    except:
        print('\nOpção Inválida\n')
if (menu == 3): 
    quit()
while True:
    try:
        print('-'*80)
        print('\n|_____Menu De Jogo_____|\n') # Menu de Pré-Jogo
        print('1-Jogar\n2-Editar Personagens\n3-Deletar Personagem')
        menu = int(input('\nDigite Uma das Opções:\n'))
    except:
        print('\nOpção Inválida\n')
    if (menu == 1):
        print('\nPreparando Para O Jogo...\n') # Preparando Para o Jogo
        break
    elif (menu == 2 or menu == 3): # Opção de Editar ou Deletar Personagens 
        print ('\nJogadores:\n')
        for i in range(len(jogadores)):
            print(f'Nome: {jogadores[i].nome}\nClasse: {jogadores[i].classe}\n')
        if (menu == 2):# Menu de Editar Personagens
            while True:
                try:
                    print('-'*80)
                    edit = input('\nDigite o Nome do Jogador Que Queira Editar:\n')
                    posição = Nomes_Jog.index(edit)
                    edit = int(input('\n1-Nome\n2-Classe\n\nSelecione o Número Correspondente a Sua Edição:\n'))
                    if (edit == 1):
                        while True:
                            jogadores[posição].nome = input('\nDigite Um Novo Nome:\n')
                            if (jogadores[posição].nome not in Nomes_Jog):
                                Nomes_Jog[posição] = jogadores[posição].nome
                                print('\nNome Alterado!\n')
                                break
                            else:
                                print('\nNome Já Está Sendo Utilizado\n')
                    elif (edit == 2): 
                        while True:
                            C = input('\nDigite Uma Classe Nova:\n').lower()
                            aux1 = jogadores[posição].vida
                            aux2 = jogadores[posição].mana
                            if (C=='mago'):
                                jogadores[posição] = mago(Nomes_Jog[posição],C)
                                print('\nClasse Alterada!')
                                jogadores[posição].status()
                                jogadores[posição].vida = aux1  
                                jogadores[posição].mana = aux2 
                                jogadores[posição].habilidade()
                                jogadores[posição].mostrar_informaçoes()
                                break
                            elif (C=='arqueiro'):
                                jogadores[posição] = arqueiro(Nomes_Jog[posição],C)
                                print('\nClasse Alterada!')
                                jogadores[posição].status()
                                jogadores[posição].vida = aux1  
                                jogadores[posição].mana = aux2
                                jogadores[posição].habilidade()
                                jogadores[posição].mostrar_informaçoes()
                                break
                            elif (C=='guerreiro'):
                                jogadores[posição] = guerreiro(Nomes_Jog[posição],C)
                                print('\nClasse Alterada!')
                                jogadores[posição].status()
                                jogadores[posição].vida = aux1  
                                jogadores[posição].mana = aux2
                                jogadores[posição].habilidade()
                                jogadores[posição].mostrar_informaçoes()
                                break
                            else:
                                print('\nClasse Invalida\n')
                    break
                except:
                    print('\nErro de Inválidez\n')
        elif(menu == 3):# Menu de Deletar Personagens
            print('-'*80)
            if (len(jogadores) == 2):
                print('\nNúmero Mínimo de Jogadores Atingido\n')
            else:
                while True:
                    try:
                        edit = input('\nDigite o Nome do Jogador Que Queira Excluir:\n')
                        posição = Nomes_Jog.index(edit)
                        print(f'\nJogador {Nomes_Jog[posição]} Foi Deletado!')
                        del Nomes_Jog[posição]
                        del jogadores[posição]
                        break
                    except:
                        print('\nNome Inválido\n')


while True:
    D20 = []
    print('-'*80)
    print('\nOrdem da Rodada:\n') # Ordem Aleatória da Rodada
    for j in range(len(jogadores)):
        Dado = random.randint(1,20)
        while (Dado in D20) == True:
            if (Dado-1 == 0):
                Dado += 1
            else:
                Dado -= 1
        D20.append(Dado)
        print(f'Jogador {jogadores[j].nome} Rolou Um: {D20[j]}\n')
    iniciativa = sorted(D20,reverse=True)
    j = 0
    while j < len(iniciativa): # Menu de Batalha
        print('-'*80)
        dex = D20.index(iniciativa[j])
        arco = 0
        if (0 >= jogadores[dex].vida):
            j += 1
            if (j < len(iniciativa)):
                dex = D20.index(iniciativa[j])
            else:
                break
        print(f'Vez de {jogadores[dex].nome}')
        print(f'Vida: {jogadores[dex].vida}')
        print(f'Mana: {jogadores[dex].mana}\n')
        while True:
            try:
                jogadores[dex].mostrar_habilidade()
                habilit = int(input('Escolha o Número Correspondente a Habilidade Desejada:\n'))
                print('-'*80)
                habilit -= 1
                if(habilit > 4 or habilit < 0):
                    print('\nHabilidade Inválida\n')
                else:
                    break
            except:
                print('\nERRO 505\n')
        if (jogadores[dex].classe == 'mago' and (habilit == 2 or habilit == 4)):
            j_alvo=dex
            print(f'\nO Jogador {jogadores[dex].nome} Utilizou {jogadores[dex].poder[habilit]}')
            jogadores[dex].ação(jogadores,habilit,j_alvo)
        elif (jogadores[dex].classe == 'guerreiro' and (habilit == 3 or habilit == 4)):
            j_alvo=dex
            print(f'\nO Jogador {jogadores[dex].nome} Utilizou {jogadores[dex].poder[habilit]}')
            jogadores[dex].ação(jogadores,habilit,j_alvo)
        elif (jogadores[dex].classe == 'arqueiro' and habilit == 4):
            j_alvo=dex
            print(f'\nO Jogador {jogadores[dex].nome} Utilizou {jogadores[dex].poder[habilit]}')
            jogadores[dex].ação(jogadores,habilit,j_alvo)
        else:
            while True:
                try:
                    print('\nJogadores:\n')
                    for i in range(len(jogadores)):
                        if (jogadores[i].nome != jogadores[dex].nome and jogadores[i].vida > 0):
                            print(f'-{jogadores[i].nome}')
                    j_alvo = input('\nDigite o Nome do Alvo:\n')
                    arco = Nomes_Jog.index(j_alvo)
                    if (jogadores[arco].nome != jogadores[dex].nome and jogadores[arco].vida > 0):
                        jogadores[dex].ação(jogadores,habilit,arco)
                        break
                    else:
                        print('\nOpção Inválida\n')
                except:
                    print('\nOpção Inválida\n')
        j += 1
    i = 0
    while i < len(jogadores): # Verificando se Algum Jogador Entrou em Óbito
        if(jogadores[i].vida <= 0):
            print('-'*80)
            print(f'Jogador {jogadores[i].nome} Faleceu.')
            del jogadores[i]
            del Nomes_Jog[i]
        i += 1
    if (len(jogadores) == 1): # Verificando se ah Vencedores
        print('-'*80)
        quit(f'\nParabéns!\nTemos um vencedor\nVencedor: {jogadores[0].nome}\n')
    elif (len(jogadores) == 0):
        print('-'*80)
        quit('\nTodos os jogadores estão mortos\nNão Há Vencedores\n')
    while True: # Menu de save
        try:
            print('-'*80)
            save_op = int(input('\n1-Sim\n2-Não\n\nDeseja Salvar:\n'))
            if (save_op == 1): 
                arquivo.salvar(jogadores)
                break
            elif (save_op == 2):
                break
            else:
                print('\nOpção Inválida\n')
        except:
            print('\nUse Apenas Números!\n')