def Duplicated(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums1 = [1, 2, 3, 4]
print(Duplicated(nums1))
nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Duplicated(nums2))
nums3 = [1, 2, 3, 1]
print(Duplicated(nums3))