# правильный ход программы
WELCOME_MESSAGE = "Добро пожаловать в ваш финансовый помощник!"
RESTART = "Хотите выйти:\n1. ДА\nили нажмите любую клавишу\n"
SELECT_CATEGORY = "Выберете категорию:\n1. доход\n2. расход\n"
DEPOSIT_MONEY = "Введите сумму дохода:\n"
SPEND_MONY = "Введите сумму расхода:\n"
DESCRIPTION = "Введите описание:\n"
SELECT_REPORT = """
1. Внести еще транзакцию
2. Получить выписку в файлах txt и выйти
Нажмите любую клавишу чтобы выйти без выписки
"""
RETURN_REPORT = """
файлы отчета в папке report:
all_transaction.txt - полная отчетность
deposit_transaction.txt - поступления
spend_transaction.txt - списание
last_transaction.txt - последняя транзакция
balance.txt - баланс
"""

# ошибки
REPEAT_INPUT = "попробуй еще раз"

BAD_CATEGORY = "Ooops такой категории нет но мы обязательно ее добавим))"

INVALID_DEPOSIT_AMOUNT = "Ошибка: сумма должна быть положительной"
INVALID_DEPOSIT_FORMAT = "Ошибка: введите цифры от 0 до 9"
INSUFFICIENT_FUNDS = "Ошибка: недостаточно средств на балансе"
