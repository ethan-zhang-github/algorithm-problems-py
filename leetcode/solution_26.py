# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums: list) -> int:
    if not nums:
        return 0
    fast = slow = 1
    while fast < len(nums):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    print(k)
    print(nums)
