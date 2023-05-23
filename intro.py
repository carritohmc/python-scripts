print ("hello world!")
# variables
name = "Felix"
last_name ='Algo'
age =99
found = True
print (name)

# if / else statements, elif is else if
if age <100:
    print ("you're still young")
    print (name)
elif age ==100:
    print ("congrats you're a century")
else:
    print("sorry you're getting old")

# functions need def name_of_function():
def say_hello():
    print("hello There")

# to call
say_hello()

#function that expects a value
def say_goodbye(name):
    print ("goodbye" + name)

say_goodbye("adrian")

# algebraic functions
print (1+2)
print (9-3)
print (100/10)

print ("my name is" + name + "and my age is"+ str(age))