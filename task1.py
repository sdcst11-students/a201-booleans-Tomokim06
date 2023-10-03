#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""
question = "Enter number:"
print(input(question))
TheNumberIsLargerThan100 = True
TheNumberIs100 = False
TheNumberIsLessThan100 = False

if TheNumberIsLargerThan100:
    print("The number is larger than 100")

if TheNumberIs100:
    print("The number is 100")

if TheNumberIsLessThan100:
    print("The number is less than 100")