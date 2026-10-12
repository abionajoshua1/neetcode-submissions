class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate starting values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum < 0:
                    j += 1

                elif current_sum > 0:
                    k -= 1

                else:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate values for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result