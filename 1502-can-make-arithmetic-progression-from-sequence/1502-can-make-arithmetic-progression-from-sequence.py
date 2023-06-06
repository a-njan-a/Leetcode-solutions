class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sArr = sorted(arr)
        diff = sArr[1] - sArr[0]
        for i in range(1, len(sArr) - 1):
            if (sArr[i+1] - sArr[i] != diff):
                return False
        return True