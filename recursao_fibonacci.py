#recursao:
#fibonacci recursivo
#sequencia de fibonacci: 0 1 1 2 3 5 8 13 21 34 55 ...

def fibRec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibRec(n - 1) + fibRec(n - 2)


def menu():
    n = int(input("Quantos termos devem ser exibidos? (maior que 2)"))
    for i in range(1, n+1):
        print(fibRec(i))

menu()
