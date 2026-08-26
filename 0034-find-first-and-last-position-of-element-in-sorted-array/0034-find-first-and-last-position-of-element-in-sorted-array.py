class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(is_first: bool) -> int:
            left = 0
            right = len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) //2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound
        first_occurrence = findBound(True)
        if first_occurrence == -1:
            return [-1, -1]
        last_occurrence = findBound(False)
        return [first_occurrence, last_occurrence]