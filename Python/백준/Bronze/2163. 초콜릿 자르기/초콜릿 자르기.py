a, b = map(int, input().split())

def devide(x, y):
    result = (x - 1) + x * (y-1)
    return result

print(devide(a, b))