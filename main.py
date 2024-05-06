from datetime import datetime

import strings as s
import validators as valid

summa = 0


def get_category() -> int:
    """
    Обработка ввода категории.
    """
    while True:
        try:
            category = int(input(s.SELECT_CATEGORY))
            if category in (1, 2):
                return category
            else:
                print(s.BAD_CATEGORY)
        except ValueError:
            print(s.BAD_CATEGORY)


def get_money(category: int) -> int:
    """
    Обработка ввода суммы.
    """
    # добавить обработчик исключений
    money: int
    if category == 1:
        money = input(s.DEPOSIT_MONEY)
    else:
        money = -input(s.SPEND_MONY)
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
        current_date: datetime = datetime.now().strftime("%Y-%m-%d %A")
        current_description = get_description()
        restart: int = input(s.RESTART)
        flag = restart == 1

        # print(current_category,
        #       current_money,
        #       current_date,
        #       current_description,
        #       sep='\n')


if __name__ == "__main__":
    main()
