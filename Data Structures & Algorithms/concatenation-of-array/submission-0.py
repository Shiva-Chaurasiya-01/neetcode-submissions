class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)

        ans = nums.copy()

        for i in range(0 , l):
            ans.append(nums[i])
        
        return ans