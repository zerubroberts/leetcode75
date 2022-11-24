from problem_724_pivot_index import Solution
import unittest   # The test framework

class Test_LeetCode(unittest.TestCase):
    def test_case1(self):
        assert Solution.pivotIndex(self, [43,44]) == 44

    def test_case2(self):
        assert Solution.pivotIndex(self, [143,44]) == 4402




if __name__ == '__main__':
    unittest.main()