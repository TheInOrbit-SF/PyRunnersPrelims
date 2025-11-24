# Mini Banking App
____
A Python-based Mini Banking App that simulates basic banking operations for multiple users. Users can create new accounts, deposit, withdraw, and check balances. Perfect for learning file handling, classes, and user interaction in Python.

**Features**

- Supports 5+ user accounts (or more)
- Create new accounts with unique account numbers
- Deposit and withdraw money from accounts
- Check account balance
- Transaction history for each account
- Simple CLI or Tkinter GUI interface
- Persistent storage using files (optional)
___
**Requirements**

- Python 3.8+
- Built-in packages: os, json, or pickle for data storage
___
**Usage**

- Clone the repository
- Run the program
- Use menu options to:
- - Create a new account
  - Deposit money
  - Withdraw money
  - Check balance
  - View transaction history
___
**Configuration**

- Modify MAX_ACCOUNTS in config.py to increase the number of accounts
- Initial balance for new accounts can be set in config.py

**Example Interaction (CLI)**
___
```
Welcome to Mini Banking App
1. Create New Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

Select Option: 1
Enter Name: Alice
Account created successfully! Your Account Number: 101

Select Option: 2
Enter Account Number: 101
Enter Amount to Deposit: 5000
Deposit Successful! Current Balance: 5000

Select Option: 4
Enter Account Number: 101
Current Balance: 5000
```
___
**Skills Learned**

- Object-Oriented Programming (Accounts as classes)
- File handling and data persistence
- Input validation and error handling
- CLI or GUI application development
