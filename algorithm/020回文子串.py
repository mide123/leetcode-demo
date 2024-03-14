
'''

给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"


提示：
1 <= s.length <= 1000
s 由小写英文字母组成
'''
class Solution:
    def countSubstrings(self, s: str) -> int:

        def manacher():
            # 马拉车算法
            arm = [0] * n
            x, y = 0, -1
            for i in range(0, n):
                k = 1 if i > y else min(arm[x + y - i], y - i + 1)

                # 持续增加回文串的长度
                while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                    k += 1
                arm[i] = k

                # 更新右侧最远的回文串边界
                k -= 1
                if i + k > y:
                    x = i - k
                    y = i + k
            # 返回每个位置往右的臂长
            return arm

        s = "#" + "#".join(list(s)) + "#"
        n = len(s)
        dp = manacher()

        # 计算真实长度回文串的个数
        ans = 0
        for num in dp:
            num = (num * 2 - 1) // 2
            if num % 2 == 0:
                ans += num // 2
            else:
                ans += num // 2 + 1
        return ans



if __name__ == '__main__':
    solution = Solution()
