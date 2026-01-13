#student profile

"""Name = "jet"
Age = 16
Height = 6.7
IsStudent = True"""

#print("Student Name:", Name, "Age:", Age, "Height:", Height, "IsStudent:", IsStudent)
#print(f"Student Name: {Name} \nAge: {Age} \nHeight: {Height} \nIs a student: {IsStudent}")

"""x = 14
y = 10

sum = x+y

print(f"sum1 {sum}")

sum = sum*8

print(f"sum2: {sum}")"""

"""Name = input("Name: ")

Food = input("What is the best food?: ")

print(f"{Name}'s favorite food is: {Food}") """

"""num = bool(input("number1: "))
num2 = str(input("number2: "))


sum = num + num2

print(f"Solution: {sum}")"""

"""age = int(input("Please enter age: "))"""

"""if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
elif age < 0:
    print("Invalid Age")
else:
    print("kid")"""

"""password1 = int(input("Enter pass1: "))
password2 = str(input("Enter Pass2: "))

#pass1: 6767
#pass2: python
#pass1 and pass2 must be enter corectly in order to unlock

if (password1 == 6767 or password2 == "python"):
    print("unlocked")
else:
    print("invalid password")"""

name = "jet"

"""for i in name:
    print(f"Letter: {i}")
    print(i)
print(i)"""


"""password = ""
trys = 0
IsFalse = True

while password != 6767:
    password = int(input("Enter Password: "))
    trys += 1
    if(trys == 5):
        print("max trys has been reached")
        IsFalse == False
        break

if (IsFalse):
    print("Access Granted")"""


"""List = [1, 2, 3, 4, 5, 6, 7]

for i in List:
    print(i)"""

"""def greet(name, age):
    return(f"Hello: {name}\nwho is {age} years old")

message = greet("BHS coding club", 0)

#print(greet("jet", 17))

age = int(input("Enter Age: "))
name = input("age: ")

print(greet(name, age))"""

"""import functions

numbers = functions.add(12, 40)
print(numbers)"""

import cowsay

user = input("Enter a sentance: ")
cowsay.cow(user)
cowsay.trex("hello")