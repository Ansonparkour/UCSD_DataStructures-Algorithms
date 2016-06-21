# Uses python3

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

a.sort(reverse=True)

result = a[0] * a[1]


print(result)



