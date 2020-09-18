
def fibonacci_sum(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    # recursive step
    print(f"Recursive call with {n} as input")
    return fibonacci_sum(n-1)+fibonacci_sum(n-2)


fibonacci_sum(5)
fibonacci_runtime = "2^N"
