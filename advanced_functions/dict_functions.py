from typing import Callable, Dict

customers: Dict[str, dict] = {} 

def add_customer() -> None:
    name = input("Enter customer name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in customers:
        print(f"Customer '{name}' already exists.")
        return
    customers[name] = {"balance": 0.0, "payments": []}
    print(f"Added customer '{name}'")

def charge_rent() -> None:
    name = input("Enter customer name: ").strip()
    if name not in customers:
        print("Customer not found.")
        return
    try:
        rent = float(input("Enter rent amount: ").strip())
        if rent <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    customers[name]["balance"] += rent
    print(f"Charged ${rent:.2f} to {name}. New balance: ${customers[name]['balance']:.2f}")

def record_payment() -> None:
    name = input("Enter customer name: ").strip()
    if name not in customers:
        print("Customer not found.")
        return
    try:
        payment = float(input("Enter payment amount: ").strip())
        if payment <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    customers[name]["balance"] -= payment
    customers[name]["payments"].append(payment)
    print(f"Recorded payment of ${payment:.2f} for {name}. New balance: ${customers[name]['balance']:.2f}")

def view_balance() -> None:
    name = input("Enter customer name: ").strip()
    if name not in customers:
        print("Customer not found.")
        return
    balance = customers[name]["balance"]
    print(f"{name}'s current balance: ${balance:.2f}")

def list_customers() -> None:
    if not customers:
        print("No customers found.")
        return
    print("\n-- Customers --")
    for name, info in customers.items():
        balance = info["balance"]
        payments = info["payments"]
        print(f"- {name}: Balance=${balance:.2f}, Payments={payments}")

def quit_app() -> None:
    print("Exiting application.")
    raise SystemExit

def invalid_choice() -> None:
    print("Invalid choice. Please try again.")


ACTIONS: Dict[str, Callable[[], None]] = {
    "1": add_customer,
    "2": charge_rent,
    "3": record_payment,
    "4": view_balance,
    "5": list_customers,
    "q": quit_app,
}

def main() -> None:
    while True:
        print("\nCustomer Management System")
        print("1. Add Customer")
        print("2. Charge Rent")
        print("3. Record Payment")
        print("4. View Balance")
        print("5. List Customers")
        print("q. Quit")
        choice = input("Choose an action: ").strip().lower()
        action = ACTIONS.get(choice, invalid_choice)  
        action()  

if __name__ == "__main__":
    main()
