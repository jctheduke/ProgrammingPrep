class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        """Pick a point and check the relative slope of all other points to this point. If the two different points have the same slope they are in the same line. Check the maximum number of points a line can have by having this particular point on it's one end.
        Note:
        1. We don't need to check of intercept as we kept one end fixed.This way there is no possiblity of paralled lines.
        2. Overlapping points should be taken care off.
        3. Lines which are parallel to Y will give a infinite slope. So, keep a tracker for the points which fall in this vertical line.
        """
        global_max = []
        for i in range(len(A)):
            local_slope_dict = {}
            vertical = 1
            overlap = 0
            for j in range(i+1, len(A)):
                if A[i] == A[j] and B[i]==B[j]:
                    overlap += 1
                elif A[i] == A[j]:
                    vertical += 1
                else:
                    slope = (B[i]-B[j])/(A[i]-A[j])
                    local_slope_dict[slope] = local_slope_dict.get(
                        slope, 1) + 1
            local_max = max(list(local_slope_dict.values()) + [-10])
            local_max = max(local_max,vertical)
            local_max = local_max + overlap
            global_max.append(local_max)
        return max(global_max)


c = Solution()
A = [-6 ,5, -18, 2, 5, -2,]
B = [-17 ,-16 ,-17, -4 , -13, 20]
print(c.maxPoints(A,B))
