from IO.console import *
from car import Car
from Configuration import config

__all__ = ['create_car', 'welcome_message']

CAR_MESSAGE = \
    f'''
Before creating a new car, notice the following:
Company must be one of: {config.CAR_COMPANIES},
Price must be a number bigger then 0,
and the Color must be one of: {config.CAR_COLORS}
'''


def welcome_message():
    output_to_user(CAR_MESSAGE)


def create_car():
    try:
        company = get_user_input("Enter car company: ")
        price = int(get_user_input("Enter car price: "))
        color = get_user_input("Enter car color: ")
        year = int(get_user_input("Enter car year: "))
        car = Car(company, price, color, year)
        output_to_user(car.__str__())
    except Exception as e:
        output_to_user(e.__str__())


