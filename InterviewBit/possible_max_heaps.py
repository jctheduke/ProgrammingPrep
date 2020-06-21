class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        """
        Calculate the possible number of max heaps that can be formed using the n distinct numbers
        https://www.geeksforgeeks.org/number-ways-form-heap-n-distinct-integers/
        """

        
        # calcualte log2 with out using the inbuild math library
        # recursivly calcuate T(n) = n-1Cl + T(l) + T(r)

        n = A
        
        # Number of max heaps that can be farmed with i distinct values
        dp = [0]*(101) # Max input constraint is 100.

        # dp storage for nCk
        nck = [ [0 for j in range(101)] for i in range(101)]

        # Log2 values for 1 to n integers
        log2i = [0]*101

        # calculate ncr using dp
        def cal_nCk(n,k):

            if k > n:
                return 0
            elif n <= 1:
                return 1
            elif k==0:
                return 1
            
            if nck[n][k] != -1:
                return nck[n][k]

            res = cal_nCk(n-1,k-1) + cal_nCk(n-1, k)
            nck[n][k] = res
            return res
        
        def getLeft(n):
            if n==1:
                return 0
            h = log2i[n]

            numh = 1<<h

            last = n - ((1<<h)-1)

            if (last >= numh//2):
                return (1<<h) -1
            else:
                return (1<<h) - 1 - ((numh//2)-last)
        
        def numberofHeaps(n):
            if (n<=1):
                return 1
            
            if (dp[n] != -1):
                return dp[n]
            
            left = getLeft(n)
            ans = (cal_nCk(n-1, left)) * numberofHeaps(left) * numberofHeaps(n-1-left)
            dp[n] = ans
            return ans
        
        def solve_n(n):
            for i in range(n+1):
                dp[i] = -1
            
            for i in range(n+1):
                for j in range(n+1):
                    nck[i][j] = -1
            
            curr_log_2 = -1
            curr_pow_2 = 1

            for i in range(1,n+1):
                if (curr_pow_2 == i):
                    curr_log_2 += 1
                    curr_pow_2 *= 2
                log2i[i] =curr_log_2
            return numberofHeaps(n)
        
        return solve_n(n) % 1000000007

x =Solution()
print(x.solve(4))
print(x.solve(34))
print(x.solve(55))