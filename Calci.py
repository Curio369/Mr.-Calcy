import art
print(art.logo)



def add(n1, n2):
    return n1 + n2
def subtract(n1 , n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

conti_main = True
while conti_main:
    n1 = int(input("Enter First Number :" ))
    conti = True
    while conti:
        print("Choose the Mathematical operator +, -, * , /")
        operator = input("Enter the operator: ")
        n2 = int(input("Enter Second Number: " ))
        operations = {"+": add(n1, n2), "-": subtract(n1, n2), "*": multiply(n1, n2), "/": divide(n1, n2)}
        result = operations[operator]
        print("Your Result is" , result)
        conditional = (input("Enter Y to continue or N to start fresh: "))
        if conditional == "Y":
            n1 = result
            conti = True
        else:
            conti = False
            print("\n" *20)