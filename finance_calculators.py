#This code allows the user to access two financial calculators based on their selection. One is ain investment calculator and the other one is a home loan repayment calculator.

import math

#Allow the user to select an investment calculator or a bond calculator. 

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond- to calculate the amount you'll have to pay on a home loan.")

user_choice = input("Enter either investment or bond below to proceed:")

user_choice = user_choice.lower()


#Calculate the investment only if the user chooses this option.
if user_choice == "investment":
    
    #Ask for the information needed.
    initial_amount = input("Please enter the amount of money you are depositing:")
    interest_rate = input("Please enter the interest rate as a whole number.")
    investment_time= input("Please enter the number of years you plan on investing.")
    #Ask user to choose between simple or compound interest.
    interest = input("Please write 'simple' or 'compound' depending on the type of interest you want to calculate. ")
    interest = interest.lower()

    #Convert all taken values to floats.
    initial_amount = float(initial_amount)
    interest_rate = float(interest_rate)
    investment_time = float(investment_time)

    #Convert interest rate in a percentage 
    interest_rate = interest_rate/100

    #Do the simple interest calculation only user chose simple.
    if interest == "simple":
        #Calculate simple interest and store the total amount once the interest has been applied in a variable called simple_interest.
        simple_interest = initial_amount * (1 + interest_rate * investment_time)
        print("The total amount once the interest has been applied will be " + str(simple_interest))
    #Do the compount interest calculation if the user input is equal to compound.
    elif interest == "compound":
        compound_interest= initial_amount * math.pow((1+ interest_rate), investment_time)
        print ("The total amount once compound interest is applied will be:" + str(compound_interest))

#Next part of the code calculates the bond if this is what the user chose. 
elif user_choice == "bond":
    #Ask the user to input the information needed.
    house_value = input("Please enter the present value of the house.")
    interest_rate = input("Please enter the interest rate as a whole number.")
    repay_time = input("Please enter the number of months you plan to take to repay the bond.")

    #Cast the variables to floats. 
    house_value = float(house_value)
    interest_rate = float(interest_rate)
    repay_time = float(repay_time)

    # Convert percentage to decimal
    annual_interest_rate = interest_rate / 100  

    print(annual_interest_rate)

    # Convert annual rate to monthly rate
    monthly_interest_rate = annual_interest_rate / 12  

    print(monthly_interest_rate)

    # Calculate the bond using the repayment formula.
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-repay_time))

    print("You will have to pay: " + str(repayment) + " every month to pay your bond")
    

    


