#import random module
import random
correct_number = random.randint(1,100)
while True:
#Take input from user
        number = int(input("Enter a number:"))
#check number is too low
        if(number < correct_number):
               print("Number you guessed is too low!")
#check number is too high
        elif(number > correct_number):
               print("Number you guessed is too high")
#check number is correct
        else:
               print("Congratulations! you guessed the correct number 😊")
               break      