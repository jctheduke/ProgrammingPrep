# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

# In next permutation of lexographical series, we 
# are just tyring to find the next smallest larger number that 
# can be formed using the the current sequence of numbers

def next_perm(N):
    n_str = list(str(N)) # For mutating the string nums
    # Find the next largest sequence suffix
    i = len(n_str)-1
    while(i>0):
        if n_str[i-1] < n_str[i]:
            break
        else:
            i -= 1
    # Find the next larger number in the suffix
    if i == 0:
        return None # Next sequence Not present
    else:
        pivot = n_str[i-1]
        for j in range(len(n_str)-1,-1,-1):
            if n_str[j] > pivot:
                break
        
        # Replace the pivot and reverse the suffix
        n_str[i-1], n_str[j] = n_str[j], n_str[i-1]
        n_str[i:] = n_str[len(n_str)-1:i-1:-1]
        x = int(''.join(n_str))
        # Return the number
        return x
x= 1234
while(True):
    x = (next_perm(x))
    if x:
        print(x)
    else:
        break
