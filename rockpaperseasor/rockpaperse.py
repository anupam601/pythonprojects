

import random 

print('Welcome to Rock, Paper, Scissors!') 

userChoice = input('Enter your choice (rock/paper/scissors): ')
compChoice = random.choice(['rock', 'paper', 'scissors']) 

if userChoice == 'rock': 
    if compChoice == 'rock':
        print("It's a draw! Both choices were rock")
    elif compChoice == 'paper': 
        print("Computer wins! Paper beats rock") 
    else: 
        print("You win! Rock beats scissors") 
        
elif userChoice == 'paper' : 
    if compChoice == 'rock': 
        print("You win! Paper beats rock") 
    elif compChoice == 'paper': 
        print("It's a draw! Both choices were paper")
    else: 
        print("Computer wins! Scissors beats paper") 
        
elif userChoice == 'scissors' :
    if compChoice == 'rock': 
        print("Computer wins! Rock beats scissors") 
    elif compChoice =='paper': 
        print("You win! Scissors beats paper")
    else: 
        print("It's a draw! Both choices were scissors")
        
else: 
    print("Invalid input. Please try again.")