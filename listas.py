#ex listas

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(l))

nova_lista = l[0:6] # pega os que estão nas posições 0, 1 e 2. Tem a mesma limitação do range()
print(nova_lista)

pares = l[0:9:2]
print(pares)

paresparcialmenteinvertida = pares[4:0:-1]
print(paresparcialmenteinvertida)

novalista_invertida = l.reverse()
print(novalista_invertida)
