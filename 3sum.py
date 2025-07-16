# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sort = sorted(nums)
#         maxim = len(sort)-1
#         minim = 0

#         left = 0
#         right = len(nums) - 1

#         summa = nums[left] + nums[right]
#         while maxim >= minim:
#             while left <= right:
#                 if summa == sort[maxim]:
#                     return [nums[left], nums[right], sort[maxim]]
#                 if summa > sort[maxim]:
#                     right -= 1
#                 if summa < sort[maxim]:
#                     right += 1
#             maxim-=1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(len(nums)):
            if a>0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threesum = nums[l] + nums[r] + a
                if threesum > 0:
                    r-=1
                if threesum <0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    if nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
        
