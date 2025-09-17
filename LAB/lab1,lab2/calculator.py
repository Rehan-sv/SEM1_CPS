# To implement basic arithemetic operations with a calculator interface
count = 0
number_of_runs = int(input("Enter the number of runs you want"))
while(count <  number_of_runs):
    n1 =int(input("enter a number"))
    n2= int(input("enter a number"))
    choice = input("enter your choice (+ or - or * or /)")

    if(choice== "+"):
        print("u have chosen ADDITION")
        print(n1+n2)
    elif(choice=="-"):
        
        print("u have chosen DIFFRENCE")
        print(n1-n2)
    elif(choice=="*"):
        
        print("u have chosen MULTIPLICATION")
        print(n1*n2)
    elif(choice=="/"):
        
        print("u have chosen DIVISION")
        print(n1/n2)
    else:
        print("you have not chosen the given operators")
    count =count +1
print("program ends.")
