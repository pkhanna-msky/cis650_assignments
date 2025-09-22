from typing import List, Dict, Any

def checkout(shopping_cart: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Ask the user for quantity of each item in the shopping_cart and compute:
      - extended price of each item (qty * original price)
      - discounted price of each item (qty * discounted unit price)
      - sum of extended prices
      - sum of discounted prices
      - total discount amount (difference)
    Returns a dictionary with per-line details and totals, and prints it.
    """
    results: Dict[str, Any] = {"items": []}
    sum_extended = 0.0
    sum_discounted = 0.0

    for line in shopping_cart:
        name = str(line["name"])
        unit_price = float(line["price"])
        unit_discounted = float(line.get("discounted_price", unit_price))  # default to original if missing

        # Read a non-negative integer quantity
        while True:
            raw = input(
                f'Enter quantity for {name} (unit: {unit_price:.2f}, discounted: {unit_discounted:.2f}): '
            ).strip()
            try:
                qty = int(raw)
                if qty < 0:
                    print("Quantity must be a non-negative integer. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a whole number (e.g., 0, 1, 2, ...).")

        extended = qty * unit_price
        extended_discounted = qty * unit_discounted

        sum_extended += extended
        sum_discounted += extended_discounted

        results["items"].append({
            "id": line.get("id"),
            "name": name,
            "qty": qty,
            "unit_price": round(unit_price, 2),
            "unit_discounted_price": round(unit_discounted, 2),
            "extended_price": round(extended, 2),
            "extended_discounted_price": round(extended_discounted, 2),
        })

    results["sum_extended"] = round(sum_extended, 2)
    results["sum_discounted"] = round(sum_discounted, 2)
    results["total_discount"] = round(sum_extended - sum_discounted, 2)

    print(results)
    return results


if __name__ == "__main__":
    # Minimal demo cart for screenshots (already includes discounted_price)
    demo_cart = [
        {"id": 102, "name": "Pen",      "category": "Writing", "price": 1.50, "discounted_price": 0.75},
        {"id": 101, "name": "Notebook", "category": "Paper",   "price": 3.99, "discounted_price": 3.99},
    ]
    checkout(demo_cart)
