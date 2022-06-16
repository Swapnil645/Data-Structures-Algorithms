def count_rotations(nums):
    if len(nums)>0:
        m = min(nums)
    c = 0
    for ele in nums:
        if ele == m:
            break
        c=c+1
    return c


def count_rotatiuons_binary(nums):
    lo,hi=0,len(nums)-1
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]
        #if nums[mid]<nums[mid-1] and nums[mid]<=nums[mid-1]:
        #if mid>0 and nums[mid]<nums[mid-1]:
        if mid>0 and nums[mid]<nums[mid-1]:
            return mid
        elif nums[mid]<nums[lo]:
            hi = mid-1
        else:
            lo = mid + 1
    
    return 0



    