try:
    age = int(input("How old are you?"))
    if age > 18:
        print("You can drive at age {age}.")
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")