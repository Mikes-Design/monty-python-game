# This is an introduction to the game
print("Welcome to the Monty Python Adventure!\nYou are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")
# this takes an input from the user and stores it in player_name and welcomes them 
player_name = input("What is your name, brave adventurer?\n")
print(f"Welcome, Sir {player_name} of Pythonia!")
#prints a statement and stores the input in the variable choice
print('A Knight steps in front of you and says, "None shall pass!"')

fight_the_knight = "1"
try_to_reason = "2"

choice = input("Do you (1) fight the Knight, or (2) try to reason with him?\n")

# this is a conditional statement that checks the value of choice and prints a different message depending on the value of choice
if choice == fight_the_knight:
    print("You draw your sword and prepare for battle!")
    print("The Knight attacks you with a swift strike!")
    print("You bravely fight, but the Knight is too strong.")
    print("You have been defeated. Game over.")
    exit()

elif choice == try_to_reason:
    print("You attempt to reason with the Knight.")
    print('You say, "Please, we mean no harm. We are on a quest for the Holy Grail."')
    print("The Knight pauses, considering your words.")
    print('He says, "If you can answer my riddle, I will let you pass."')
    print('The Knight asks, "How many woods could a woodchuck chuck if a woodchuck could chuck wood?"')
    
    # this takes an input from the user and stores it in riddle_answer
    riddle_answer = input("What is your answer?\n")

    print("The Knight says Hah, I can't believe you tried to answer that! I't does not matter if I kill you now or not you shall die from stupidity.")
    print("The Knight lets you pass.")
# this creates a loop that asks for input then prints a statment and breaks out of the loop
while True: 
    choice = input("Do you want to cross the Bridge of Death? (yes/no)\n").lower()

    if choice == "yes":
        print("A troll appears and asks you three questions!")
        break
    elif choice == "no":
        print("You wisely turn back.")
        break
    else:
        print("Please answer 'Yes' or 'No'.")
    
# A print statment that congragulates the player and states the player name from the input ealier that asks player name and stores it into the variable player_name
print(f"Congratulations, you have completed your quest!\nFarewell, Sir {player_name}!")