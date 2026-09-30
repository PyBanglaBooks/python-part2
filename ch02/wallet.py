class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} Taka.")

    def send(self, other, amount):
        if amount > self.balance:
            print(f"Sorry {self.owner}, not enough balance.")
            return
        self.balance -= amount
        other.balance += amount
        print(f"{self.owner} sent {amount} Taka to {other.owner}.")

    def show(self):
        print(f"{self.owner}: {self.balance} Taka")


rahim = Wallet("Rahim", 500)
karim = Wallet("Karim")
rahim.send(karim, 200)
karim.send(rahim, 1000)
karim.deposit(300)
rahim.show()
karim.show()
