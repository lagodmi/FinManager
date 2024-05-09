import json


class Model_Transaction:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"""
                Date: {self.date},
                Category: {self.category},
                Amount: {self.amount},
                Description: {self.description}
                """

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

    def to_json(self):
        return json.dumps(self.to_dict())
