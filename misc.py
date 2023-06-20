from itertools import combinations, combinations_with_replacement, permutations

def get_combinations(num_chips, array_size):
    numbers = range(num_chips + 1)
    combinations = list(combinations_with_replacement(numbers, array_size))
    result = []
    
    for combo in combinations:
        if sum(combo) == num_chips:
            result.append(combo)

    return result

def get_permutations(combinations):
    combo_perms = []

    for combo in combinations:
        combo_perms.extend(list(set(permutations(combo))))

    return combo_perms
        

def permute(num_chips, array_size):
    combinations = get_combinations(num_chips, array_size)
    permutations = get_permutations(combinations)
    
    return permutations