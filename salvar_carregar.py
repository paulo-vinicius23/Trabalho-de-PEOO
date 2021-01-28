# Importando Bibliotecas
from Mago import mago
from Arqueiro import arqueiro
from Guerreiro import guerreiro
class arquivo:
    @staticmethod
    def salvar(players):# Função de Salvar
        try:
            arq=open("Save.txt",)
            inp=arq.read()
            if len(inp) != 0:
                while True:
                    try:
                        ask=int(input("Jogo Salvo Encontrado\n\n1-Sim\n2-Não\n\nDeseja Sobrescrever:\n"))
                        if (ask==1):
                            arq=open("Save.txt","w")
                            arq.close()
                            break
                        elif (ask==2):
                            return
                        else:
                            print('\nOpção Inválida\n')
                    except:
                        print('\nUse Apenas Números!\n')
            arquivo=open("Save.txt","w")
            for i in range(len(players)):
                if players[i].classe == "guerreiro":
                    arquivo.write(f"ESCUDOstaks:{players[i].staks_le}\nESCUDOpor:{players[i].levantar_escudo}\nRAIVAstaks:{players[i].staks_ri}\nRAIVApor:{players[i].raiva_interior}\n")
                arquivo.write(f"NOME:{players[i].nome}\nCLASSE:{players[i].classe}\nVIDA:{players[i].vida}\nMANA:{players[i].mana}\n\n")
            print("Jogo salvo ...\n")
        except :
            print('Arquivo "Save.txt" não encontrado ou corrompido\n')
    @staticmethod
    def carregar(jogadores, Nomes_Jog): # Função de Carregar
        test=open("Save.txt")
        info=test.read()
        if len(info)==0:
            print("\nNenhum Save Encontrado\n")
            return
        arq=open("Save.txt")
        Dados_carregados=[]
        Nomes=[]
        classes=[]
        vida=[]
        mana=[]
        staksle=[]
        staksri=[]
        por_le=[]
        por_ri=[]
        for linha in arq:
            if linha.startswith("NOME:"):
                atpos=linha.find(":")
                Nomes.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("CLASSE:"):
                atpos=linha.find(":")
                classes.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("VIDA:"):
                atpos=linha.find(":")
                vida.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("MANA:"):
                atpos=linha.find(":")
                mana.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("ESCUDOstaks:"):
                atpos=linha.find(":")
                staksle.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("ESCUDOpor:"):
                atpos=linha.find(":")
                por_le.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("RAIVAstaks:"):
                atpos=linha.find(":")
                staksri.append(linha[atpos+1:].replace("\n",""))
            elif linha.startswith("RAIVApor:"):
                atpos=linha.find(":")
                por_ri.append(linha[atpos+1:].replace("\n",""))      
        Dados_carregados.append(Nomes)                    
        Dados_carregados.append(classes)                    
        Dados_carregados.append(vida)                    
        Dados_carregados.append(mana)  
        x=Dados_carregados                  
        for i in range(len(x[0])):
            N=str(x[0][i])
            C=str(x[1][i])
            if C == "mago":
                jogadores.append(mago(N,C))
            elif C == "guerreiro":
                jogadores.append(guerreiro(N,C))
            elif C == "arqueiro":
                jogadores.append(arqueiro(N,C))
            Nomes_Jog.append(N)
            jogadores[i].status()
            jogadores[i].habilidade()
            jogadores[i].vida=int(x[2][i])
            jogadores[i].mana=int(x[3][i])
            jogadores[i].mostrar_informaçoes()
        g=0
        for u in range(len(jogadores)):
            if jogadores[u].classe=="guerreiro":
                jogadores[u].staks_le=int(staksle[g])
                jogadores[u].levantar_escudo=float(por_le[g])
                jogadores[u].staks_ri=int(staksri[g])
                jogadores[u].raiva_interior=float(por_ri[g])
                g+=1