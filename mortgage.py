def prompt(string):
    print (f'--> {string}')

def invalid_num(string):
    try:
        float(string)
        return float(string) <= 0
    except ValueError:
        return True

def invalid_month(string):
    try:
        int(string)
        return int(string) <= 0
    except ValueError:
        return True

def has_interest(char):
    if char and char[0] == 'y':
        return True
    return False

prompt("Welcome to Mortgage/Car Loan Calculator!\n")

while True:
    prompt("Enter loan amount (in dollars): ")

    while True:
        loan_amount = input()

        if not invalid_num(loan_amount):
            loan_amount = float(loan_amount)
            break

        prompt('Please enter a valid number greater than 0.')

    prompt("Does your loan have interest? (y/n)")
    interest = input()

    if has_interest(interest):
        prompt("Enter Annual Percentage Rate (in percentage): ")

        while True:
            apr = input()

            if not invalid_num(apr):
                apr = float(apr)
                break

            prompt('Please enter a valid percentage greater than 0.')

    prompt("Enter loan duration (in whole months): ")

    while True:
        monthly_loan_dur = input()

        if not invalid_month(monthly_loan_dur):
            monthly_loan_dur = int(monthly_loan_dur)
            break

        prompt('Please enter a valid integer greater than 0.')

    if has_interest(interest):
        monthly_int_rate = (apr / 100) / 12

        monthly_payment = loan_amount * (monthly_int_rate /
        (1 - (1 + monthly_int_rate) ** (-monthly_loan_dur)))
    else:
        monthly_payment = loan_amount / monthly_loan_dur

    prompt(f'The monthly payment is ${monthly_payment:.2f}.')

    prompt("Calculate again? (y/n)")
    again = input()

    if again and again[0] != 'y':
        prompt("Thanks for using my mortgage calculator!")
        break