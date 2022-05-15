#bibliotecas
import random
import math
import string

#normalizando base de paises
def normaliza(dic):
  novo_dic = {}
#passa pelos items do dicionario
  for continente, paises in dic.items():
#passa pelos items da lista de paises 
    for pais, dados in paises.items():
#define dados quando se trata de continente
      dados['continente'] = continente
      novo_dic[pais] = dados
  return novo_dic


#sorteia um pais da lista de paises
def sorteia_pais(dicionario):
    return random.choice(list(dicionario.keys()))
    

#ordena lista de paises
def adiciona_em_ordem(pais,distancia,lista):
    pais_formatado = [pais,distancia]
    i = 0
    
    # lista vazia:
    if len(lista) == 0:
        return [pais_formatado]
    
    #encaixa na poscição correta caso len(lista) > 1:
    while i < len(lista):
        pais_da_lista = lista[i]
        if distancia > pais_da_lista[1]:
            i += 1
        else:
            lista.insert(i,pais_formatado)
            i = len(lista)
    return lista

#verifica se pais esta em lista de paises
def esta_na_lista(pais,lista):
    i = 0
    while i < len(lista):
        pais_da_lista = lista[i]
        if pais_da_lista[0] == pais:
            return True
        else:
            i += 1
    return False

#calcula distancia de haversine
def haversine(raio,o1,l1,o2,l2):

    sin_o = math.sin(((o2 - o1)/2)*(math.pi/180))**2
    cos_o1 = math.cos(o1*(math.pi/180))
    cos_o2 = math.cos(o2*(math.pi/180))
    sin_l = math.sin(((l2 - l1)/2)*(math.pi/180))**2

    distancia = 2*raio * math.asin((sin_o+cos_o1*cos_o2*sin_l)**0.5)

    return distancia

#Sorteia Letra fora de uma lista de Restrições
def sorteia_letra(palavra,lista_restrita):
    #removendo caracteres indesejados
    palavra = palavra.lower()
    palavra = palavra.replace(' ','')
    for caracter in string.punctuation:
        if caracter in palavra:
            palavra = palavra.replace(caracter,'') 
    #removendo caracteres restritos
    for restricao in lista_restrita:
        palavra = palavra.replace(restricao,'')
    #palavra vazia
    if palavra == '':
        return ''
    #sorteia caractere
    else:
        return random.choice(palavra)
 #define distancias e suas cores     
 def verifica_cor(dist):
    if dist[1] <= 1000:
        print('\33[96m{:.0f} km -> {} \33[0m'.format(dist[1],dist[0])) #ciano
    if dist[1] > 1000 and dist[1] <= 2000:
        print('\33[93m{:.0f} km -> {} \33[0m'.format(dist[1],dist[0])) #amarelo
    if dist[1] > 2000 and dist[1] <= 5000:
        print('\33[91m{:.0f} km -> {} \33[0m'.format(dist[1],dist[0])) #vermelho
    if dist[1] > 5000 and dist[1] <= 10000:
        print('\33[95m{:.0f} km -> {} \33[0m'.format(dist[1],dist[0])) # roxo
    if dist[1] > 10000:
        print('\33[90m{:.0f} km -> {}\33[0m'.format(dist[1],dist[0])) # preto)
