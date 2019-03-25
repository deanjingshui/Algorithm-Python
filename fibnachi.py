"""
斐波那契数列
"""

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(8))
print(fib(10))