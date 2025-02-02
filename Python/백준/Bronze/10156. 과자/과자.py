a, b, c = map(int,input().split())

def money(x, y, z):
    result = x * y - z
    if result < 0 :
        return 0
    return result

print(money(a, b, c))