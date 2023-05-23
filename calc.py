#functions

def print_menu():
    print("-----------")
    print("[1] sum")
    print("[2] subtract")
    print("[3] multiply")
    print("[4] divide")


print_menu()
selection=input("Choose the operation")
number_1=float(input("Choose the first number"))
number_2=float(input("Choose the second number"))

def operation(selection,one,two):
     if selection =="1":
        total=one+two
        print(str(total))
     elif selection =="2":
        total=one-two
        print(str(total))
     elif selection =="3":
        total=one*two
        print(str(total))
     elif selection =="4":
            if two==0:
                print("you cannot divide by 0")
            else:
                total=one/two
                print(str(total))

operation(selection, number_1,number_2)

