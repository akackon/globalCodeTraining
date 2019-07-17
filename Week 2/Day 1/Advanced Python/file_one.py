def is_even(x):
    if x % 2 == 0:
        return True

def someFunction(x):
    return not(is_even(x))

numbers = [1,56,234,87,4,76,24,69,90,135]
print(list(filter(someFunction,numbers)))

# print(list(map(is_even,numbers)))