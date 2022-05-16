# bibliotecas:
import string
import random
import math
#from dis import dis
from Base_de_paises import carrega_dados
from  Funções import *




DADOS = carrega_dados()
RAIO = 6371

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

#inicia o jogo
quer_jogar = True
while quer_jogar:
    #define parametros
    tentativas = 20
    distancias = []
    paises_palpitados = []
    cor = []
    acertou_pais = False
    cor_band = True
    ltr_cap = True
    ar = True
    pop = True
    cont = True
    foi_dicas = False
    cor_da_bandeira = []
    letra_da_capital = []
    opcao_de_dicas = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5'}

    DICAS = {}
    pais_sorteado = sorteia_pais(DADOS)
    #informações de pais sorteado
    dados_pais_sorteado = DADOS[pais_sorteado]
    pega_bandeira = (dados_pais_sorteado['bandeira'])
    capital = dados_pais_sorteado['capital']
    geo_pais_sorteado = dados_pais_sorteado['geo']
    coordenadas_pais_sorteado = [geo_pais_sorteado['latitude'],geo_pais_sorteado['longitude']]
    

    #chance de palpite caso tenha tentativas
    while tentativas>0:
        if tentativas <= 4 and cor_band:
            cor_band = False
            opcao_de_dicas[1] = ''
        if tentativas <= 3 and ltr_cap:
            ltr_cap = False
            opcao_de_dicas[2] = ''
        if tentativas <= 6 and ar:
            ar = False
            opcao_de_dicas[3] = ''
        if tentativas <= 5 and pop:
            pop = False
            opcao_de_dicas[4] = ''
        if tentativas <= 7 and cont:
            cont = False
            opcao_de_dicas[4] = ''

        
        # imprime tentatives e pergunta palpite
        print ('''
Você tem {} tentativa(s)'''.format('\33[96m {} \33[0m'.format(tentativas)))
        pais_palpite = input('Qual é o seu palpite?')
        pais_palpite = pais_palpite.lower()
        if pais_palpite == pais_sorteado:
            print("""
\33[92mParabéns Você Acertou o País !!!\33[0m""") #ciano
            acertou_pais = True
            tentativas = 0
        #palpite é inventario
        elif pais_palpite == 'inventario':
            print('''
Distâncias:''')
            for dist in distancias:
                verifica_cor(dist)
            print('''
Dicas:''')
            for dica,value in DICAS.items():
                if dica == 'cor_da_bandeira':
                    cor_da_bandeira_exibir = ', '.join(value)
                    print('   - Cores da bandeira: {}'.format(cor_da_bandeira_exibir))
                if dica == 'letra_da_capital':
                    letras_da_capital_exibir = ', '.join(value)
                    print('   - Letras da capital: {}'.format(letras_da_capital_exibir))
                if dica == 'area':
                    print('   - Área:{} km2'.format(value))
                if dica == 'populacao':
                    print('   - População: {} habitantes'.format(value))
                if dica == 'continente':
                    print('   - Continente: {}'.format(value))
        
        #palapite é um pais que nao foi palpitado antes
        elif pais_palpite in DADOS:
            if pais_palpite not in paises_palpitados:
                #calcula distancia do pais sorteado
                dados_pais_palpite = DADOS[pais_palpite]
                geo_pais_palpite = dados_pais_palpite['geo']
                coordenadas_pais_palpite = [geo_pais_palpite['latitude'],geo_pais_palpite['longitude']]
                distancia= haversine(RAIO,coordenadas_pais_sorteado[0],coordenadas_pais_sorteado[1],coordenadas_pais_palpite[0],coordenadas_pais_palpite[1])
                distancias = adiciona_em_ordem(pais_palpite,distancia,distancias)
                paises_palpitados.append(pais_palpite)
                tentativas -= 1 
                print("""
Distâncias:""")
                for dist in distancias:
                    verifica_cor(dist)
                if foi_dicas:
                    print('''
Dicas:''')
                for dica,value in DICAS.items():
                    if dica == 'cor_da_bandeira':
                        cor_da_bandeira_exibir = ', '.join(value)
                        print('   - Cores da bandeira: {}'.format(cor_da_bandeira_exibir))
                    if dica == 'letra_da_capital':
                        letras_da_capital_exibir = ', '.join(value)
                        print('   - Letras da capital: {}'.format(letras_da_capital_exibir))
                    if dica == 'area':
                        print('   - Área:{} km2'.format(value))
                    if dica == 'populacao':
                        print('   - População: {} habitantes'.format(value))
                    if dica == 'continente':
                        print('   - Continente: {}'.format(value))
            else:
                print("""
Este país ja foi palpitado""")

        #palpite foi pedir dica
        elif pais_palpite == 'dica':
            #print mercado de dicas, caso nao tenha tentativas suficiente dica nao é imprimida
            print('''
            Mercado de Dicas
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-''')
            if cor_band:
                print('1. Cor da Bandeira   - custa 4 tentativas')
            if ltr_cap:
                print('2. Letra da capital  - custa 3 tentativas')
            if  ar:
                print('3. Área              - custa 6 tentativas')
            if  pop:
                print('4. População         - custa 5 tentativas')
            if  cont:
                print('5. Continente        - custa 7 tentativas')
            print('''0. Sem dica                       
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
''')
            #pede para escolher a dica
            
            
            opc_str = (''.join(opcao_de_dicas.values()))
            x = list(opc_str)
            dica_escolhida = input('Escolha sua opção [{}]:'.format(('|'.join(x))))
            if dica_escolhida == '':
                dica_escolhida == 'filtro'
            if dica_escolhida in opcao_de_dicas.values():
                dica_escolhida = int(dica_escolhida)
            while dica_escolhida != 5 and dica_escolhida != 4 and dica_escolhida != 3 and dica_escolhida != 2 and dica_escolhida != 1 and dica_escolhida != 0:
                print ('Escolha uma opção valida!')
                dica_escolhida = input('Escolha sua opção [{}]:'.format(('|'.join(x))))
                if dica_escolhida == '':
                    dica_escolhida == 'filtro'
                if dica_escolhida in opcao_de_dicas.values():
                    dica_escolhida = int(dica_escolhida)
            #faz ação da dica:
            if dica_escolhida == 1 and cor_band:
                custo = 4
                valor_mais_alto = 0
                cor_i = ''
                for cores, valor  in pega_bandeira.items():
                    if valor > valor_mais_alto:
                        valor_mais_alto = valor
                        cor_i = cores
                if cor_i != 'outras':
                    pega_bandeira.pop(cor_i)
                    cor.append(cor_i) 
                    DICAS['cor_da_bandeira'] = cor
                    tentativas -= custo
                if cor_i == 'outras':
                    cor_band = False
                    opcao_de_dicas[1] = ''

                foi_dicas = True
            if dica_escolhida == 2 and ltr_cap:
                custo = 3
                letra_sorteada = (sorteia_letra(capital,letra_da_capital))
                letra_da_capital.append(letra_sorteada)
                DICAS['letra_da_capital'] = letra_da_capital
                tentativas-=custo
                if len(capital) == len(letra_da_capital):
                    opcao_de_dicas[2] = ''
                    ltr_cap = False
                foi_dicas = True
            if dica_escolhida == 3 and ar:
                custo = 6
                DICAS['area'] = dados_pais_sorteado['area']
                tentativas -= custo
                ar = False
                foi_dicas = True
                opcao_de_dicas[3] = ''
            if dica_escolhida == 4 and pop:
                custo = 5
                tentativas -= custo
                DICAS['populacao'] = dados_pais_sorteado['populacao']
                pop = False
                foi_dicas = True
                opcao_de_dicas[4] = ''
            if dica_escolhida == 5 and cont:
                custo = 7
                DICAS['continente'] = dados_pais_sorteado['continente']
                tentativas -= custo
                cont = False
                foi_dicas = True
                opcao_de_dicas[5] = ''
            print('''
Distâncias:''')
            for dist in distancias:
                verifica_cor(dist)
            if foi_dicas:
                print('''
Dicas:''')
            for dica,value in DICAS.items():
                if dica == 'cor_da_bandeira':
                    cor_da_bandeira_exibir = ', '.join(value)
                    print('   - Cores da bandeira: {}'.format(cor_da_bandeira_exibir))
                if dica == 'letra_da_capital':
                    letras_da_capital_exibir = ', '.join(value)
                    print('   - Letras da capital: {}'.format(letras_da_capital_exibir))
                if dica == 'area':
                    print('   - Área:{} km2'.format(value))
                if dica == 'populacao':
                    print('   - População: {} habitantes'.format(value))
                if dica == 'continente':
                    print('   - Continente: {}'.format(value))
                    
            #palpite é desisto 
        elif pais_palpite == 'desisto':
            quer_desistir = input('Tem certeza que deseja desistir da rodada? [S|N]')
            if quer_desistir == 'S' or quer_desistir == 's':
                #criar lista de respostas para desisto
                print("Que pena, o país era: {}".format(pais_sorteado))
                tentativas = 0
                acertou_pais = True
            
            #palpite nao foi reconhecido
        else:
            print('país desconhecido')
    if tentativas > 0:
        print('Você tem {} tentativas'.format(0))
    if acertou_pais == False:
        print('Lamentavelmente você perdeu, o país era: {}'.format(pais_sorteado))
    quer_continuar = input("""
Jogar Novamente?[S|N]""")
    if quer_continuar != 'S' and quer_continuar != 's':
        print("""
Até a Próxima! :)""")
        quer_jogar = False
