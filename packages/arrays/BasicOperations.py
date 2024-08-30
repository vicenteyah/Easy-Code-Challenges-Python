from typing import List
"""
 # Operations with Sums, Subtractions, and Modulus
    Given an array of integers `nums`, you need to perform the following operations to determine the final value:

        1. **Sum:** Add all the numbers in the array that are multiples of 3.
        2. **Subtraction:** Subtract all the numbers in the array that are multiples of 5.
        3. **Modulus:** For each number in the array, if it is divisible by both 3 and 5, 
           perform the operation `value % 10` and add it to the final result.

    Implementation:
       Write a function `calculateResult(nums: List[int]) -> int` that returns the final value after performing the above operations.

    Example 1:
        Input: nums = [3, 5, 15, 7, 9]
        Output: 12
        Explanation:
            - Sum: 3 + 9 = 12 (multiples of 3)
            - Subtraction: 5 = -5 (multiple of 5)
            - Modulus: 15 % 10 = 5 (multiple of both 3 and 5)
        Final result: 12 - 5 + 5 = 12 
    
    Example 2:
        Input: nums = [6, 10, 30, 12, 25]
        Output: 13
        Explanation:
            - Sum: 6 + 12 + 30 = 48 (multiples of 3)
            - Subtraction: 10 + 25 = 35 (multiples of 5)
            - Modulus: 30 % 10 = 0 (multiple of both 3 and 5)
        Final result: 48 - 35 + 0 = 13 

    Hint:
        Make sure to correctly handle negative numbers and consider that a number can be a multiple of both 3 and 5,
        in which case you should perform all the operations.
"""

class BasicOperations:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def calculate_result(self) -> int:
        # your code here
        return 0