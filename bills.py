"""
File: bills.py
Author: Christopher Reid
Description:
- Calculates Monthly Expenses (Customizable and Preset Options)
- Calculates Net Monthly Savings
- Calculates Bills as % of Net Income
- Calculates Roommates Split Amount
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
    print(' ______________________ ')
    print('|                      |')
    print('|       COMMANDS       |')
    print('|______________________|')
    print('SET: Default preset bills (Current as of October 2022).')
    print('CUSTOM: Customize bill input.')
    print(' _______________________________ ')


def bills_preset():
    """Bill presets current as of October 2022."""
    rent = 1338.10
    cars = 108.98
    internet = 102.05
    cell = 80.00
    Bills_PRESET(rent, cars, internet, cell)


def bills_custom():
    """Returns a dictionary of bills as determined by user input."""

    bills = {'rent': 0, 'car insurance': 0, 'internet': 0, 'cell phone': 0}
    for expense in bills:
        bills[expense] = float(input(f'How much was the {expense} bill this month?: '))
    Bills_CUSTOM(bills)


class Bills_PRESET:
    def __init__(self, rent, cars, internet, cell):
        """Passed preset values for bills as arguments."""
        self.rent = rent
        self.cars = cars
        self.internet = internet
        self.cell = cell
        self.electricity = self.set_electricity()

        self.bills = {
            'Rent': self.rent,
            'Car Insurance': self.cars,
            'Internet': self.internet,
            'Cell Phone': self.cell,
            'Electricity': self.electricity
        }
        self.bills_list()
        self.print_total()

    def set_electricity(self):
        """Prompts user for electric bill because it can vary."""
        return float(input('How much was the electric bill this month?: '))

    def bills_list(self):
        """Prints each bill from the dictionary."""
        # Pretty Print Bills
        for name, amount in self.bills.items():
            print('________________________')
            print(f'{name}: ${amount}')
        print('________________________')

    def print_total(self):
        """Prints the total for the month."""
        total = 0

        for amount in self.bills.values():
            total += amount
        print(f'The total amount for this month is: ${round(total, 2)}')
        print()
        income = float(input('Estimate this month\'s NET income: '))
        print()

        # Calculate Net Savings
        print(f'You should have ${round(income - total)} leftover after expenses. ')
        if income - total < 0:
            print('Advice: You need to go on a budget.')
            answer = input('...Want some advice on how to get rich? :) (Y/N): ')
            if answer.upper() == 'Y':
                print('Some resources...')
                phrase = 'Click this URL -> '
                print(phrase + 'https://en.wikipedia.org/wiki/Millionaire')
                print(phrase + 'https://en.wikipedia.org/wiki/The_Total_Money_Makeover ')
                print(phrase + 'https://en.wikipedia.org/wiki/The_Millionaire_Next_Door')
                print(phrase + 'https://en.wikipedia.org/wiki/Bad_debt')
                print(phrase + 'https://en.wikipedia.org/wiki/Debt')
            elif answer.upper() == 'N':
                print('Fine :) Your loss. ')
        else:
            print('Advice: Learn about Investing.')
            print('Some resources...')
            phrase = 'Click this URL -> '
            print(phrase + 'https://en.wikipedia.org/wiki/Inflation')
            print(phrase + 'https://en.wikipedia.org/wiki/The_Total_Money_Makeover ')
            print(phrase + 'https://en.wikipedia.org/wiki/S%26P_500')
            print(phrase + 'https://en.wikipedia.org/wiki/John_C._Bogle')
            print(phrase + 'https://en.wikipedia.org/wiki/Dollar_cost_averaging')
            print(phrase + 'https://jlcollinsnh.com/')
        print()

        # Calculate bills as % of total income
        for bill in self.bills:
            print(f'The {bill} bill is [{round((self.bills.get(bill) / income) * 100, 1)}%] of your income estimate.')
        print()

        self.split_bills(total)

    def split_bills(self, total):
        """Prints the amount based on the number of roommates. """
        roommates = float(input('How many roommates are splitting the bill?: '))
        print()
        split = round((total / roommates), 2)
        print(f'This month\'s roommate share: ${split}.')
        print()


class Bills_CUSTOM:
    def __init__(self, bills):
        """Passed a dictionary containing the bills as an argument."""
        self.bills = bills
        self.bills['electricity'] = self.set_electricity()

        self.bills_list()
        self.print_total()

    def set_electricity(self):
        """Prompts user for electric bill because it can vary."""
        return float(input('How much was the electric bill this month?: '))

    def bills_list(self):
        """Prints each bill from the dictionary."""
        # Pretty Print Bills
        for name, amount in self.bills.items():
            print('________________________')
            print(f'{name}: ${amount}')
        print('________________________')

    def print_total(self):
        """Prints the total for the month."""
        total = 0

        for amount in self.bills.values():
            total += amount
        print(f'The total amount for this month is: ${round(total, 2)}')
        print()
        income = float(input('Estimate this month\'s NET income: '))
        print()

        # Calculate Net Savings
        print(f'You should have ${round(income - total)} leftover after expenses. ')
        if income - total < 0:
            print('Advice: You need to go on a budget.')
            print('Some resources...')
            phrase = 'Click this URL -> '
            print(phrase + 'https://en.wikipedia.org/wiki/Millionaire')
            print(phrase + 'https://en.wikipedia.org/wiki/The_Total_Money_Makeover ')
            print(phrase + 'https://en.wikipedia.org/wiki/The_Millionaire_Next_Door')
            print(phrase + 'https://en.wikipedia.org/wiki/Bad_debt')
            print(phrase + 'https://en.wikipedia.org/wiki/Debt')
        else:
            print('Learn about investing.')
            print('Some resources...')
            phrase = 'Click this URL -> '
            print(phrase + 'https://en.wikipedia.org/wiki/Inflation')
            print(phrase + 'https://en.wikipedia.org/wiki/The_Total_Money_Makeover ')
            print(phrase + 'https://en.wikipedia.org/wiki/S%26P_500')
            print(phrase + 'https://en.wikipedia.org/wiki/John_C._Bogle')
            print(phrase + 'https://en.wikipedia.org/wiki/Dollar_cost_averaging')
            print(phrase + 'https://jlcollinsnh.com/')
        print()

        # Calculate bills as % of total income
        for bill in self.bills:
            print(f'The {bill} bill is [{round((self.bills.get(bill) / income) * 100, 1)}%] of your income estimate.')
        print()

        self.split_bills(total)

    def split_bills(self, total):
        """Prints the amount based on the number of roommates. """
        roommates = float(input('How many roommates are splitting the bill?: '))
        print()
        split = round((total / roommates), 2)
        print(f'This month\'s roommate share: ${split}.')
        print()


main()