def generate_permutations(nums):
    if len(nums) == 0:
        return [[]]  # Base case: empty list has one permutation, which is the empty list
    permutations = [[]]  # Initialize with an empty permutation
    for num in nums:
        print("num: ", num)
        new_permutations = []
        print("new_permutations: ", new_permutations)
        for perm in permutations:
            print("perm: ", perm)
            for i in range(len(perm) + 1):
                print("i: ", i)
                new_perm = perm[:i] + [num] + perm[i:]
                print("new_perm: ", new_perm)
                new_permutations.append(new_perm)
                print("new_permutations: ", new_permutations)
        permutations = new_permutations
        print("permutations: ", permutations)
    return permutations

# Example usage:
nums = [1, 2, 3]
permutations = generate_permutations(nums)
for permutation in permutations:
    print(permutation)
