import strings as s
from file_utils import Transaction, ReportService


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
    deposit_amount: int

    while True:
        if category == 'Доход':
            try:
                deposit_amount = int(input(s.DEPOSIT_MONEY))
                if deposit_amount < 0:
                    print(s.INVALID_DEPOSIT_AMOUNT)
                    continue
                return deposit_amount
            except ValueError:
                print(s.INVALID_DEPOSIT_FORMAT)
                continue

        else:
            try:
                deposit_amount = int(input(s.SPEND_MONY))
                balance = Transaction.get_balance()
                if deposit_amount < 0:
                    print(s.INVALID_DEPOSIT_AMOUNT)
                    continue
                if balance - deposit_amount < 0:
                    print(s.INSUFFICIENT_FUNDS)
                    continue
                return deposit_amount
            except ValueError:
                print(s.INVALID_DEPOSIT_FORMAT)
                continue


def get_description() -> str:
    """
    Обработка ввода описания.
    """
    return input(s.DESCRIPTION)


def restart_report() -> str:
    """
    Формирование отчетности.
    """
    massage = input(s.SELECT_REPORT)
    report = ReportService()
    if massage == "2":
        report.get_report()
        print(s.RETURN_REPORT)
    return massage


def update() -> str:
    """
    Редактирование записи.
    """
    transactions: list[dict] = Transaction.get_all_transaction()
    counter = 1
    for transaction in transactions:
        print(f'Номер операции: {counter}')
        for key, val in transaction.items():
            key = ReportService.translation(key)
            print(f'{key}: {val}')
        print()
        counter += 1
    num_transaction: int = int(input(s.UPDATE_NUM_TRANSACTION)) - 1
    up_transaction = transactions[num_transaction]
    date: str = up_transaction['date']
    category: str = up_transaction['category']
    amount: int = up_transaction['amount']
    description: str = up_transaction['description']

    command: str = input(s.UPDATE_SELECT_KEY.format('Категорию', category))
    if command == '1':
        category = get_category()
    command: str = input(s.UPDATE_SELECT_KEY.format('Сумму', amount))
    if command == '1':
        amount = get_money(category)
    command: str = input(s.UPDATE_SELECT_KEY.format('Описание', description))
    if command == '1':
        description = get_description()

    Transaction.update_transaction(
        number_transaction=num_transaction,
        category=category,
        amount=amount,
        description=description,
        date=date
    )
    print(s.UPDATE_BAY)


def main():
    flag: bool = True
    while flag:
        try:
            print(s.WELCOME_MESSAGE)
            ddd = input('выбор 1 2')
            if ddd == '1':
                update()
            else:
                current_category = get_category()
                current_money = get_money(current_category)
                current_description = get_description()
                Transaction.set_transaction(
                    current_category,
                    current_money,
                    current_description
                )
            restart: str = restart_report()
            flag = restart == "1"
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            flag = False


if __name__ == "__main__":
    main()
