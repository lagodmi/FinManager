import json
from datetime import datetime


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
        balance = cls.get_balance()

        new_transaction = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'category': category,
            'amount': amount,
            'description': description,
            'balance': balance + amount if category == 'Доход' else balance - amount
        }
        transactions.append(new_transaction)
        with open(cls.TRANSACTIONS_FILE, 'w') as f:
            json.dump(transactions, f, indent=4)

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
    def get_deposit_transaction(cls):
        """
        Получение транзакций зачисления.
        """
        transactions = cls.get_all_transaction()
        return [t for t in transactions if t['category'] == 'Доход']

    @classmethod
    def get_spend_transaction(cls):
        """
        Получение транзакций списания.
        """
        transactions = cls.get_all_transaction()
        return [t for t in transactions if t['category'] == 'Расход']

    @classmethod
    def get_balance(cls):
        """
        Получение текущего остатка по счету.
        """
        last_transaction = cls.get_last_transaction()
        if last_transaction:
            return last_transaction['balance']
        else:
            return 0
