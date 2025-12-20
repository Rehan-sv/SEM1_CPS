def test(n):
    if n >= 15:
        return n - 5
    else:
        return test(test(n + 3))
print(test(6))