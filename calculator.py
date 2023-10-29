#Simple Calculator
calculate = True

while (calculate == True) :
        
        print("\n < CALCULATOR >")
        
        num1 = int(input("\n Enter  first  number:"))
        num2 = int(input("Enter  second  number:"))

        print("\n Operation Choice :")
        print(" ' + ' for Addition")
        print(" ' - ' for Subtraction")
        print(" ' * ' for Multiplication")
        print(" ' / ' for Division")

        operator = input("\n Enter Operator :")
 
        match operator :
 
            case "+" :
                 print(f"Result : {num1} + {num2} = ",num1+num2)

            case "-" :
                print(f"Result : {num1} - {num2} = ",num1-num2)

            case "*" :
                print(f"Result : {num1} * {num2} = ",num1*num2)

            case "/" :
                if num2 == 0 :
                    print("Undefined ")
                else :
                    print(f"Result : {num1} / {num2} = ",num1/num2)

            case _ :
                print("Invalid operator")


            
        