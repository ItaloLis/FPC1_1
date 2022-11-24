idade = 200
soma, qtde, media, maior, menor = 0, 0, 0, 0, 200

while idade != 0:
     idade = int(input("Digite uma idade ou 0 para parar: "))
     soma += idade
     if idade > 0:
         qtde += 1
         if idade > maior:
             maior = idade
         if idade < menor:
             menor = idade

media = soma/qtde
print("Soma das idades: ", soma)
print("Quantidade de idades: ", qtde)
print("Média das idades: %.2f" %media)
print("Maior idade: ", maior)
print("Menor idade: ", menor)
