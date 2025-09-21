import random
from typing import List, Dict, Tuple
from school_supplies import catalog

def build_shopping_cart(subset_size: int) -> List[Dict]:
    """
    Create a shopping_cart list by randomly selecting "subset_size" UNIQUE items from the catalog.

    Valid values for subset_size: 1..5 (inclusive).
    Raises:
        ValueError("Invalid subset size") for any invalid size.

    Returns:
        List[Dict]: each element is a catalog item dict that also includes its "id".
                    Example: {"id": 116, "name": "Index Cards", "category": "Paper", "price": 2.99}
    """
    if not isinstance(subset_size, int) or not (1 <= subset_size <= 5):
        raise ValueError("Invalid subset size")

    population: List[Tuple[int, Dict]] = list(catalog.items())

    chosen = random.sample(population, subset_size)

    cart: List[Dict] = [{"id": item_id, **info} for item_id, info in chosen]
    return cart

if __name__ == "__main__":
    random.seed(42) 

    print(f"build_shopping_cart(3) -> {build_shopping_cart(3)}")

    try:
        print(f"build_shopping_cart(0) -> {build_shopping_cart(0)}")
    except ValueError as e:
        print("Error:", e)

    print(f"build_shopping_cart(5) -> {build_shopping_cart(5)}")