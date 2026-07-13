class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = 0
        right = len(heights) - 1
        width = len(heights) - 1
        while left < right:
            c = width * min(heights[left], heights[right])
            if(c > max):
                max = c

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            width -= 1
        
        return max