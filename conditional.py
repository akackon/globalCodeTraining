# i = 8
# if(i % 2 == 0):
#     print ("Even Number")
# else:
#     print ("Odd Number")

#function that takes a list of numbers and returns the sum of all the even numbers

def sum_evens(n):
    numbers = [n]
    print ("Enter the numbers \n")
    for i in range(0,n):
        numbers[i] = int(input())
        print (numbers[i])
    add = 0
    for i in range(0,len(numbers)):
        if numbers[i] % 2 == 0:
            add += numbers[i]
            print (add)

sum_evens(5)

