def tail_factorial(n, accumulator=1):
  if n == 0: return accumulator
  else: return tail_factorial(n-1, accumulator * n)
