'''
Факториалом числа называют произведение всех натуральных чисел до него включительно. Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.

Формула нахождения факториала:

n! = 1 * 2 * … * n,
'''
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f
print(factorial(5))