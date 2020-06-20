# Find the kth lexicographical sequence of the given numbers.

# Concept : Each number at the 1st position has 
# (n-1)! permuations with the rest of the numbers
# for 2nd element there are there (n-2)! and so on

def fact(n):
    if n == 0 or n==1:
        return 1
    return n*fact(n-1)

def kth_permutation(n,k):
    k = k -1
    nums = list(range(1,n+1))
    ith_permutations = fact(n)
    output = []
    for i in range(n):
        ith_permutations = int(ith_permutations/(n-i))
        ith_position = int(k/ith_permutations)
        output.append(nums.pop(ith_position))
        k = k - ith_position*ith_permutations
    return output

# for i in range(10):
print(0, kth_permutation(0,0))


