def somaLista(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaLista(lista[1:])

res = somaLista([4, 4, 9, 3])
print(res)
