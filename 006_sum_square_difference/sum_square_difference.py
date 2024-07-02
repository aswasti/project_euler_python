import math

def sum_square_difference(n):
    """
    Find the difference between the sum of the squares of consecutive the natural numbers <= n and the square of the sum.

    Parameters:
        n (int): limit of how many natural numbers to use to find the sum square difference
    
    Returns:
        (int): difference between the sum of the squares of consecutive the natural numbers <= n and the square of the sum
    
    Example: 
        The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + 3^2 ... 10^2 = 385
        The square of the sum of the first ten natural numbers is, (1 + 2 + 3 ... + 10)^2 = 55^2 = 3025
        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is, 3025 - 385 = 2640
        
        sum_square_difference(10) ==> 2640
        sum_square_difference(100) ==> 25164150
    """
    sum = (n*(n+1))/2
    sum_of_squares = (n*((2*n) + 1)*(n+1))/6 # (n(n+1)) / 2
    sum_square_difference = math.pow(sum,2) - sum_of_squares # (n(2n+1)(n+1)) / 6
    return int(sum_square_difference)
    

        
        

    
    