#list
colors =["white", "black", "red", "green"]

#to add, or what was push in JS
colors.append("burgundy")
print(colors)

#get any element
print (colors[0])

# for loops in python
for color in colors: #for (i=0; i<colors.length, i++)
    print(color)

#dictionaries
me = {
    "first_name":"John",
    "last_name" : "Doe",
    "age":36
}

print (me)
print (me["first_name"])

me["age"] =99

#add a new element
me["color"] = "blue"