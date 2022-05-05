#bibliotecas
import random
import math

#sorteia um pais da lista de paises
def sorteia_pais(dicionario):
    pais = random.choice(list(dicionario.items()))
    return (pais[0])

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

def haversine(raio,o1,l1,o2,l2):

    sin_o = math.sin(((o2 - o1)/2)*(math.pi/180))**2
    cos_o1 = math.cos(o1*(math.pi/180))
    cos_o2 = math.cos(o2*(math.pi/180))
    sin_l = math.sin(((l2 - l1)/2)*(math.pi/180))**2

    distancia = 2*raio * math.asin((sin_o+cos_o1*cos_o2*sin_l)**0.5)

    return distancia

#Sorteia Letra fora de uma lista de Restrições
import random
import string

def sorteia_letra(palavra,lista_restrita):
    palavra = palavra.lower()
    palavra = palavra.replace(' ','')
    for caracter in string.punctuation:
        if caracter in palavra:
            palavra = palavra.replace(caracter,'')
    for restricao in lista_restrita:
        palavra = palavra.replace(restricao,'')
    if palavra == '':
        return ''
    else:
        letra = random.choice(palavra)
        return letra
