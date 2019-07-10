for i in range(1,11):
    print(i)
# The i is iterating from 1 to 10 and comes out when the loop reaches 11 and is executing the code in the indentation below it

for j in [1,2,3]:
    print(j)
# j is taking on values 1,2,3 and executing the code in the indentation

# Using range to do the same thing
for j in range(1,4):
    print(j)

j = [1,2,3]
print(type(j))

# j[1,2,3] is list
for k in range(0,19,2):
    print(k)

# Function staroffour to produce this
# ****
# ****
# ****
# ****

def staroffour():
    for i in range(0,4):
        asterisk = ""
        for j in range(0,4):
            asterisk += "*"
        print(asterisk)

staroffour()

# Function dancingstars() to produce this
# *
# **
# ***
# ****
# ***
# **
# *

def dancingstars():
    asterisk = ""
#     red =
    for j in range(0,7):
        if j < 4:
           asterisk += "*"
        else:
            asterisk = asterisk[0:len(asterisk)-1]
        print(asterisk)


dancingstars()

print("\n\n")
# String as input and searches for letter
def findThatString(sentence,letter):
    for i in range(len(sentence),0,-1):
        if(sentence[len(sentence)-i] == letter):
            return "true"
            break
        if i == 1:
            return "false"

sentence = input("Please enter your sentence\n")
letter = input("Please what letter is being searched for?\n")
print(findThatString(sentence,letter))