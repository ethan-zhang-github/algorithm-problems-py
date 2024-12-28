# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
def two_sub(numbers: list, target: int) -> list:
    table = {}
    for i in range(len(numbers)):
        if target - numbers[i] in table:
            return [table[target - numbers[i]]+1, i+1]
        table[numbers[i]] = i
    return []

if __name__ == '__main__':
    print(two_sub([2, 7, 11, 15], 9))