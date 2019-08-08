import math

def fibo(n):
    r5 = math.sqrt(5)
    phi = (1+r5) / 2
    phih = (1-r5) / 2
    return int((phi**n - phih**n) / r5)


print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))

