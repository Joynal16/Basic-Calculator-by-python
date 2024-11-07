"""

                       print("Welcome to calculator")
                          print("1.Addition")
                            print("2.Substraction")
                              print("3.Multiplication")
                                                              """

option = int (input("Basic Calculation operation:"))


if option == 1 or option == 2 or option == 3 or option == 4:

    # Step-1; Addition Process.
    n1 = int(input("enter The first Number: "))
    n2 = int(input("enter The first Number: "))
    n3=n1+n2
    print("Addition is " +str(n3))


    # Step-2; Subtraction Process.
    n1 = int(input("enter The first Number: "))
    n2 = int(input("enter The first Number: "))
    n3 = n1 - n2
    print("Substration is " + str(n3))

    # Step-3; Multiplication Process.
    n1 = int(input("enter The first Number: "))
    n2 = int(input("enter The first Number: "))
    n3 = n1 * n2
    print("Multiplication is " + str(n3))

    # Step-4; Divion Process.
    n1 = int(input("enter The first Number: "))
    n2 = int(input("enter The first Number: "))
    n3 = n1 / n2
    print("Division is " + str(n3))

else:
    print("Invalid Input")