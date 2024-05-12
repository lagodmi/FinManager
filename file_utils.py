from datetime import datetime
import json


class Transaction:
    TRANSACTIONS_FILE = 'transaction.json'

    @classmethod
    def get_all_transaction(cls):
        """
        Получение всех транзакций.
        """
        try:
            with open(cls.TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
                transactions = json.load(f)
            return transactions
        except FileNotFoundError:
            return []

    @classmethod
    def set_transaction(cls, category, amount, description):
        """
        Добавление новой транзакции.
        """
        transactions = cls.get_all_transaction()

        new_transaction = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'category': category,
            'amount': amount,
            'description': description,
        }
        transactions.append(new_transaction)
        with open(cls.TRANSACTIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(transactions, f, indent=4, ensure_ascii=False)

    @classmethod
    def get_last_transaction(cls):
        """
        Получение последней транзакции.
        """
        transactions = cls.get_all_transaction()
        if transactions:
            return transactions[-1]
        else:
            return None

    @classmethod
    def get_transaction_by_category(cls, category):
        """
        Получение транзакций по категории.
        """
        transactions = cls.get_all_transaction()
        return [t for t in transactions if t['category'] == category]

    @classmethod
    def get_balance(cls):
        """
        Получение текущего остатка по счету.
        """
        balance: int = 0
        trans = cls.get_all_transaction()
        balance += sum(int(t['amount'])
                       if t['category'] == 'Доход'
                       else -int(t['amount'])
                       for t in trans)
        return balance

    @classmethod
    def update_transaction(cls, number_transaction,
                           category, amount, description, date):
        """
        Обновление транзакции.
        """
        all_transaction = cls.get_all_transaction()
        all_transaction[number_transaction] = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description,
        }

        with open(cls.TRANSACTIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_transaction, f, indent=4, ensure_ascii=False)


class ReportService:
    transaction = Transaction()

    def translation(word: str) -> str:
        """
        Перевод на русский.
        """
        translation_dict: dict = {
            'date': 'Дата',
            'category': 'Категория',
            'amount': 'Сумма',
            'description': 'Описание',
        }
        return translation_dict[word]

    @classmethod
    def get_report(cls):
        """
        Создание файлов отчетности.
        """
        report_dict: dict = {
            'report/all_transaction.txt': cls.transaction.get_all_transaction(),
            'report/deposit_transaction.txt': cls.transaction.get_transaction_by_category('Доход'),
            'report/spend_transaction.txt': cls.transaction.get_transaction_by_category('Расход'),
            'report/last_transaction.txt': [cls.transaction.get_last_transaction()],
        }
        for link, report in report_dict.items():
            all_result: str = ''
            for trans in report:
                for key, values in trans.items():
                    key = cls.translation(key)
                    all_result += key + ': ' + str(values) + '\n'
                all_result += '\n'

            with open(link, 'w', encoding='utf-8') as f:
                f.write(all_result)
