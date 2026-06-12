class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        al, ar = 0, len(nums1) - 1
        bl, br = 0, len(nums2) - 1

        arr = []
        a = 0
        b = 0

        i = 0
        while i != (len(nums1) + len(nums2)):
            if a >= len(nums1):
                arr.append(nums2[b])
                b += 1
                i += 1
                continue

            if b >= len(nums2):
                arr.append(nums1[a])
                a += 1
                i += 1
                continue

            if nums1[a] < nums2[b]:
                arr.append(nums1[a])
                a += 1
                i += 1
            else:
                arr.append(nums2[b])
                b += 1
                i += 1
        
        print(arr)

        if len(arr) % 2 == 0:
            mid = len(arr) // 2 - 1
            return (arr[mid] + arr[mid+1]) / 2
        else:
            return arr[math.ceil(len(arr) / 2) - 1]