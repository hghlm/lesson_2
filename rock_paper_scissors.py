import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES_SHORT = ["r", "p", "sc", "l", "sp"]

WINNING_COMBOS = { "rock": ["scissors", "lizard"],
                   "paper": ["rock", "spock"],
                   "scissors": ["paper", "lizard"],
                   "lizard": ["spock", "paper"],
                   "spock": ["rock", "scissors"]}

SEPARATOR = '---------------------------------------------------------------'

# Print a formatted message.
def prompt(message):
    print(f"==> {message}")

# Takes choices for player and cpu and returns winner.
def determine_winner(player, cpu):
    if player == cpu:
        return 'tie'

    if cpu in WINNING_COMBOS[player]:
        return 'player'

    return 'cpu'

# Displays choices for player and computer and prints who wins.
def display_winner(player, cpu, winner):
    print()
    prompt(f"You chose {player}, computer chose {cpu}.")

    if winner == 'player':
        prompt(f"You win!\n{SEPARATOR}")
    elif winner == 'cpu':
        prompt(f"Computer wins!\n{SEPARATOR}")
    else:
        prompt(f"It's a tie!\n{SEPARATOR}")

# Displays welcome message.
def welcome_message():
    prompt("Let's play rock, paper, scissors, lizard, spock!")
    prompt("Best out of five!")
    print(SEPARATOR)

# Displays ending message.
def ending_message():
    prompt(f'The score is {score["player_score"]}:{score["cpu_score"]}.')

    if score["player_score"] > score["cpu_score"]:
        prompt('You won the match!\n')
    else:
        prompt('The computer won the match!\n')

# Ask for player choice input and returns it normalized.
def get_player_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)},')
    print(f'    or {", ".join (VALID_CHOICES_SHORT)} for short.')
    choice = input('--> ').strip().lower()

    while choice not in VALID_CHOICES and choice not in VALID_CHOICES_SHORT:
        prompt("That's not a valid choice")
        choice = input('--> ').strip().lower()

    return normalize_choice(choice)

# Takes short valid choice or valid choice input and returns valid choice.
def normalize_choice(choice):
    if choice not in VALID_CHOICES:
        index = VALID_CHOICES_SHORT.index(choice)
        choice = VALID_CHOICES[index]
    return choice

# Asks user to play again and returns their choice.
def play_again():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input('--> ').strip().lower()

        if answer in ['y', 'n']:
            break

    if answer[0] == 'y':
        prompt("Let's play again!\n")
        print(SEPARATOR)
        return True

    prompt("Thanks for playing!")
    return False

# Main program.
score = {"player_score": 0,
         "cpu_score": 0}

welcome_message()

while True:
    prompt(f'The score is {score["player_score"]}:{score["cpu_score"]}.\n')

    player_choice = get_player_choice()
    cpu_choice = random.choice(VALID_CHOICES)

    victor = determine_winner(player_choice, cpu_choice)
    display_winner(player_choice, cpu_choice, victor)

    if victor == 'player':
        score['player_score'] += 1
    elif victor == 'cpu':
        score['cpu_score'] += 1

    if score['player_score'] == 3 or score['cpu_score'] == 3:
        ending_message()
        score['player_score'] = 0
        score['cpu_score'] = 0

        if not play_again():
            break