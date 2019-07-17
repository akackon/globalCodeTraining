def fold(x):
    running_total = 0
    for item in x :
        running_total += item
    print(running_total)
numbers = [1, 2, 3, 4, 5]
fold(numbers )