import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES_SHORT = ["r", "p", "sc", "l", "sp"]

# Print a formatted message.
def prompt(message):
    print(f"==> {message}")

# Takes choices for player and cpu and returns winner.
def determine_winner(player, cpu):
    if ((player == "rock" and (cpu == "scissors" or cpu == "lizard")) or
        (player == "paper" and (cpu == "rock" or cpu == "spock")) or
        (player == "scissors" and (cpu == "paper" or cpu == "lizard")) or
        (player == "lizard" and (cpu == "spock" or cpu == "paper")) or 
        (player == "spock" and (cpu == "rock" or cpu == "scissors"))):
        return 'player'
    elif ((player == "rock" and cpu == "rock") or
        (player == "paper" and cpu == "paper") or
        (player == "scissors" and cpu == "scissors") or
        (player == "lizard" and cpu == "lizard") or 
        (player == "spock" and cpu == "spock")):
        return 'tie'
    else:
        return 'cpu'

# Displays choices for player and computer and prints who wins.
def display_winner(player, cpu, winner):
    prompt(f"You chose {player}, computer chose {cpu}.")

    if winner == 'player':
        prompt("You win!")
    elif winner == 'cpu':
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

# Increments the score of the winner by 1.        
def increment_score(winner):
    if winner == 'player':
        global player_score 
        player_score += 1
    elif winner == 'cpu':
        global cpu_score
        cpu_score += 1

# Takes short valid choice or valid choice input and returns valid choice.
def normalize_choice(choice):
    if choice not in VALID_CHOICES:
        index = VALID_CHOICES_SHORT.index(choice)
        choice = VALID_CHOICES[index]
    return choice

def welcome_message():
    prompt("Let's play rock, paper, scissors, lizard, spock!")
    prompt("Best out of five!\n")

# Displays best of three winner.
def ending_message():
    if player_score > cpu_score:
        prompt('You win!')
    else:
        prompt('Computer wins!')
        
# Ask for player choice input and returns it normalized.        
def get_player_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)},')
    print(f'    or {", ".join (VALID_CHOICES_SHORT)} for short.')
    choice = input().strip().lower()

    while choice not in VALID_CHOICES and choice not in VALID_CHOICES_SHORT:
        prompt("That's not a valid choice")
        choice = input().strip().lower()
    
    return normalize_choice(choice)

def play_again():
    while True:
            prompt("Do you want to play again (y/n)?")
            answer = input().strip().lower()
    
            if answer in ['y', 'n']:
                break
        
    if answer[0] == 'y':
        prompt("Let's play again!\n")
        return True
    else:
        prompt("Thanks for playing!")
        return False

# Main program.
player_score = 0
cpu_score = 0
rematch = True

welcome_message()

while rematch:
    player_choice = get_player_choice()
    cpu_choice = random.choice(VALID_CHOICES)

    winner = determine_winner(player_choice, cpu_choice)
    increment_score(winner)
    display_winner(player_choice, cpu_choice, winner)
    
    prompt(f'The score is {player_score}:{cpu_score}.\n')

    if player_score == 3 or cpu_score == 3:
        ending_message()
        player_score = 0
        cpu_score = 0
        
        rematch = play_again()