def bubbleSort(lista, tamanho):
    troca = True
    while troca:
        troca = False
        for i in range(tamanho-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                troca = True
    return lista

def main():
    lista = list
    list1 = [28, 26, 30, 24, 25, 102, 100, 50]
    print(bubbleSort(list1, len(list1)))

main()

#ou

lista = list
lista = [28, 26, 30, 24, 25, 102, 100, 50]
for i in range(len(lista)-1):
    if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
    for r in range(len(lista)-1, 0, -1):
        if lista[r] < lista[r-1]:
            lista[r], lista[r-1] = lista[r-1], lista[r]
print(lista)
