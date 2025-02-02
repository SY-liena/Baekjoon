T = int(input())
num = 0
result = [0] * T

for i in range(T):
    a, b = map(int, input().split())
    result[i] = a + b

for i in range(T):
    print(f'Case #{i+1}: {result[i]}')
