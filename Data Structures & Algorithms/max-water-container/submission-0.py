class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l,r = 0, len(heights)-1

        while(l < r):
            h = min(heights[l], heights[r])
            w = r - l
            area = w * h
            res = max(res, area)
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
            
        
        return res