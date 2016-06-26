#Uses python3
import sys

'''
#naive algorim
def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
'''

#Euclidean Algorithm
def Euclidean(a,b):
    if b == 0:
        return a
    else:
        remainder = a % b
        return Euclidean(b,remainder)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(Euclidean(a, b))
