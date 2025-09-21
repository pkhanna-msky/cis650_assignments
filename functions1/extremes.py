from school_supplies import catalog

def extremes(category: str, extreme: str = "Highest") -> dict[int, dict]:
    """
    Return the single item (as {id: info_dict}) inm the given category that has the highest (default) or lowest price. 

    Example expected by assignment:
    >>> extremes("Paper", "Lowest") -> {116: {"name": "Index Cards", ... , "price": 2.99}}
    """

    filtered: list[tuple[int, dict]] = [
        (item_id, info)
        for item_id, info in catalog.items()
        if info["category"].lower() == category.lower()
    ]

    if not filtered:
        raise ValueError(f"No items found in category {category}")

    key_func = lambda pair: pair[1]["price"]
    if extreme.lower() == "lowest":
        choose_id, chosen_info = min(filtered, key=key_func)
    else:
        choose_id, chosen_info = max(filtered, key=key_func)

    return {choose_id: chosen_info}

if __name__ == "__main__":
    print(extremes("Paper", "Lowest"))
    print(extremes("Paper", "Highest"))
    print(extremes("Writing", "Highest"))
    try:
        print(extremes("NotACategory", "Lowest"))
    except ValueError as e:
        print(e)

