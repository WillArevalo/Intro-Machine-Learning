def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
fib(int(input("Serie de Fibonachi, ¿número de términos?: "))
