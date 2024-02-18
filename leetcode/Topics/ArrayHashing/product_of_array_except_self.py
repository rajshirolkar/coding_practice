def productExceptSelf(nums: List[int]) -> List[int]:
    l = nums[0]
    r = nums[len(nums) - 1]
    pdts = [1] * len(nums)

    for i in range(1, len(nums)):
        pdts[i] *= l
        l *= nums[i]
        pdts[len(nums) - 1 - i] *= r
        r *= nums[len(nums) - 1 - i]
    return pdts
