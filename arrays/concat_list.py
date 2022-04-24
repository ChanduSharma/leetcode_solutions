def concat_list_twice(nums: list[int]) -> list[int]:
    """
    concat a single list twice
    """    
    res = []
    length = len(nums)
    for i in range(2 * length):
        res.append(nums[i % length])

    return res
