def pytriple(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if(a*a+b*b == c*c):
        return True
    else:
        return False

print(pytriple(input("Enter first number:"), input(
    "Enter second number:"), input("Enter third number:")))
