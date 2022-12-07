

num = int(input('Enter:'))

def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


for i in range(num):
    print(fibonacci(i))
