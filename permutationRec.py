def generate_permutations(nums):
    # Base case: if the list is empty or has only one element, return it as a permutation
    if len(nums) <= 1:
        yield nums
    else:
        # Iterate through each element in the list
        for i in range(len(nums)):
            # Fix the current element at the beginning and generate permutations for the rest of the elements
            fixed_element = [nums[i]]
            remaining_elements = nums[:i] + nums[i+1:]
            for permutation in generate_permutations(remaining_elements):
                # Yield each permutation with the fixed element at the beginning
                yield fixed_element + permutation


nums = [1, 2, 3]
for permutation in generate_permutations(nums):
    print(permutation)

