def fibRec(n):
  if n==1: return 0
  elif n==2: return 1
  else: return fibRec(n-1) + fibRec(n-2)
  
for i in range(1, 8):
  print fibRec(1)
  
#Exemplo de recursão
