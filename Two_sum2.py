class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            if index1 < index2 and numbers[index1] + numbers[index2] == target:
                return [index1 + 1, index2 + 1]
            if numbers[index1] + numbers[index2] < target:
                index1 +=1
            else:
                index2 -=1
        
