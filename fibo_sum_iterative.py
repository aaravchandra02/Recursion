def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a = a+b
            a, b = b, a
        return(b)


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)
