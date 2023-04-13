def busca_li(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

def main():
    lista = [8, 5, 'abc', 32, 67, False]
    elemento = int(input('Digite o elemento que quer encontrar:'))
    
    indice = busca_li(lista, elemento)

    if indice != None:
        print(f'O índice do elemento {elemento} é {indice}')
    else:
        print('O elemento digitado não está na lista')

main()
