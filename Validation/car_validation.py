# Outer project imports
from datetime import datetime
# Inner project imports
from Configuration import config

__all__ = [
    'validate_company',
    'validate_color',
    'validate_price',
    'validate_year'
]


def validate_company(company: str) -> bool:
    return company in config.CAR_COMPANIES


def validate_color(color: str) -> bool:
    return color in config.CAR_COLORS


def validate_year(year: int) -> bool:
    return config.MINIMUM_CAR_YEAR < year < datetime.today().year


def validate_price(price: int) -> bool:
    return price > 0
