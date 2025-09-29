class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        stack = []
        stackdup = []

        for i in range(length):
            if stack and stack[-1] == nums[i]:
                stackdup.append(nums[i])
            else:
                stack.append(nums[i])

        nums[:] = stack
        
        return len(stack)
