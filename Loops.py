#loops

for i in range(1, 10, 2): #2 is step size
    print("Hello")

for i in range(2, 10, 2):
    print(i)

animals = [
    {"name": "Mango", "type": "dog", "age": 7},
    {"name": "Berry", "type": "dog", "age": 12},
    {"name": "Tom", "type": "cat", "age": 7},
    {"name": "abbas", "type": "turtle", "age":27}
]

for animal in animals:
    if animal["type"] == "dog":
        print("It is a dog")
    elif animal["type"] == "cat":
        print("It is a cat")
    else:
        print("It is neither a dog nor a cat")

        # lets print wether numbers from 1 to 100 are even or odd
    for i in range(1, 100):
     if i % 2==0:
        print("it is even")
    else:
        print("it is odd")  

name = "Omar"
age = 33
print(f"My name is {name} and I am {age} years old")       


for i in range(10, 0, -1):
 print(i)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
   print(f"I like {fruit}")

count = 1

while count <= 5:
   print(f"Count is {count}")
   count += 1

#guessing game

secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number(1-10): "))
    if guess < secret_number:
        print("too low!")
    elif guess > secret_number:
        print("too high!")
    else:
        print("your guess was correct!")
