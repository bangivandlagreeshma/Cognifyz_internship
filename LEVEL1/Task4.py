def calculator():
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    operator=input("Enter an opertor:")
    if operator=="+":
        result=n1+n2
    elif operator=="-":
        result=n1-n2
    elif operator=="*":
        result=n1*n2
    elif operator=="/":
        result=n1/n2
    elif operator=="%":
        result=n1%n2
    elif operator=="//":
        result=n1//n2
    else:
        print("Invalid operator")
    print(f' The result is:{n1}{operator}{n2}={result}')
calculator()