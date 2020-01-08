# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# 该文件是一个单元测试文件，用于测试 文件 1-函数单元测试
#
import unittest
from func import new_sub
from func import new_sum


# 开始进行测试
class Test(unittest.TestCase):
    def setUp(self):
        print "Unit tests start calling automatically"

    def tearDown(self):
        print "The test ended automatically"

    # 测试函数在函数名前面 + test
    def test_new_sum(self):
        self.assertEqual(new_sum(1, 3), 4, "test_sum error: ")

    def test_new_sub(self):
        self.assertEqual(new_sub(10, 1), 9, "test_sub error: ")


if __name__ == '__main__':
    unittest.main()
