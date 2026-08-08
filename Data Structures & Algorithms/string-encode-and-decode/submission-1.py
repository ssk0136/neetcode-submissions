class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str(len(word)) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != '#':
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract exactly 'length' characters
            res.append(s[j:j + length])

            # Move to the next encoded word
            i = j + length

        return res