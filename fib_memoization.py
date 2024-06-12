#fibonacci using memoization
d = {}
def fib_mem(n):
    if n in d:
        return d[n]
    elif n==1 or n==2:
        return 1
    elif n<=0:
        return 0
    else:
        res = fib_mem(n-1) + fib_mem(n-2)
        d[n] = res
    return res
print(fib_mem(7))