class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for char in strs:
            sorted_string = tuple(sorted(char))
            if sorted_string not in groups:
                groups[sorted_string] = [char]

            else:
                groups[sorted_string].append(char)
            
        return list(groups.values())