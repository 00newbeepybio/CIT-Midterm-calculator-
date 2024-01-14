def calc():
    #Write complete Additon, Subtraction, Multiplication, and Division (Case Specific)
    o=input(str("Enter your Operation (+,-,*,/): "))
    A= str("+")
    S= str("-")
    M= str("*")
    D= str("/")
    value1=int(input("Enter your Value1: "))
    value2=int(input("Enter your Value2: "))
    if o == "+":
     print (int(value1+value2))
    elif o == "-":
     print (int(value1-value2))
    elif o == "*":
     print (int(value1*value2))
    elif o == "/":
     print (int(value1/value2))
    else:
     print ("Invalid Input")

calc()
