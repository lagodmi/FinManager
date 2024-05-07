from datetime import datetime

import strings as s
from file_utils import Transaction
import validators as valid

summa = 0


def get_category() -> str:
    """
    Обработка ввода категории.
    """
    CAT = {
        1: 'Доход',
        2: 'Расход'
    }

    while True:
        try:
            category = int(input(s.SELECT_CATEGORY))
            if category in (1, 2):
                return CAT[category]
            else:
                print(s.BAD_CATEGORY)
        except ValueError:
            print(s.BAD_CATEGORY)


def get_money(category: str) -> int:
    """
    Обработка ввода суммы.
    """
    # добавить обработчик исключений
    money: int
    if category == 'Доход':
        money = input(s.DEPOSIT_MONEY)
    else:
        money = -int(input(s.SPEND_MONY))
    return money


def get_description() -> str:
    """
    Обработка ввода описания.
    """
    return input(s.DESCRIPTION)


def main():
    flag: bool = True
    while flag:
        print(s.WELCOME_MESSAGE)
        current_category = get_category()
        current_money = get_money(current_category)
        current_description = get_description()
        Transaction.set_transaction(
            current_category,
            current_money,
            current_description
        )
        restart: int = input(s.RESTART)
        flag = restart != 1


if __name__ == "__main__":
    main()
