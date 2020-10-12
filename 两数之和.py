class Solution:
    def two_sum(self, nums, target):
        """这样写更直观，遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i
                print(dct[n])
                print(i)
            print(dct)
        return []


s = Solution()
print(s.two_sum(nums=[2, 7, 7, 11, 15], target=10))
