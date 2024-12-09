from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(numbers)):
            if target - numbers[i] in cache:
                return [cache[target - numbers[i]]+1, i+1]
            cache[numbers[i]] = i
        return [-1, -1]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))