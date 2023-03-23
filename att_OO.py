#Att - OO

#q1
class Pessoa:
    def __init__(self, idade):
        self. idade = idade

def ordenarPessoas(lista):
    #usando bubble sort
    troca = True
    while troca:
        troca = False
        k = 1
        for i in range(n-k):
            if lista[i].idade > lista[i+1].idade:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                troca = True
        k += 1
    return lista
