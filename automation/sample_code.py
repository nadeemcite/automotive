def sum(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed")
    return a + b
