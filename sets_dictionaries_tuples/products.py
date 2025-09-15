from collections import Counter
from typing import List, Dict

PRODUCTS = [
    {"sku": "MUG-001", "name": "Logo mug",   "category": "drinkware", "price": 12.0},
    {"sku": "TEE-101", "name": "neon Tee",   "category": "apparel",   "price": 22.5},
    {"sku": "HAt-050", "name": "Dad Cap",    "category": "apparel",   "price": 18.0},
    {"sku": "STK-777", "name": "Sticker",    "category": "accessory", "price": 2.0},
    {"sku": "TEE-101", "name": "neon tee", "category": "Apparel", "price": 22.5},  
    {"sku": "MUG-002", "name": " Travel Mug ", "category": "Drinkware", "price": 16.0},
    {"sku": "BAG-010", "name": "Tote Bag", "category": "accessory", "price": 9.0}, 
    {"sku": "PIN-005", "name": "Enamel Pin", "category": "accessory", "price": 4.0}, 
]

def clean_record(product: dict) -> dict:
    """Return a cleaned product record."""
    name = str(product["name"]).strip().title()
    sku = str(product["sku"]).strip().upper()
    category = str(product["category"]).strip().lower()
    price = float(product["price"])
    return {"sku": sku, "name": name, "category": category, "price": price}

cleaned: List[Dict] = [clean_record(p) for p in PRODUCTS]

seen = set()
unique_products: List[Dict] = []
for product in cleaned:
    key = (product["sku"], product["name"], product["category"], product["price"])
    if key not in seen:
        seen.add(key)
        unique_products.append(product)

print("Cleaned, de-duplicated products:")
for product in unique_products:
    print(product)

unique_categories = {product["category"] for product in unique_products}
print("\nUnique categories:")
print({category for category in unique_categories})

counts = Counter(product["category"] for product in unique_products)
print ("\nProduct counts by category:")
for category in sorted(counts):
    print(f"{category}: {counts[category]}")

