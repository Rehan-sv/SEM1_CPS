n = int(input("Enter number of tokens: "))
tokens = list(map(int, input("Enter tokens (sorted): ").split()))
key = int(input("Enter search token: "))

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2
    if tokens[mid] == key:
        print("Token found at position", mid + 1)
        break
    elif tokens[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Token not found")
