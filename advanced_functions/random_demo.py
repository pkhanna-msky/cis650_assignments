import random
from typing import List

def demo_randint():
    "Simulate rolling a six-sided die 10 times"
    rolls = [random.randint(1, 6) for _ in range(10)]
    print("randint(1,6) x10 ->", rolls)

def demo_choice():
    "Pick random tenants from a list multiple times."
    tenants = ["Alice", "Bob", "Charlie", "David", "Eva"]
    picks = [random.choice(tenants) for _ in range(5)]
    print("random.choice(tenants) x5 ->", picks)

if __name__ == "__main__":
    print("===random module demos ===")
    demo_randint()
    demo_choice()