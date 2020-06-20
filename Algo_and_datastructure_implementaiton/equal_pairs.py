class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        # run a two for loops and store the values of a+b in a dict.
        # add the sum of A[a]+A[b] as the key and (a,b) as pair.
        # when there a collison that mean we have an answer to the solution.
        sum_dict = {}
        solutions = []
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                sum_val = A[i]+A[j]
                if sum_val in sum_dict:
                        a, b = sum_dict[sum_val]
                        if a==i or b==i or b==j:
                            pass
                        else:
                            # sol_str = 'a'.join(list(map(str,[a,b,i, j])))
                            sol_str = [a,b,i,j]
                            solutions.append(sol_str)
                else:
                    sum_dict[sum_val] = [i,j]
        
        # sort solutions
        solutions.sort()
        print(solutions)
        # return the least solution
        #return list(map(int,solutions[0].split('a')))
        return solutions[0]

x= Solution()
print(x.equal([9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8,7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5]))
