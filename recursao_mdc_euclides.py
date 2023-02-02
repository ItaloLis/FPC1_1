def MDC(a, b):
  if (b==0):
    return a
  else:
    return MDC(b, a % b)
  
  # Máximo divisor comum segundo Euclides
