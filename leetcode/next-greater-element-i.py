class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        greater=[-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                greater[stack[-1]]= nums2[i]
                stack.pop()
            stack.append(i)

        ans=[0]*len(nums1)
        for i in range(len(nums1)):
            ans[i]= greater[nums2.index(nums1[i])]
        return ans

