class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, low, high, x):
            if low <= high: 
                mid = (low + high) // 2
                #weather it's ascending on the left or right
                if arr[mid] == x:
                    return mid

                if arr[low] <= arr[mid]: # asc on the left
                    # first see if x is on the left
                    print("test1")
                    if x >= arr[low] and x < arr[mid]:
                        print("1",arr[low:mid])
                        return binary_search(arr, low, mid-1, x)
                    else: # on the right
                        print("2",arr[mid+1:])
                        return binary_search(arr, mid+1, high, x)

                elif arr[high] >= arr[mid]: # asc on the right
                    # first see if x is on the right
                    if x > arr[mid] and x <= arr[high]:
                        return binary_search(arr, mid+1, high, x)
                    else:
                        return binary_search(arr, low, mid-1, x)
            else:
                return -1
        print(nums, target)
        return binary_search(nums, 0, len(nums)-1, target)