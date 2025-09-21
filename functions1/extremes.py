from school_supplies import catalog

def extremes(category: str, extreme: str = "Highest") -> dict[int, dict]:
    """
    Return the single item (as {id: info_dict}) in the given category that has the highest (default) or lowest price. 

    Example expected by assignment:
    extremes("Paper", "Lowest") -> {116: {"name": "Index Cards", ... , "price": 2.99}}
    """
    category = category.strip()
    if extreme.lower() not in {"highest", "lowest"}:
        raise ValueError("extreme must be 'Highest' or 'Lowest'")
    
    filtered: list[tuple[int, dict]] = [
        (item_id, info)
        for item_id, info in catalog.items()
        if info["category"].lower() == category.lower()
    ]

    if not filtered:
        raise ValueError(f"No items found in category {category}")

    key_func = lambda pair: pair[1]["price"]
    if extreme.lower() == "lowest":
        chosen_id, chosen_info = min(filtered, key=key_func)
    else:
        chosen_id, chosen_info = max(filtered, key=key_func)

    return {chosen_id: chosen_info}

if __name__ == "__main__":
    print(f'extremes("Paper", "Lowest") -> {extremes("Paper", "Lowest")}')
    print(f'extremes("Paper", "Highest") -> {extremes("Paper", "Highest")}')
    print(f'extremes("Writing", "Highest") -> {extremes("Writing", "Highest")}')
    try:
        print(f'extremes("NotACategory", "Lowest") -> {extremes("NotACategory", "Lowest")}')
    except ValueError as e:
        print("Error:", e)

