a, b = map(int, input().strip().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return print(a)

def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm == greater
            break
        greater += 1

    return print(greater)


gcd(a,b)
lcm(a,b)