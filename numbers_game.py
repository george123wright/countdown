from typing import List
import itertools

def find_first_expression(nums: List[int], target: int) -> str:

    operators = ['+', '-', '*', '/']
    
    for subset_size in range(1, len(nums) + 1):
        for num_subset in itertools.permutations(nums, subset_size):
            for operator_combination in itertools.product(operators, repeat=len(num_subset)-1):
                expressions = []
                
                flat_expression = ''.join(
                    f"{num_subset[i]}{operator_combination[i]}" for i in range(len(num_subset) - 1)
                ) + str(num_subset[-1])
                expressions.append(flat_expression)
                
                if len(num_subset) > 1:
                    expressions.append(
                        f"({num_subset[0]}{operator_combination[0]}{num_subset[1]})"
                        + ''.join(f"{operator_combination[i]}{num_subset[i + 1]}" for i in range(1, len(num_subset) - 1))
                    )
                
                if len(num_subset) > 2:
                    expressions.append(
                        ''.join(f"{num_subset[i]}{operator_combination[i]}" for i in range(len(num_subset) - 2))
                        + f"({num_subset[-2]}{operator_combination[-1]}{num_subset[-1]})"
                    )
                
                if len(num_subset) > 2:
                    full_bracket_expression = f"({flat_expression})"
                    expressions.append(full_bracket_expression)
                
                for expr in expressions:
                    try:
                        if eval(expr) == target:
                            return expr  
                    except ZeroDivisionError:
                        continue
    
    return None  

nums = [2, 4, 15, 8, 50, 100]
target = 739
first_valid_expression = find_first_expression(nums, target)
print(first_valid_expression)
