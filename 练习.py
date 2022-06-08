def selSort(nums):
    n = len(nums)
    for bottom in range(n-1):
        mi = bottom
        for i in range(mi, n):
            if nums[i] < nums[mi]:
                 mi = i
        nums[bottom], nums[mi] = nums[mi], nums[bottom] 
    return nums
                
numbers = [49, 38, 65, 97, 76, 13, 27, 49]
print(selSort(numbers))