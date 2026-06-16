print(" <--- SIMPLE CALCULATOR --- >");
a=float(input("Enter number 1:"));
b=float(input("Enter number 2:"));
c=input("Choose your operation(+, -,*,/):")
if(c == "+"):
     print("Result:",(a+b));
elif(c == "-"):
    print("Result:",(a-b));
elif(c == "*"):
    print("Result:",(a+b));
elif(c == "/"):
    if(a != 0):
        print("Result:",(a/b));
    else:
        print("Division is not possible");
else:
    print("Invalid operation");
