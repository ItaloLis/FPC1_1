n1, n2, exp, total = 37, 38, 0, 0

for i in range(1, 38):
    exp = n1*n2/i
    total += exp
    n1 -= 1
    n2 -= 1

print("%.2f" %total)
