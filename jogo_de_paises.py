# bibliotecas:
import string
import random
import math
#from dis import dis
from Base_de_paises import carrega_dados
from  Funções import *



DADOS = carrega_dados()
RAIO = 6371

quer_jogar = True
while quer_jogar:
    tentativas = 20
    distancias = []
    pais_sorteado = sorteia_pais(DADOS)
    print (pais_sorteado)
    dados_pais_sorteado = DADOS[pais_sorteado]
    capital = dados_pais_sorteado['capital']
    letras_restritas = []
    geo_pais_sorteado = dados_pais_sorteado['geo']
    coordenadas_pais_sorteado = [geo_pais_sorteado['latitude'],geo_pais_sorteado['longitude']]
    print('''
 ============================
|                            |
|  Bem-vindo ao Acerta País  |
|                            |
|         Diciplina:         |
|     Design de Software     |
 ============================ 

comandos:

dica         - Acessa o mercado de dicas 
desisto      - Desiste da rodada
inventario   - Exibe sua posição e dicas

Um país foi sorteado, tente descobrir!
''')
    ar = True
    pop = True
    cont = True
    cor_da_bandeira = []
    letra_da_capital = []
    DICAS = {}
    
    while tentativas>0:
        cor_da_band = False
        letra_cap = False

        print ('Você tem {} tentativa(s)'.format(tentativas))
        pais_palpite = input('Qual é o seu palpite?')
        
        #palpite eh pais 
        elif pais_palpite == 'dica':
            print('''
            Mercado de Dicas
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-''')
            if tentativas > 4:
                print('1. Cor da Bandeira   - custa 4 tentativas')
                cor_da_band = True
            if tentativas > 3:
                print('2. Letra da capital  - custa 3 tentativas')
                letra_cap = True
            if tentativas > 6 and ar:
                print('3. Área              - custa 6 tentativas')
            if tentativas > 5 and pop:
                print('4. População         - custa 5 tentativas')
            if tentativas > 7 and cont:
                print('5. Continente        - custa 7 tentativas')
            print('''0. Sem dica                       
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
''')
            
            dica_escolhida = int(input('Escolha sua opção [0|1|2|3|4|5]:'))
            while dica_escolhida >5  or dica_escolhida <  0:
                print ('Escolha uma opção valida!')
                dica_escolhida = int(input('Escolha sua opção [0|1|2|3|4|5]:'))
            if dica_escolhida == 1 and cor_da_band:
                custo = 4
                #cor_da_bandeira.append()
                DICAS['cor_da_bandeira'] = cor_da_bandeira
                tentativas -= custo

                print (1)
            if dica_escolhida == 2 and letra_cap:
                custo = 3
                letra_sorteada = (sorteia_letra(capital,letras_restritas))
                letra_da_capital.append(letra_sorteada)
                letras_restritas.append(letra_sorteada)
                DICAS['letra_da_capital'] = letra_da_capital
                tentativas-=custo
    
            if dica_escolhida == 3 and ar and tentativas > 6:
                custo = 6
                DICAS['area'] = dados_pais_sorteado['area']
                tentativas -= custo
                ar = False
            if dica_escolhida == 4 and pop and tentativas > 5:
                custo = 5
                tentativas -= custo
                DICAS['populacao'] = dados_pais_sorteado['populacao']
                pop = False
                print (4)
            if dica_escolhida == 5 and cont and tentativas > 7:
                custo = 7
                DICAS['continente'] = dados_pais_sorteado['continente']
                tentativas -= custo
                cont = False
                print (5)

        else:
            print('país desconhecido')
        # distancias,dicas e tentativas
            
    quer_jogar = False
