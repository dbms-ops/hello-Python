# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# textwrap 模块：用于优化显示结果；
#

import textwrap

# 用于将单个段落包装为 text，并返回包含被包装段落的单个字符串
print textwrap.fill("Thou hast made me endless, such is thy pleasure. This frail vessel thou emptiest again and again, "
                    "and fillest it ever with fresh life.", width=10)

# 将字符串按照 width 进行切割，并且返回一个 list
print textwrap.wrap("Thou hast made me endless, such is thy pleasure. This frail vessel thou emptiest again and again, "
                    "and fillest it ever with fresh life.", width=10)

#
