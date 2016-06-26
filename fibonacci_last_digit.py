#Uses python3
import sys
def get_fibonacci_last_digit(n):
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
            f[j] = (f[j-1] + f[j-2]) % 10
    return f[n]

if __name__ == '__main__':
    #use sys to input data is only working for shell, not any IDE
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
