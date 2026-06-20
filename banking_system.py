import datetime
import random
import sys

class BankAccount:
    def __init__(self, account_holder: str, initial_deposit: float):
        self.account_number = str(random.randint(100000, 999999))
        self.account_holder = account_holder
        self.balance = initial_deposit
        self.transaction_history = []
        self._add_to_ledger("Initial Deposit", initial_deposit, "CR")

    def _add_to_ledger(self, description: str, amount: float, transaction_type: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "description": description,
            "amount": amount,
            "type": transaction_type,
            "resulting_balance": self.balance
        }
        self.transaction_history.append(entry)

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("\nError: Deposit amount must be greater than zero.")
            return False
        
        self.balance += amount
        self._add_to_ledger("Cash Deposit", amount, "CR")
        print(f"\nSuccess: Deposited ₹{amount:,.2f}")
        print(f"Updated Balance: ₹{self.balance:,.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("\nError: Withdrawal amount must be greater than zero.")
            return False
        if amount > self.balance:
            print("\nError: Insufficient funds for this transaction.")
            print(f"Available Balance: ₹{self.balance:,.2f}")
            return False
        
        self.balance -= amount
        self._add_to_ledger("Cash Withdrawal", amount, "DR")
        print(f"\nSuccess: Withdrew ₹{amount:,.2f}")
        print(f"Updated Balance: ₹{self.balance:,.2f}")
        return True

    def display_balance(self):
        print("\n--- Account Balance Inquiry ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance:,.2f}")

    def generate_statement(self):
        print(f"\n--------------------------------------------------------")
        print(f"          ACCOUNT STATEMENT - {self.account_holder.upper()}          ")
        print(f"Account Number: {self.account_number}")
        print(f"Generated On:   {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"--------------------------------------------------------")
        print(f"{'Timestamp':<20} | {'Description':<20} | {'Type':<4} | {'Amount':<12} | {'Balance':<12}")
        print("-" * 78)
        
        for entry in self.transaction_history:
            amt_str = f"₹{entry['amount']:,.2f}"
            bal_str = f"₹{entry['resulting_balance']:,.2f}"
            print(f"{entry['timestamp']:<20} | {entry['description']:<20} | {entry['type']:<4} | {amt_str:<12} | {bal_str:<12}")
        
        print(f"--------------------------------------------------------")
        print(f"Final Settled Balance: ₹{self.balance:,.2f}\n")


class BankingSystemManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        print("\n--- Open a New Account ---")
        name = input("Enter the full name of the account holder: ").strip()
        if not name:
            print("Error: Name field cannot be left blank.")
            return

        try:
            initial_deposit = float(input("Enter initial deposit amount (Minimum ₹500): "))
            if initial_deposit < 500:
                print("Error: The minimum required deposit to open an account is ₹500.")
                return
        except ValueError:
            print("Error: Please enter a valid numerical value.")
            return

        new_account = BankAccount(name, initial_deposit)
        self.accounts[new_account.account_number] = new_account
        print(f"\nAccount successfully created for {name}.")
        print(f"Your designated Account Number is: {new_account.account_number}")

    def access_account(self):
        print("\n--- Access Account Dashboard ---")
        acc_num = input("Enter your 6-digit Account Number: ").strip()
        account = self.accounts.get(acc_num)

        if not account:
            print("Error: The provided account number could not be found.")
            return

        while True:
            print(f"\nWelcome back, {account.account_holder}")
            print("1. Deposit Funds")
            print("2. Withdraw Funds")
            print("3. Check Balance")
            print("4. Generate Statement")
            print("5. Log Out")
            
            choice = input("Please select an operation (1-5): ").strip()

            if choice == "1":
                try:
                    amt = float(input("Enter the amount to deposit: "))
                    account.deposit(amt)
                except ValueError:
                    print("Error: Invalid input. Please enter a number.")
            elif choice == "2":
                try:
                    amt = float(input("Enter the amount to withdraw: "))
                    account.withdraw(amt)
                except ValueError:
                    print("Error: Invalid input. Please enter a number.")
            elif choice == "3":
                account.display_balance()
            elif choice == "4":
                account.generate_statement()
            elif choice == "5":
                print("Securely logged out of your session.")
                break
            else:
                print("Error: Invalid selection. Please choose a valid option.")


def main():
    manager = BankingSystemManager()
    
    mock1 = BankAccount("Jayraj Sindhav", 25000.0)
    mock2 = BankAccount("Rahul Patel", 1200.0)
    manager.accounts[mock1.account_number] = mock1
    manager.accounts[mock2.account_number] = mock2

    print("=============================================")
    print("        CORE BANKING MANAGEMENT SYSTEM       ")
    print("=============================================")
    print(f"Note: Pre-loaded demo account for verification: {mock1.account_number} ({mock1.account_holder})")

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit System")
        
        main_choice = input("Please enter your choice (1-3): ").strip()

        if main_choice == "1":
            manager.create_account()
        elif main_choice == "2":
            manager.access_account()
        elif main_choice == "3":
            print("\nClosing core database pipelines safely. Goodbye.")
            sys.exit()
        else:
            print("Error: Unrecognized option. Please try again.")


if __name__ == "__main__":
    main()