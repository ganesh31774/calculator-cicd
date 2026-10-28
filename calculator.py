def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    if b==0:
        raise ValueError("cannot divide by zero")
    return a/b
def main():
    a=10
    b=5
    print("Python Calculator")
    print("First number:",a)
    print("Second number:",b)
    print("Addition:",add(a,b))
    print("Subtraction:",subtract(a,b))
    print("Multiplacation:",multiply(a,b))
    print("Division:",devide(a,b))
if __name__ =="__main__":
    main()
