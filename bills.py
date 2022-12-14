"""
File: bills.py
Author: Christopher Reid
Description:
- Calculates Monthly Expenses (Customizable and Preset Options)
- Calculates Roommates Split Amount
- Calculates Net Monthly Savings
- Calculates Bills as % of Net Income
"""


def main():
    header()
    command = input('Enter a command: ')
    print()
    if command.upper() == 'SET':
        bills_preset()
    elif command.upper() == 'CUSTOM':
        bills_custom()

    again = input('Would you like to run this again? (Y/N): ')
    if again.upper() == 'Y':
        main()
    elif again.upper() == 'N':
        exit()


def header():
    print(' ____  _ _ _    _____      _            _       _             ')
    print('|  _ \(_) | |  / ____|    | |          | |     | |            ')
    print('| |_) |_| | | | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ')
    print('|  _ <| | | | | |    / _` | |/ __| | | | |/ _` | __/ _ \| \'__|')
    print('| |_) | | | | | |___| (_| | | (__| |_| | | (_| | || (_) | |   ')
    print('|____/|_|_|_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ')
    print()
    print('| CHOOSE A COMMAND |')
    print('|__________________|')
    print()
    print('SET: Default preset bills (Current as of January 2023).')
    print('CUSTOM: Customize bill input.')
    print()


def bills_preset():
    """Bill presets current as of October 2022."""
    bills = {'rent': 1338.10,
             'cars': 108.98,
             'internet': 105.12,
             'cell': 80.00,
             'electricity': get_electricity_bill()
             }
    Bills_PRESET(bills)


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


def resources(savings):
    phrase = 'Open this URL -> '
    if savings < 0:
        print(phrase + 'https://en.wikipedia.org/wiki/Millionaire')
        print(phrase + 'https://en.wikipedia.org/wiki/The_Total_Money_Makeover ')
        print(phrase + 'https://en.wikipedia.org/wiki/The_Millionaire_Next_Door')
        print(phrase + 'https://en.wikipedia.org/wiki/Bad_debt')
        print(phrase + 'https://en.wikipedia.org/wiki/Debt')
    else:
        print(phrase + 'https://en.wikipedia.org/wiki/Inflation')
        print(phrase + 'https://en.wikipedia.org/wiki/The_Total_Money_Makeover ')
        print(phrase + 'https://en.wikipedia.org/wiki/S%26P_500')
        print(phrase + 'https://en.wikipedia.org/wiki/John_C._Bogle')
        print(phrase + 'https://en.wikipedia.org/wiki/Dollar_cost_averaging')
        print(phrase + 'https://jlcollinsnh.com/')
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
        resources(savings)


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
        resources(savings)


main()
