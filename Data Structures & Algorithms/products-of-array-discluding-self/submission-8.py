class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pre.append(nums[0])
        end = [0] * len(nums)
        end[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            pre.append(pre[i - 1] * nums[i])
        for i in range(len(nums) - 2, 0, -1):
            end[i] = end[i + 1] * nums[i]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(end[1])
            elif i == len(nums) - 1:
                res.append(pre[len(nums) - 2])
            else:
                res.append(pre[i - 1] * end[i + 1])
        
        return res

            

        
