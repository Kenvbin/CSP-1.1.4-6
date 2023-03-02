#   a114_divisible.py

# get two numbers from user
print ("Write your favorate number!")
num1 = int(input("Enter here: "))
print ("Write a number you HATE!")
num2 = int(input("Enter here: "))
# loop whle the numbers are not divisible (the remainder is 0)
while num1 % num2 != 0:
  print ("The remainder of the 2 numbers is more than 0 try again!")
  print ("Write your favorate number!")
  num1 = int(input("Enter here: "))
  print ("Write a number you HATE!")
  num2 = int(input("Enter here: "))
  # inform user of result 

  # gather user input again
  
# inform user of result 
if num1 % num2 == 0:
  print ("Congrats you input 2 numbers that have a remainder of 0!")