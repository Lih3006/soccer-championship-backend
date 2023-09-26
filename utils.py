from datetime import datetime, timedelta
from exceptions import *


def data_processing(data) -> None:
    first_cup = 1930
    last_cup_year = datetime.now().year
    test_range = range(first_cup, last_cup_year, 4)
    cup_year = data['first_cup']
    format_cup_year = datetime.strptime(cup_year, '%Y-%m-%d').year

    format_cup_year = datetime.strptime(data['first_cup'], '%Y-%m-%d').year
    last_cup_year = datetime.now().year
    confirm_years = format_cup_year+data['titles']*4
    if data['titles'] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    if format_cup_year not in test_range:
        raise InvalidYearCupError("there was no world cup this year")
    if last_cup_year < confirm_years:
        raise ImpossibleTitlesError(
                "impossible to have more titles than disputed cups")
