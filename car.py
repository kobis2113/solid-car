from Validation.car_validation import *
from Validation.validation_utills import validate_field


class Car:
    def __init__(self, company: str, price: int, color: str, year: int):
        self.company = validate_field(validate_company, company.lower())
        self.price = validate_field(validate_price, price)
        self.color = validate_field(validate_color, color.lower())
        self.year = validate_field(validate_year, year)

    def __str__(self):
        return f'A {self.year} {self.color} {self.company} worth {self.price}'
