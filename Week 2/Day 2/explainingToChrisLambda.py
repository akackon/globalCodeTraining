from
numbers = [1,3,5,11,64,532,32]
print(list(map(lambda x: x%2 == 0, numbers)))
print(list(filter(lambda x: x%2==0,numbers)))