def generate_permutations(nums):
    if len(nums) <= 1:
        return [nums]
    else:
        permutations = []
        for i in range(len(nums)):
            fixed_element = [nums[i]]
            remaining_elements = nums[:i] + nums[i+1:]
            for permutation in generate_permutations(remaining_elements):
                permutations.append(fixed_element + permutation)
        return permutations

# Example usage:
nums = [1, 2, 3]
permutations = generate_permutations(nums)
for permutation in permutations:
    print(permutation)
