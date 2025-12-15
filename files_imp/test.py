def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

num = int(input("\nEnter a number: "))
print(sum_of_digits(num))
