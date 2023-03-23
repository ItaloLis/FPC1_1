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

