#bibliotecas
import random

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
