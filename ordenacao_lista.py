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


# inserção direta:

def insSort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i
        while j > 0 and lista[j-1]>chave:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = chave
    return lista

lista = list
lista = [27, 12, 20, 37, 18, 17, 15]
print(insSort(lista))


#Inserção por incremento

def shellSort(nums):
    n = len(nums)
    h = int(n/2)
    while h>0:
        for i in range(h, n):
            c = nums[i]
            j = i
            while j >=  and c < nums[j-h]:
                nums[j] = nums[j-h]
                j = j-h
                nums[j] = c
        h = int(h/2.2)
        
