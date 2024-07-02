
def sum_of_multiples(n, a, b):
    """
    Calculate the sum of all natural numbers below `n` that are multiples of `a` or `b`.

    Parameters:
    n (int): The upper limit (exclusive).
    a (int): The first divisor.
    b (int): The second divisor.

    Returns:
    int: The sum of all multiples of `a` or `b` below `n`.
    
    Example:
    sum_of_multiples(1000, 3, 5) ==> 233168
    """
    sum = 0
    for i in range(n):
        if (i % a == 0) or (i % b == 0):
            sum += i
    return sum
