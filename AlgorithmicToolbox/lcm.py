#Uses python3
import sys

def gcb(a,b):
    if b == 0:
        return a
    else:
        remainder = a % b
        return gcb(b,remainder)

def lcm(a, b):
    tmp = a*b // gcb(a,b)
    return tmp

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

