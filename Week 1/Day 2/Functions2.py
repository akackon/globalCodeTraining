# Write another function called get_name, which does the same
# but for the users name.
def get_name():
    name = input("Enter your name : ")
    return name


print("Your name is", get_name(), " and your name is a ", type(name))