# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 该文件用于对于 person 类进行测试；
# ；
#
#

import unittest

from person import Person


class Test(unittest.TestCase):
    def setUp(self):
        print "test start"

    def tearDown(self):
        print "tear down"

    def test_init(self):
        tom = Person("tom",13)
        self.assertEqual(tom.name,"tom","name error")

    def test_getage(self):
        tom = Person("tom",22)
        self.assertEqual(tom.getage(),tom.age,"getage error")


if __name__ == '__main__':
    unittest.main()
