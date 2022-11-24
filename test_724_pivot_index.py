from problem_724_pivot_index import Solution
import unittest   # The test framework

class Test_LeetCode(unittest.TestCase):
    def test_case1(self):
        assert Solution.pivotIndex(self, [1,7,3,6,5,6]) == 3

    def test_case2(self):
        assert Solution.pivotIndex(self,  [1,2,3]) == -1

    def test_case3(self):
        assert Solution.pivotIndex(self,  [2,1,-1]) == 0







if __name__ == '__main__':
    unittest.main()