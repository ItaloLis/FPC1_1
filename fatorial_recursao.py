def fatRecursivo(num):
  if (num == 1):
    return 1
  else:
    return num * fatRecursivo(num-1)
  
