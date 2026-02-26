def fact(n):
  if n == 0:
    return 1
  return n*fact(n-1)
print(fact(4))



def factNumber(i, n, count):
    if i > n:
        print(count)
        return
    factNumber(i + 1, n, count * i)

factNumber(1, 5, 1)

def factorial(n, b, i, c):
    if i > n:
        print(c)
        return
    factorial(n, b - 1, i + 1, c * b)

factorial(5, 5, 1, 1)
