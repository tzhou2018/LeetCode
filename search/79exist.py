'''
@Time    : 2020/3/27 21:52
@FileName: 79exist.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        rows = len(board)
        cols = len(board[0])
        tem = [[True] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if self.findPath(board, tem, rows, cols, row, col, word):
                    return True
        return False

    def findPath(self, board, tem, rows, cols, i, j, word):
        if not word:
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols \
                or not tem[i][j] or board[i][j] != word[0]:
            return False
        tem[i][j] = False
        if self.findPath(board, tem, rows, cols, i - 1, j, word[1:]) or \
                self.findPath(board, tem, rows, cols, i, j + 1, word[1:]) or \
                self.findPath(board, tem, rows, cols, i + 1, j, word[1:]) or \
                self.findPath(board, tem, rows, cols, i, j - 1, word[1:]):
            return True
        tem[i][j] = True
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))
