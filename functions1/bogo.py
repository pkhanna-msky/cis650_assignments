from typing import List, Dict

def BOGO_deal(shopping_cart: List[Dict], name: str, discount_percent: float = 50.0) -> List[Dict]:
    """
    Apply a Buy-One-Get-One deal to items in shopping_cart that match "name" (case-insensitive).
    Every second occurrence (2nd, 4th, 6th, ...) of that item gets a discounted unit price.
    Non-matching items (and non-discounted matches) keep the original price.

    Side effect: add/overwrite "discounted_price" on each cart line.
    Returns the same list (so you can pass it straight into Task 4).
    """
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")

    target = name.strip().lower()
    seen = 0

    for line in shopping_cart:
        unit_price = float(line["price"])
        if line["name"].strip().lower() == target:
            seen += 1
            if seen % 2 == 0:
                discounted = round(unit_price * (1.0 - discount_percent / 100.0), 2)
            else:
                line["discounted_price"] = unit_price
        else:
            line["discounted_price"] = unit_price

        line["discounted_price"] = discounted

    
    return shopping_cart
    

if __name__ == "__main__":

    cart_a = [
        {"id": 101, "name": "Notebook", "category": "Paper", "price": 3.99},
        {"id": 101, "name": "Pen", "category": "Writing", "price": 1.50},
        {"id": 102, "name": "Pencil", "category": "Writing", "price": 0.75},
        {"id": 104, "name": "Eraser", "category": "Correction", "price": 0.99},
    ]
    print("Before (A):", cart_a)
    BOGO_deal(cart_a, "Pen")
    print("After (A, 50% on Pen):", cart_a)

    
    cart_b = [
        {"id": 101, "name": "Pen", "category": "Writing", "price": 1.50},
        {"id": 102, "name": "Pen", "category": "Writing", "price": 1.50},
        {"id": 101, "name": "Notebook", "category": "Paper", "price": 3.99},
        {"id": 102, "name": "Pen", "category": "Writing", "price": 1.50},
    ]
    print("Before (B):", cart_b)
    BOGO_deal(cart_b, "Pen", discount_percentage=30)
    print("After (B, 30% on Pen):", cart_b)