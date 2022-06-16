from syslog import LOG_LOCAL5

from numpy import minimum


class Solution:
    def binary_search(self, nums, target):
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid = (hi+lo)//2
            mid_number = nums[mid]
            print('lo.... hi....mid.... mid_number',lo,hi,mid,mid_number)
            if mid_number == target:
                if target == nums[mid-1]:
                    mid = mid-1
                return mid   
            elif mid_number > target:
                hi = mid - 1
            elif mid_number < target:
                lo = mid + 1
        return -1



    def count_rotations_linear(self,nums):
        [4,1,2,3]
        lo,hi = 0,len(nums)-1
        m=1


        c = 0
        for ele in nums:
            if ele == m:
                break
            c=c+1
        return c


    """a sorted list will be given as input with its elements rotated"""
    """This is a function whichs return value of K times the list is roatated using binary search"""
    def count_rotations(self,nums):
        #nums=[4,5,1,2,3]  [3,4,5,1,2]
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid = (lo+hi)//2
            mid_number = nums[mid]
            #if nums[mid]<nums[mid-1] and nums[mid]<=nums[mid-1]:
            if mid>0 and nums[mid]<nums[mid-1]:
                return mid
            elif nums[mid]<nums[lo]:
                hi = mid-1
            else:
                lo = mid + 1




		    # elif nums[mid] > nums[end]:
            #     start = mid+1
            # elif nums[mid]<nums[hi]:
            #     hi = mid - 1
            # else:
            #     lo = mid + 1 
        return 0




# def countRotations(arr):
# 	n = len(arr)
# 	start = 0
# 	end = n-1

# 	# Finding the index of minimum of the array
# 	# index of min would be equal to number to rotation
# 	while start<=end:
# 		mid = start+(end-start)//2
		
# 		# Calculating the previous(prev)
# 		# and next(nex) index of mid
# 		prev = (mid-1+n)%n
# 		nex = (mid+1)%n

# 		# # Checking if mid is minimum
# 		if arr[mid]<arr[prev] and arr[mid]<=arr[nex]:
# 		    return mid
       

# # Driver code
# arr = [6, 12,15,18,2,3]
# n = len(arr)
# print(countRotations(arr))


obj = Solution()
print(obj.count_rotations([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
