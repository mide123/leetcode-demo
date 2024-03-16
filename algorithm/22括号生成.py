"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
提示：
1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        self.dfs(n, n, "", res)
        return res

    def dfs(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)

        if left > 0:
            self.dfs(left - 1, right, s + "(", res)
        if right > left:
            self.dfs(left, right - 1, s + ")", res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(2))
