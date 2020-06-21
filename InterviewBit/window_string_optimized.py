class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if len(A) < len(B) or len(A) == 0 or len(B) == 0:
            return ''

        b_dict = {}
        for x in B:
            if x in b_dict:
                b_dict[x] += 1
            else:
                b_dict[x] = 1
        min_count_matches = 0
        
        def add_j(j):
            j += 1
            if A[j] not in b_dict:
                pass
            elif A[j] in sol_dict:
                sol_dict[A[j]] += 1
            else:
                sol_dict[A[j]] = 1
            return j

        def check_valid():
            if len(sol_dict) < len(b_dict):
                return False
            for x in b_dict:
                if sol_dict[x] < b_dict[x]:
                    return False
            return True
        
        sol_dict = {}
        i = 0
        j = -1
        sols = []

        j = add_j(j)
        

        while(i <= j and j < len(A)):
            print(A[i:j+1])
            if check_valid():
                sols.append((j-i, i, j))
                if A[i] not in b_dict:
                    pass
                else:
                    if sol_dict[A[i]] == 1:
                        sol_dict.pop(A[i])
                    else:
                        sol_dict[A[i]] -= 1
                i += 1
            else:
                if j == len(A)-1:
                    j += 1
                    break
                j = add_j(j)
        if len(sols) == 0:
            return ''
        sols.sort()
        start = sols[0][1]
        end = sols[0][2]
        return A[start:end+1]

x = Solution()
print(x.minWindow("ADOBEC", "ABC"))
