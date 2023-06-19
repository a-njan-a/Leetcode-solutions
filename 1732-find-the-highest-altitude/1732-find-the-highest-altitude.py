class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        result = [0] * (len(gain) + 1)

        for i in range(len(gain)):
            result[i+1] = gain[i] + result[i]

        return max(result)