#https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/st-hash.html
#Questões - Tabelas Hash

#q1
def funcHash(chave, tamanho):
    return chave % tamanho


#q4
def colisoes(tabela):
    total = 0
    for i in tabela:
        if len(i) > 1:
            total += len(i)-1
    return total


#q5
'''
Versão errada, p achar a posição da chave
def busca(chave, tabela):
    pos = funcHash(chave, len(tabela))
    if chave in tabela[pos]:
        return pos #Achou o elemento
    else:
        return None #Não achou'''

def busca(chave, tabela):
    pos = funcHash(chave, len(tabela))
    for elem in tabela[pos]:
        if elem != None:
            if elem[0] == chave: #achou
                return elem[1]
    else:
        return None #Não achou, lista terminou


#q6 Sondagem linear
def InserirSondLin(chave, tabela):
    pos = funcHash(chave, len(tabela))
    while tabela[pos] != None:
        pos += 1
        if pos == len(tabela):
            pos = 0
    tabela[pos] = chave
#pos = (pos + 1) % len(tabela)   substitui 3 linhas: 41 a 43


#q7 Sondagem Quadrática
def InserirSondQuad(chave, tabela):
    pos = chave % len(tabela)
    i = 0
    while tabela[pos] != None:
        i += 1
        pos = (pos + i**2) % len(tabela)
    tabela[pos] = chave

