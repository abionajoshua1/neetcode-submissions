class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for string in strs:
            length = len(string)
            separator = "#"

            encoded_string += f"{length}{separator}{string}"

        return encoded_string

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            separator_index = s.find("#", i)

            length = int(s[i:separator_index])

            string_start = separator_index + 1
            string_end = string_start + length

            string = s[string_start:string_end]

            result.append(string)

            i = string_end

        return result