def soma(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

n_pecas = int(input())
pecas = [int(i) for i in input().split(" ")]
todas = [i for i in range(1, n_pecas+1)]

peca_perdida = soma(todas) - soma(pecas)
print(peca_perdida)
