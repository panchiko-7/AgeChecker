age = input("Enter your age: ")

try:
    age = int(age)

    if age >= 0 and age <= 12:
        print("You're a child")
    elif age >= 13 and age <= 19:
        print("You're a teen")
    elif age >= 20 and age <= 22:
        print("You're a young adult")
    elif age >= 23 and age <= 64:
        print("You're an adult ")
    elif age >= 65 and age <= 122:
        print('u are a senior')
    else:
        print("That's not a valid age ")

except ValueError:
    print("Enter a valid age")