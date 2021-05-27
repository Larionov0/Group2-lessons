class Bank:
    def __init__(self, name, income, costs):
        self.name = name
        self.income = income
        self.costs = costs

    @property
    def money(self):
        return self.income - self.costs


b = Bank('Privat', 100_000, 80_000)

b.income += 10_000

print(b.money)
