def addition():
    return firstvalue+secondvalue

def subtraction():
    return firstvalue-secondvalue

def multiply():
    return firstvalue*secondvalue

def division():
    return firstvalue/secondvalue

def modulodivision():
    return firstvalue%secondvalue

def Calculator(firstvalue,secondvalue,operation):

    if operation == "+":
        print(addition())
    elif operation == "-":
        print(subtraction())
    elif operation == "*":
        print(multiply())
    elif operation == "/":
        print(division())
    elif operation == "%":
        print(modulodivision())
    else:
        print("enter a valid operator")
        
firstvalue =int(input("enter first value : "))
secondvalue =int(input("enter second value : "))
operation =input("enter operator only + - * / : ")
Calculator(firstvalue,secondvalue,operation)
