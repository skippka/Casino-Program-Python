import random
from colorama import Fore, Back, Style


class PREFIX:
    CORRECT_PREFIX = Fore.GREEN + "[i] - " + Style.RESET_ALL
    INFO_PREFIX = Fore.BLUE + "[i] - " + Style.RESET_ALL
    WARN_PREFIX = Fore.YELLOW + "[i] - " + Style.RESET_ALL
    ERROR_PREFIX = Fore.RED + "[i] - " + Style.RESET_ALL


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("==============")
    print(" || ".join(row))
    print("==============")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("=========================")
    print("Welcome to Python Casino  ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("=========================")

    while balance > 0:
        print(PREFIX.INFO_PREFIX + f"Current balance: ${balance}")

        bet = input(PREFIX.INFO_PREFIX + "Place your bet amount: ")

        if not bet.isdigit():
            print(PREFIX.ERROR_PREFIX + "Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print(PREFIX.ERROR_PREFIX + "Insufficient funds")
            continue

        if bet <= 0:
            print(PREFIX.ERROR_PREFIX + "Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(PREFIX.CORRECT_PREFIX + f"You won ${payout}")
        else:
            print(PREFIX.INFO_PREFIX + "Sorry you lost this round")

        balance += payout

        play_again = input( "Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("===========================================")
    print(f"Game over! Your final balance is ${balance}")
    print("===========================================")

if __name__ == '__main__':
    main()
