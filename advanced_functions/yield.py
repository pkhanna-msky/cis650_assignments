from typing import List, Iterator

def running_total(numbers: List[int]) -> Iterator[int]:
    """Yields a running (cumulative) total.
    Example:
    numbers = [2, 5, 3]
    """
    total = 0
    for n in numbers:
        total += n
        yield total 

def squares(numbers: List[int]):
    """Yields the square of each number in the input list.
    Example:
    numbers = [2, 5, 3]
    """
    for n in numbers:
        yield n * n

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Data:", data)
    print("Running totals:", list(running_total(data)))
    print("Squares:", list(squares(data)))

