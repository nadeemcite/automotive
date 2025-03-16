def add_two_numbers(a: int, b: int) -> int:
    """Add two positive integers together.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
        
    Returns:
        int: Sum of the two numbers
        
    Raises:
        ValueError: If either number is negative
        TypeError: If inputs are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Only positive integers are allowed")
    return a + b
