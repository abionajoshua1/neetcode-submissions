from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = Counter(nums)
        
        # Step 2: Use heap to get k most common
        return [item for item, count in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
