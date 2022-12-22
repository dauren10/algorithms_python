# Fn = Fn-1 + Fn-2
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(9))
