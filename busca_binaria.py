def busca_bi(lista, elem, comeco, final):
    if comeco <= final:
        meio = (comeco + final) // 2
        if lista[meio] == elem:
            return meio
        if elem < lista[meio]:
            return busca_bi(lista, elem, comeco, meio-1)
        else:
            return busca_bi(lista, elem, meio+1, final)
    return None
