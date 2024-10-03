# bank-management-system
This project is part of the Samsung Innovation Campus Coding and Programming course,it developes a simple bank management system where users can create accounts, log in, and perform various banking operations such as depositing, withdrawing, transferring funds, and checking account balances.

Features:
User Authentication:
Users can create a new account or log in with an existing one using their ID and password.
The system provides warnings for incorrect login credentials or input errors.

Banking Operations:
Deposit: Users can deposit amounts in different currencies (USD, SAR, EGP), with automatic conversion to EGP.
Withdraw: Similar to deposits, withdrawals can be made in USD, SAR, or EGP, with conversion to EGP.
Transfer: Users can transfer money between accounts, with validation checks for account existence and sufficient balance.
Balance Check: Users can view their current balance and personal information.

Technical Details:
User information is stored in JSON format.
Currency Conversion rates: 1 USD = 30 EGP, 1 SAR = 9 EGP.
