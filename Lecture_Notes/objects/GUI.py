
import tkinter as tk
from account import Account, Savings
from tkinter import simpledialog

class AccountGUI:
    def __init__(self, root):
        self.root = root
        
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(side="top")
        
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(side="top")
        
        self.accounts = [] 
        self.selected_account = None
        
        self.balance_label = tk.Label(self.frame1, text="Balance: ")
        self.balance_label.pack(side="left", anchor="n")
        
        self.account_owner_label = tk.Label(self.frame1, text="Account Owner: ")
        self.account_owner_label.pack(side="left", anchor="n")
        
        self.account_number_label = tk.Label(self.frame1, text="Account Number: ")
        self.account_number_label.pack(side="left", anchor="n")
        
        self.deposit_button = tk.Button(self.frame2, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side="left")
        
        self.withdraw_button = tk.Button(self.frame2, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(side="left")
        
        self.create_account_button = tk.Button(self.frame2, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

    def deposit(self):
        pass
    
    def withdraw(self):
        pass
    
    def display_account(self):
        pass
    
    def create_account(self):
        account_number = simpledialog.askstring("Enter Acc Num", "Enter")
        account_owner = simpledialog.askstring("enter own", "Enter own")
        account_balance = simpledialog.askfloat("Enter bal", "Enter bal")
        if account_number and account_owner and account_balance is not None:
            interest_rate = simpledialog.askfloat("Enter interest", "Enter interest")
            if interest_rate is not None:
                if interest_rate == 0:
                    account = Account( account_number, account_owner, account_balance )
                else:
                    account = Savings( account_number, account_owner, account_balance , interest_rate)
                self.accounts.append(account)
                self.selected_account = account

if __name__ == '__main__':
    # create a window
    root = tk.Tk()
    # set the dimensions of the window
    root.geometry("500x400")

    root.title("Banking Application")
    app = AccountGUI(root)
    # establish persistent window
    root.mainloop()

