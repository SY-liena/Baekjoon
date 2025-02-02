x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def nemo(a, b, c):
    lst = [a, b, c]
    if(lst.count(a) == 1):
        return a
    elif(lst.count(b) == 1):
        return b
    else:
        return c

print(nemo(x1, x2, x3), nemo(y1, y2, y3))