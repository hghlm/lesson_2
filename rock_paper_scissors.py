import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES_SHORT = ["r", "p", "sc", "l", "sp"]

player_score = 0
cpu_score = 0

def prompt(message):
    print(f"==> {message}")
    
def determine_winner(player,cpu):
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
        return 'computer'

def display_winner(player, cpu):
    prompt(f"You chose {player}, computer chose {cpu}.")

    if ((player == "rock" and (cpu == "scissors" or cpu == "lizard")) or
        (player == "paper" and (cpu == "rock" or cpu == "spock")) or
        (player == "scissors" and (cpu == "paper" or cpu == "lizard")) or
        (player == "lizard" and (cpu == "spock" or cpu == "paper")) or 
        (player == "spock" and (cpu == "rock" or cpu == "scissors"))):
        prompt("You win!")
        global player_score 
        player_score += 1
    elif ((player == "rock" and cpu == "rock") or
        (player == "paper" and cpu == "paper") or
        (player == "scissors" and cpu == "scissors") or
        (player == "lizard" and cpu == "lizard") or 
        (player == "spock" and cpu == "spock")):
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")
        global cpu_score
        cpu_score += 1

def normalize_choice(choice):
    if choice not in VALID_CHOICES:
        index = VALID_CHOICES_SHORT.index(choice)
        choice = VALID_CHOICES[index]
    return choice
    
def display_score():
    prompt(f'The score is {player_score}:{cpu_score}.\n')

def ending_message():
    if player_score > cpu_score:
        prompt(f'You win!')
    else:
        prompt(f'Computer wins!')

play_again = True

prompt("Let's play rock, paper, scissors, lizard, spock!")
prompt("Best out of five!\n")

while play_again:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)},')
    print(f'    or {", ".join (VALID_CHOICES_SHORT)} for short.')
    choice = input()

    while choice not in (VALID_CHOICES and VALID_CHOICES_SHORT):
        prompt("That's not a valid choice")
        choice = input()

    choice = normalize_choice(choice)

    cpu_choice = random.choice(VALID_CHOICES)

    winner = display_winner(choice, cpu_choice)
    display_score()

    if player_score == 3 or cpu_score == 3:
        ending_message()
        player_score = 0
        cpu_score = 0
        
        while True:
            prompt("Do you want to play again (y/n)?")
            answer = input().lower()
    
            if answer.startswith('n') or answer.startswith('y'):
                break
    
        if answer[0] == 'n':
            prompt("Thanks for playing!")
            play_again = False
            
    