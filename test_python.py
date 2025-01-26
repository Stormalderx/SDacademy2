#integer variable

apples_amount = 10

print("Hello world")
print(apples_amount, type(apples_amount))

#boolean variable
adult = True
print(adult, type(adult))


#float variable
pi = 3.14  #. not , !!!
print(pi, type(pi))

#string variable
name = "Ola" # 'Ola'
print(name, type(name))

'''
    variable = "2" (it is a string because it is inside quotes)
    variable2 = 2  (integer) ARE NOT THE SAME!!!    
'''

string1 = "Ola"
string2 = " Duda"

print(string1+string2)

#1
number1 = 3
number2 = 5
print(number1+number2) #8

#2
number1 = "3" #strings
number2 = "5" #strings
print(number1+number2) # "35"

#3
number1 = "3"
number2 = "5"
print(number1+number2) #AN ERROR! You can't do this, because it is str and int
print("Ola 2")

#4
person_info = {"name":"omar", "eyes_color":"Brown", "Pipedrive":6, "engineer": True}
print(person_info)
print(person_info["eyes_color"])
person_info["hair_color"] = "black"
print(person_info)
