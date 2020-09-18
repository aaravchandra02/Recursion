# define your sum_to_one() function above the function call
def sum_to_one(n):
    result = 1
    call_stack = []

    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")

# This is where the separate values stored in the call stack are accumulated into a single return value.
    while len(call_stack) != 0:
        return_value = call_stack.pop()
        print(
            f"Return value of {return_value['n_value']} adding to result {result}")
        result += return_value['n_value']

    return result, call_stack


sum_to_one(4)
