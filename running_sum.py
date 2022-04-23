from cProfile import run


def running_sum(nums: list[int]) -> list[int]:

    i = 1
    while i < len(nums):
        nums[i] = nums[i] + nums[i-1]
        i += 1

    return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(*running_sum(nums))