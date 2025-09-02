from Bank import Bank, SavingsAccount, CurrentAccount, FixedDepositAccount

if __name__ == "__main__":
    bank = Bank()

    # Create accounts
    savings = SavingsAccount("S1001", "Alice", interest_rate=5.0, balance=1000.0)
    current = CurrentAccount("C1001", "Bob", overdraft_limit=500.0, balance=500.0)
    fixed_deposit = FixedDepositAccount("FD1001", "Charlie", amount=2000.0, interest_rate=6.5, lock_in_days=30)

    # Add to bank
    bank.add_account(savings)
    bank.add_account(current)
    bank.add_account(fixed_deposit)

    # Perform actions
    print("\n--- Savings Account ---")
    savings.deposit(200)
    savings.withdraw(150)
    savings.apply_interest()
    print(savings)

    print("\n--- Current Account ---")
    current.withdraw(900)  # Uses overdraft
    current.deposit(400)
    print(current)

    print("\n--- Fixed Deposit Account ---")
    try:
        fixed_deposit.withdraw(500)  # Should raise error due to lock-in period
    except Exception as e:
        print(f"Error: {e}")
    fixed_deposit.apply_interest()
    print(fixed_deposit)

    print("\n--- Fund Transfer ---")
    try:
        bank.transfer_funds("S1001", "C1001", 300)
    except Exception as e:
        print(f"Transfer failed: {e}")
    print(savings)
    print(current)
