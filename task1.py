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


question = "Enter a number:"
a = input(question)
a = float(a)

if a == 100:
    print("The number is 100")

if a < 100:
    print("The number is smaller than 100")

if a > 100:
    print("The number is bigger than 100")


