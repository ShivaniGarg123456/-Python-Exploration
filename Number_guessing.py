import random                                                           #import random module to generate a random number
correct_number = random.randint(1,100)        #storing random number in a variable 
while True:                                                             #loop condition till user will not enter correct number
    number  = int(input("Enter a number(1-100):"))                                         #user input a number  
    if(number < correct_number ):                            #condition if number input is low
        print("number is too low!")
    elif(number > correct_number):                                #condition if number input is high
        print("number is too high!")
    else:                  #if user input a correct number
        print("congratulations! you guess the correct number") 
        break                                                      #loop will exit if user enetred a correct number
    
    play_again = print("Do you want to play again?(types yes/No)") .strip() .lower()
    if(play_again!= yes):
        print("Thanks for playing!!!")
        break    
