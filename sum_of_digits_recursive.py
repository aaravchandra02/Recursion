def sum_digits(n):
    if n == 0:
        return(n)
    else:
        res = n % 10
        return res+sum_digits(n//10)


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)
