import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, initial_balance=500):  #initial balance as Rs 500
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Rs {amount}. New balance: Rs {self.balance}."
        else:
            return "Invalid amount entered!."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Rs {amount}. New balance: Rs {self.balance}."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid amount entered!."

class ATMApp:
    def __init__(self, root):
        self.atm = ATM()
        self.root = root
        self.root.title("JTK ATM")

        self.root.geometry("350x300")
        self.balance_label = tk.Label(root, text="Welcome to JTK Bank", font=("Inter", 16,"bold"))
        self.balance_label.pack(pady=15)

        self.deposit_label = tk.Label(root, text="Deposit Amount:",font=("Inter",12))
        self.deposit_label.pack()
        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(root, text="Deposit",font=("Inter",10), command=self.deposit)
        self.deposit_button.pack(pady=10)

        self.withdraw_label = tk.Label(root, text="Withdraw Amount:",font=("Inter",12))
        self.withdraw_label.pack()
        self.withdraw_entry = tk.Entry(root)
        self.withdraw_entry.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw",font=("Inter",10), command=self.withdraw)
        self.withdraw_button.pack(pady=10)

        self.check_balance_button = tk.Button(root, text="Check Balance",font=("Inter",10), command=self.check_balance)
        self.check_balance_button.pack(pady=15)

    def deposit(self):
        try:
            amount = float(self.deposit_entry.get())
            message = self.atm.deposit(amount)
            messagebox.showinfo("Deposit", message)
            self.update_balance()
        except ValueError:
            messagebox.showerror("Error!", "Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(self.withdraw_entry.get())
            message = self.atm.withdraw(amount)
            messagebox.showinfo("Withdraw", message)
            self.update_balance()
        except ValueError:
            messagebox.showerror("Error!", "Please enter a valid amount.")

    def check_balance(self):
        balance = self.atm.check_balance()
        messagebox.showinfo("Balance", f"Your balance is: Rs {balance}")


    def update_balance(self):
        balance = self.atm.check_balance()
        self.balance_label.config(text=f"Balance: Rs {balance}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
