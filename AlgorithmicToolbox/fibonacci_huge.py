# Uses python3
import sys
def get_fibonacci(n,m):
    f = []
    for i in range(n+1):
        f.append(0)
    f[0] = 0
    f[1] = 1
    if (n <= 1):
        return n
    else:
        #j from 2 to n
        for j in range(2, n+1):
            f[j] = (f[j-1] + f[j-2]) % m
    return f[n]


def get_remainder_len(m):
    k = 1
    remainder = [0]
    while True:
        remainder.append(get_fibonacci(k,m))
        if (k>2) & (remainder[k] == 1) & (remainder[k-1] == 0):
            remainder = remainder[0:k-1]
            break
        k = k +1
    return len(remainder)


def get_fibonaccihuge(n,m):
    f = n % get_remainder_len(m)
    tmp = get_fibonacci(f,m)
    return tmp

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))

