# https://leetcode.cn/problems/remove-element/description/
def remove_element(nums: list, val: int) -> int:
    n = len(nums)
    i, j = 0, n - 1
    while i <= j:
        if nums[i] != val:
            i += 1
            continue
        if nums[j] == val:
            j -= 1
            continue
        nums[i], nums[j] = nums[j], nums[i]
    return i


if __name__ == '__main__':
    nums = [3, 3]
    k = remove_element(nums, 5)
    print(k)
    print(nums)
