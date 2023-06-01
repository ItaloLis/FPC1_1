n = int(input())

pecas = [int(i) for i in input().split(" ")]

for i in range(1, n+1):
  for j in pecas:
    if i != j:
      print(i)

      
lista = [i for i in range(1, n+1)]
print(lista)
