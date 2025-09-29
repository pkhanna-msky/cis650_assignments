import re

FORBIDDEN = set("0123456789+-*/=%^{}") 

NAME_PIECE = r"[A-Za-z][A-Za-z'-]*"

def has_forbidden_chars(s: str) -> bool:
    return any(ch in FORBIDDEN for ch in s)

def parse_name(s: str):
    """
    Returns (first, last, fmt) where fmt is one of 'a','b','c','d' per the prompt:
      a) First Last
      b) Last, First
      c) First Middle Last
      d) First M. Last  (middle initial with or without a period)
    Raises ValueError on invalid input/unsupported format.
    """
    s = s.strip()
    if not s:
        raise ValueError("Empty input.")

    if has_forbidden_chars(s):
        raise ValueError("Contains a number, arithmetic sign, or curly brace.")

    m = re.fullmatch(rf"\s*({NAME_PIECE})\s*,\s*({NAME_PIECE})\s*", s)
    if m:
        last, first = m.group(1), m.group(2)
        return first.title(), last.title(), "b"
    
    parts = re.split(r"\s+", s)

  
    if len(parts) == 2 and all(re.fullmatch(NAME_PIECE, p) for p in parts):
        first, last = parts[0], parts[1]
        return first.title(), last.title(), "a"

   
    if len(parts) == 3 and re.fullmatch(NAME_PIECE, parts[0]) and re.fullmatch(NAME_PIECE, parts[2]):
        first, mid, last = parts
       
        if re.fullmatch(r"[A-Za-z]\.?", mid):
            return first.title(), last.title(), "d"
      
        if re.fullmatch(NAME_PIECE, mid):
            return first.title(), last.title(), "c"

    raise ValueError("Unsupported name format for this assignment.")

def main():
    print("Enter a name to analyze (press Enter with no text to quit).")
    while True:
        raw = input("Name: ").strip()
        if raw == "":
            print("Goodbye!")
            break
        try:
            first, last, fmt = parse_name(raw)
            print(f"Format detected: {fmt}")
            print(f"First name: {first}")
            print(f"Last  name: {last}")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
