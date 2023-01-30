import pyfiglet

"""
File: bills.py
Author: Christopher Reid
Description:
- Calculates Monthly Expenses (Customizable and Preset Options)
- Calculates Roommates Split Amount
- Calculates Net Monthly Savings
- Calculates Bills as % of Net Income
"""

CURRENT = {'rent': 1338.10,
           'cars': 155.18,
           'internet': 105.12,
           'cell': 80.00
           }

def bills_preset(curr_bills):
    """Bill presets current as of October 2022."""
    curr_bills['electricity'] = get_electricity_bill()
    Bills_PRESET(curr_bills)


def bills_custom():
    """Returns a dictionary of bills as determined by user input."""

    print('Input expense name and dollar amount (Sample Format: [ Rent 1100 ].')
    print('Enter "done" when finished.')
    print()
    bills = {}
    while True:
        try:
            bill_name, amount = input('Name & Amount: ').split()
        except ValueError:
            break
        bills[bill_name] = float(amount)
    print()
    Bills_CUSTOM(bills)


def display_title(current_bills):
    ascii_banner = pyfiglet.figlet_format("Bill Calculator")
    print(ascii_banner)
    print('CURRENT BILLS:')
    for name, amount in current_bills.items():
        print(f'{name}: ${amount}')
    print()
    print(' ____________________')
    print(' \ CHOOSE A COMMAND  \\')
    print('  \___________________\\')
    print()
    print('SET: Default preset bills (Current as of January 2023).')
    print('CUSTOM: Customize bill input.')
    print()


def split_bills(total):
    """Prints the amount based on the number of roommates. """
    roommates = float(input('How many roommates are splitting the bill?: '))
    if roommates <= 0:
        print("Sorry, please enter a positive non-zero integer.")
        print()
        split_bills(total)
    else:
        split = round((total / roommates), 2)
        return split


def resources():
    print('Here\'s a little book I wrote on personal finance. Hope you enjoy and learn! :)')
    phrase = 'Open this URL -> '
    print(phrase + 'https://drive.google.com/file/d/1BkpjseROzhfaKMPNRIojX3Mkw2d3PkZU/view?usp=share_link')
    print()


def get_electricity_bill():
    """Prompts user for electric bill due to variation."""
    return float(input('How much was the electric bill this month?: '))


class Bills_PRESET:
    def __init__(self, bills):
        """Passed preset values for bills as arguments."""
        self.bills = bills
        self.total = self.pretty_print()
        self.roommates = split_bills(self.total)
        print()
        print(f'BILL TOTAL: ${self.total}')
        print(f'ROOMMATE SHARE: ${self.roommates}.')
        print()
        self.financial_stats()

    def pretty_print(self):
        """Displays bills with total."""
        for name, amount in self.bills.items():
            print(f'{name}: ${amount}')
        total = round(sum(self.bills.values()), 2)
        print()
        return total

    def financial_stats(self):
        """Prints the relevant financial statistics for the month."""
        print('------------------------')
        print('USEFUL FINANCIAL STATS')
        print('------------------------')
        print()
        income = float(input('Estimate this month\'s NET income: '))
        print()

        # Calculate Net Savings
        savings = round(income - self.total)
        print(f'NET SAVINGS: ${savings}')
        print()

        # Calculate bills as % of total income
        print('INCOME PERCENTAGE:')
        for bill in self.bills:
            print(f'[{round((self.bills.get(bill) / income) * 100, 1)}%] = {bill}')
        print()

        # Resources
        print('RESOURCES:')
        resources()


class Bills_CUSTOM:
    def __init__(self, bills):
        """Passed a dictionary containing the bills as an argument."""
        self.bills = bills
        self.total = self.pretty_print()
        self.roommates = split_bills(self.total)
        print()
        print(f'BILL TOTAL: ${self.total}')
        print(f'ROOMMATE SHARE: ${self.roommates}.')
        print()
        self.financial_stats()

    def pretty_print(self):
        """Displays bills with total."""
        for name, amount in self.bills.items():
            print(f'{name}: ${amount}')
        total = round(sum(self.bills.values()), 2)
        print()
        return total

    def financial_stats(self):
        """Prints the relevant financial statistics for the month."""
        print('------------------------')
        print('USEFUL FINANCIAL STATS')
        print('------------------------')
        print()
        income = float(input('Estimate this month\'s NET income: '))
        print()

        # Calculate Net Savings
        savings = round(income - self.total)
        print(f'NET SAVINGS: ${savings}')
        print()

        # Calculate bills as % of total income
        print('INCOME PERCENTAGE:')
        for bill in self.bills:
            print(f'[{round((self.bills.get(bill) / income) * 100, 1)}%] = {bill}')
        print()

        # Resources
        print('RESOURCES:')
        resources()


def main(current):
    display_title(current)
    command = input('Enter a command: ')
    print()
    if command.upper() == 'SET':
        bills_preset(current)
    elif command.upper() == 'CUSTOM':
        bills_custom()

    again = input('Would you like to run this again? (Y/N): ')
    if again.upper() == 'Y':
        main()
    elif again.upper() == 'N':
        exit()


main(CURRENT)