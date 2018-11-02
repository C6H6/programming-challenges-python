import random


def get_choice():
    print("1. Rock\n2. Paper\n3. Scissors")
    try:
        choice = int(input("Choice: "))
        if 1 <= choice <= 3:
            return choice
        else:
            raise ValueError
    except ValueError:
        print("Invalid parameter")
        exit(255)


def get_winner(user, computer):
    if user == 1:
        if computer == 1:
            return 'Draw'
        elif computer == 2:
            return 'Computer wins'
        return 'You win'
    elif user == 2:
        if computer == 1:
            return 'You win'
        elif computer == 2:
            return 'Draw'
        return 'Computer wins'
    else:
        if computer == 1:
            return 'Computer wins'
        elif computer == 2:
            return 'You win'
        return 'Draw'


user_choice = get_choice()
computer_choice = random.randint(1, 3)

print("Result: " + get_winner(user_choice, computer_choice))
