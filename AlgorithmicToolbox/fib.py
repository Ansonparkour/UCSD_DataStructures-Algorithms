#Uses python3
def calc_fib(n):
    f = []
    #python range() have trick, should be attention
    for i in range(n+1):
        f.append(0)
    f[0] = 0
    f[1] = 1
    if (n <= 1):
        return n
    else:
        for j in range(2, n+1):
            f[j] = f[j-1] + f[j-2]
    return f[n]

n = int(input())
print(calc_fib(n))

