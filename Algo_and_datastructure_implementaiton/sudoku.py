class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):

        # check if the sudoku is valid in given state
        def check_row(A, row):
            list_row = [x for x in A[row] if x != '.']
            set_row = set(list_row)
            if len(list_row) == len(set_row):
                return True
            else:
                False

        def check_col(A, col):
            list_col = [A[row][col] for row in range(len(A)) if A[row][col] != '.']
            if len(list_col) == len(set(list_col)):
                return True
            else:
                return False

        def check_block(A, row, col):
            nums_list = []
            row_block = 3 * (row//3)
            col_block = 3 * (col//3)
            for row in range(row_block, row_block+2):
                for col in range(col_block, col_block+2):
                    if A[row][col] != '.':
                        nums_list.append(A[row][col])
            if len(nums_list) == len(set(nums_list)):
                return True
            else:
                return False

        def check_valid(A, row, col):
            if check_row(A, row) and check_col(A, row) and check_block(A, row, col):
                return True
            else:
                return False

        # Explore all the options and see if sudoku is valid.
        def helper(A, row, col, nums):
            while(col < 9):
                if A[row][col] != '.':
                    col += 1
                else:
                    ele = nums.pop(0)
                    B = A[:]
                    B[row] = B[row][:col]+ele+B[row][col+1:]
                    if check_valid(B, row, col):
                        A[row][col] = ele
                        col += 1
                    else:
                        nums.append(ele)
            return A

        row = 0
        col = 0
        nums = list(range(1, 10))

        row = 0 
        col = 0
        helper(A,row,col)

        for row in range(len(A)):
            col = 0
            poss_nums = [str(x) for x in nums if str(x) not in A[row]]
            A = helper(A, row, col, poss_nums)

x = Solution()
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
x.solveSudoku(A)
