"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""

'''
思路：
那么如何获取到每个连续序列的起点呢，或者说什么样的数才是一个连续序列的起点？
答案是这个数的前一个数不存在于数组中，因为我们需要能够快速判断当前数num的前一个数num - 1是否存在于数组中。

同时当我们定位到起点后，我们就要遍历这个连续序列，什么时候是终点呢？
答案是当前数num的后一个数nunm + 1不存在于数组中，因此我们需要能够快速判断当前数num的后一个数num + 1是否存在于数组中。

为了实现上述需求，我们使用哈希表来记录数组中的所有数，以实现对数值的快速查找。

'''


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        data_set = set(nums)
        max_len = 0
        for n in data_set:
            if (n - 1) not in data_set:
                i = n
                length = 0
                while i in data_set:
                    i = i + 1
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([]))