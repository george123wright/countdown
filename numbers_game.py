from typing import List
import itertools

def find_first_expression(nums: List[int], target: int) -> str:
    """
    Finds the first valid expression using the numbers in `nums` with operations
    (+, -, *, /) and brackets to compute the `target`. Ensures the output is
    clearly structured with brackets for BIDMAS logic.
    """
    operators = ['+', '-', '*', '/']

    for subset_size in range(1, len(nums) + 1):
        
        for num_subset in itertools.permutations(nums, subset_size):
            
            for operator_combination in itertools.product(operators, repeat=len(num_subset)-1):

                def build_expression(numbers, operators):

                    expr = f"{numbers[0]}"

                    for i in range(len(operators)):
                        expr = f"({expr}{operators[i]}{numbers[i + 1]})"
                    return expr

                expression = build_expression(num_subset, operator_combination)
                
                try:
                    if eval(expression) == target:
                        return expression  
                except ZeroDivisionError:
                    continue
    
    return None  


nums = [2, 4, 15, 8, 50, 100]
target = 739
first_valid_expression = find_first_expression(nums, target)
print(first_valid_expression)

first_valid_expression = find_first_expression(nums, target)
print(first_valid_expression)
