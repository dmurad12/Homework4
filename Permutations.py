def permutationsOperation(input_list):
    # If list is empty then return the empty list
    if len(input_list) == 0:
        return []
    
    # If list only has one element, then return that element
    if len(input_list) == 1:
        return [input_list]
    
    # new list to store all the permutations
    all_permutations = []
    
    # Iterate over each element in the list
    for i in range(len(input_list)):
        current_element = input_list[i]
        
        remaining_elements = input_list[:i] + input_list[i+1:]
        
        # Generate all permutations of the remaining elements
        permutations_of_rest = permutationsOperation(remaining_elements)
        
        for permutation in permutations_of_rest:
            all_permutations.append([current_element] + permutation)
    
    return all_permutations

input_list = [0,7,11,22]
permutations = permutationsOperation(input_list)
for n in permutations:
    print(n)
