class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] = seen[num]+1

        top_k = seen.items()

        def get_frequency(i):
            return i[1]

        sorted_top_k = sorted(top_k, key=get_frequency)

        result = []

        for i in sorted_top_k[-k:]:
            a = i[0]
            result.append(a)

        return result

