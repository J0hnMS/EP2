# bibliotecas:
import string
import random
import math
#from dis import dis
from Base_de_paises import carrega_dados
from  Funções import *



DADOS = carrega_dados()
RAIO = 6371

#inicia o jogo
quer_jogar = True
while quer_jogar:
    #define parametros
    tentativas = 20
    distancias = []
    ar = True
    pop = True
    cont = True
    cor_da_bandeira = []
    letra_da_capital = []
    DICAS = {}
    pais_sorteado = sorteia_pais(DADOS)
    
    #informações de pais sorteado
    dados_pais_sorteado = DADOS[pais_sorteado]
    capital = dados_pais_sorteado['capital']
    geo_pais_sorteado = dados_pais_sorteado['geo']
    coordenadas_pais_sorteado = [geo_pais_sorteado['latitude'],geo_pais_sorteado['longitude']]
    
    #tela de inicio
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
    
    #chance de palpite caso tenha tentativas
    while tentativas>0:
        #parametros locais

        
        # imprime tentatives e pergunta palpite
        print ('Você tem {} tentativa(s)'.format(tentativas))
        pais_palpite = input('Qual é o seu palpite?')
        
        #palpite é um pais valido
        if pais_palpite in DADOS:
            #calcula distancia do pais sorteado
            dados_pais_palpite = DADOS[pais_palpite]
            geo_pais_palpite = dados_pais_palpite['geo']
            coordenadas_pais_palpite = [geo_pais_palpite['latitude'],geo_pais_palpite['longitude']]
            distancia= haversine(RAIO,coordenadas_pais_sorteado[0],coordenadas_pais_sorteado[1],coordenadas_pais_palpite[0],coordenadas_pais_palpite[1])
            distancias = adiciona_em_ordem(pais_palpite,distancia,distancias)
            tentativas -= 1 
            print('Distâncias:')
            for dist in distancias:
                print('{:.0f} km -> {}'.format(dist[1],dist[0]))
            print('Dicas:')
            for dica,value in DICAS.items():
                if dica == 'cor_da_bandeira':
                    print('   - Cores da bandeira: {}'.format(value))
                if dica == 'letra_da_capital':
                    print('   - Letras da capital: {}'.format(value))
                if dica == 'area':
                    print('   - Área:{} km2'.format(value))
                if dica == 'populacao':
                    print('   - População: {} habitantes'.format(value))
                if dica == 'continente':
                    print('   - Continente: {}'.format(value))
                    
        #palpite foi pedir dica
        elif pais_palpite == 'dica':
            #print mercado de dicas, caso nao tenha tentativas suficiente dica nao é imprimida
            print('''
            Mercado de Dicas
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-''')
            if tentativas > 4:
                print('1. Cor da Bandeira   - custa 4 tentativas')
            if tentativas > 3:
                print('2. Letra da capital  - custa 3 tentativas')
            if tentativas > 6 and ar:
                print('3. Área              - custa 6 tentativas')
            if tentativas > 5 and pop:
                print('4. População         - custa 5 tentativas')
            if tentativas > 7 and cont:
                print('5. Continente        - custa 7 tentativas')
            print('''0. Sem dica                       
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
''')
            #pede para escolher a dica
            dica_escolhida = int(input('Escolha sua opção [0|1|2|3|4|5]:'))
            
            #dica esta fora das opcoes
            while dica_escolhida >5  or dica_escolhida <  0:
                print ('Escolha uma opção valida!')
                dica_escolhida = int(input('Escolha sua opção [0|1|2|3|4|5]:'))
      
            #faz ação da dica:
            if dica_escolhida == 1 and cor_da_band:
                custo = 4
                cor = []
                pega_bandeira = (DADOS('bandeira'))
                for cores, valor  in pega_bandeira.items():
                    if valor > cor[1]:
                        cor = [cores, valor]
                cor_da_bandeira.append(cor[0])
                DICAS['cor_da_bandeira'] = cor_da_bandeira
                tentativas -= custo
            if dica_escolhida == 2 and tentativas > 3:
                custo = 3
                letra_sorteada = (sorteia_letra(capital,letra_da_capital))
                letra_da_capital.append(letra_sorteada)
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
            if dica_escolhida == 5 and cont and tentativas > 7:
                custo = 7
                DICAS['continente'] = dados_pais_sorteado['continente']
                tentativas -= custo
                cont = False
            print('Distâncias:')
            for dist in distancias:
                print('{:.0f} km -> {}'.format(dist[1],dist[0]))
            print('Dicas:')
            for dica,value in DICAS.items():
                if dica == 'cor_da_bandeira':
                    print('   - Cores da bandeira: {}'.format(value))
                if dica == 'letra_da_capital':
                    print('   - Letras da capital: {}'.format(value))
                if dica == 'area':
                    print('   - Área:{} km2'.format(value))
                if dica == 'populacao':
                    print('   - População: {} habitantes'.format(value))
                if dica == 'continente':
                    print('   - Continente: {}'.format(value))
                    
            #palpite é desisto 
        elif pais_palpite == 'desisto':
            quer_desistir = input('Tem certeza que deseja desistir da rodada? [S|N]')
            if quer_desistir == 'S':
                print("Até Próxima Vez! :) ")
            
            #palpite nao foi reconhecido
        else:
            print('país desconhecido')
            
    quer_jogar = False
