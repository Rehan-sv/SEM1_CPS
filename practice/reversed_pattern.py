n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(j, end=' ')
    print()
for i in range(n, -1, -1):
    for j in range(i):
        print(j, end=' ')
    print()
