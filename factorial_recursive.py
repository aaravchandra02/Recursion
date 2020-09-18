
def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)


# valid value till this input size
print(factorial(998))
# error thrown "RecursionError: maximum recursion depth exceeded in comparison"
print(factorial(999))
