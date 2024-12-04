# This is used to import the function into this code.
from random import choice

# These 3 prints are here to give directions for the user who is doing the RPS like game.
print("Welcome to the arena, this is a life or death battle!")

print("You have three options, you can turn into Rubber, you can get electric powers, or wield a sword.")

print("But choose wisely. The other opponent can do the same thing")

# This is for the user to input if they want to continue the game or quit.
retry = input("Would you like to continue? (y/n): ")

# This is the while loop and it will loop the code until at the end if you put "n". Once the code sees "n", it will end the code.
while retry != "n":

    # This is the attack variable so it can be defined for the next while loop.
    attack = ("Choose your weapon! (Rubber, Electricity, or Sword): ")

    # This is the second while loop. This is used so that in case you clicked the wrong button, the code wouldn't keep going and it will reset to where you choose your weapon.
    while attack != "":

        # This is where you input your weapon
        attack = input("Choose your weapon! (r,e,s): ")
        # This makes a new variable and that new variable lowercases the input from the "attack" variable.
        low_attack = attack.lower()
        
        # These conditional statements are here so if the user chooses another option other than the 3 provided, it will reset the code.
        # If you do choose one of the 3 options, it will print out a phrase and it will break the loop.
        if low_attack == "r":
            print("Your body turns rubber!")
            break
        elif low_attack == "e":
            print("You feel a surge of electricity going through your body!")
            break
        elif low_attack == "s":
            print("You wield your sword!")
            break
        else:
            print("Error, chose the 3 options from the top")
        

    # This prints the following string.
    print("Opponets turn!")
    
    # This is a list for the other opponent.
    rivals_attack = ["r", "e", "s"]
    
    # Once you import the function, you can have the random "choice" option.
    # The random "choice" option chooses the list from the variable you specified (in this case it will be rivals attack), and makes a new variable with that string.
    rivals_decision = choice(rivals_attack)

    # These conditional statements will print out when the opponent choose the 3 strings randomly
    if rivals_decision == "r":
        print("Your opponent throws his rubbary fists!")
    elif rivals_decision == "e":
        print("Your opponent shoots an electrical current!")
    elif rivals_decision == "s":
        print("Your opponent swings his sword!")

    # All of these conditional statements are the different scenerios that will happen when certain combinations happens.
    if rivals_decision == "r" > low_attack == "e":
        print("Your opponent resisted your electricity and knocked you out! You Lose!")
    elif rivals_decision == "r" < low_attack == "s":
        print("You slash the your opponent in half! You Win!")
    elif rivals_decision == "r" == low_attack == "r":
        print("You both hit each others rubber bodies, it seems to have no effect! You tied!")
    elif rivals_decision == "e" == low_attack == "e":
        print("You both electrify yourselves to no avail! You tied!")
    elif low_attack == "s" > rivals_decision == "e":
        print("Your sword gets conducted with elctricity! You Lose!")
    elif rivals_decision == "e" < low_attack == "r":
        print("You resisted the electricity and knocked your opponent out! You Win!")
    elif rivals_decision == "s" > low_attack == "e":
        print("You electricity conducted your opponents sword! You Win!")
    elif rivals_decision == "s" == low_attack == "s":
        print("You both clash swords and defend perfectly! You tied!")
    elif rivals_decision == "s" > low_attack == "r":
        print("Your rubber body gets sliced in half! You Lose!")

    # This is here so if you want to play again, you type "y", or leave the game, you type "n"
    retry = input("Would you like to continue? (y/n): ")