
'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_list = []
        max_len = 0
        for c in s:
            if c not in sub_list:
                sub_list.append(c)
                now_len = len(sub_list)
                if max_len < now_len:
                    max_len = now_len
            else:
                sub_list = sub_list[sub_list.index(c)+1:]
                sub_list.append(c)
        return max_len

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))