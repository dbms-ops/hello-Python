# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
#

import argparse


#   prog: 通过sys.argv[0]来获取当前程序运行的名称，通过%(prog)s可以引用程序名称
#   usage：用于指定该脚本的用法，默认回生成，允许覆盖；
#   description:用于描述程序，脚本；
#   epilog：用于帮助信息的结尾，提供帮助信息；
#   prefix_chars：表示命令开始使用的前缀，例如--help中的-就是前缀；
#   add_help：是否添加帮助信息，默认是打开的；
#       关闭的信息就是这行：-h, --help  show this help message and exit

parser = argparse.ArgumentParser(description="Process some integers.")

#  name or flags: 创建一个参数，例如：foo、 -f、--foo；
#  action：表示对于参数的处理动作
#       store：表示存储参数的值
#       store_const：存储被const命名参数指定的值;
#       store_true: 用于存储True的值，默认是False
#       store_false: 用于存储False的值，默认是True
#       append: 存储一个列表，并且将每个参数值追加到列表中。在允许多次使用选项时很有用
#       append_const: 存储一个列表，并且添加 const 属性
#       count: 用于统计该变量的值
#       help: 打印所有当前解析器中的选项和参数的完整帮助信息，然后退出
#       version: 期望有一个 version= 命名参数在 add_argument() 调用中，并打印版本信息并在调用后退出:
#           parser.add_argument('--version', action='version', version='%(prog)s 2.0')
#  nargs：
#
#       关联一个单独的命令行参数到一个单独的被执行的动作
#       命名参数关联不同数目的命令行参数到单一动作
#       N：指定一个整数，命令行中的 N 个参数会被聚集到一个列表中
#
#


parser.add_argument('integers',metavar='N',nargs='+',type=int,
                    help='an integer for the accumulator')


parser.add_argument('--sum',dest='accumulate',action='store_const',
                    const=sum,default=max,
                    help='sum the integers (default: find the max)')




args = parser.parse_args()
print args.accumulate(args.integers)
print type(args)















if __name__ == '__main__':
    pass
    