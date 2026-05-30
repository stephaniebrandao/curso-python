# ATM Simulation

# The user starts with a balance of 500€ and can withdraw money — in whole amounts — until the balance reaches zero or the account is closed.

balance = 500

while balance > 0:
    withdraw = int(input("Informe o valor do saque (ou digite 0 para sair): "))

    if withdraw == 0:
        break
    elif withdraw < 0:
        print("Invalide value! Type a positive number!")
    elif withdraw > balance:
        print("Insufficient funds! Withdrawal failed.")
    else:
        balance -= withdraw
        print(f"Withdrawal completed! New balance: {balance}€.")


print("Operation complete!")