# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#

import argparse
import sys
import textwrap


# ArgumentParser对象解析：
#   prog: 通过sys.argv[0]来获取当前程序运行的名称，通过%(prog)s 可以引用程序名称，该值允许修改
#   usage：用于指定该脚本的用法，默认会生成，允许覆盖；
#   description:在帮助信息的开始描述程序的文本信息；
#   epilog：在帮助信息结尾描述程序的文本信息
#   parents:  ArgumentParser的对象列表，包括其参数；这个适合用于帮助信息相互继承的情况下，暂时用不到
#   formatter_class：一个自定义输出信息的类；
#   prefix_chars：表示命令开始使用的前缀，例如--help中的-就是前缀，默认使用-，不建议进行修改；
#   fromfile_prefix_chars：前缀文件的字符集，应该从这些文件中读取参数；
#   argument_default：全局参数的默认值；
#   add_help：是否添加帮助信息，默认是打开的；
#       关闭的信息就是这行：-h, --help  show this help message and exit


def integers_help():
    # /data1/python2.7/bin/python2.7 /tmp/pycharm_project_73/2-常见模块用法/12-argparse用法详解.py 1 2 3 4 56  --sum
    # 创建 ArgumentParser 解析对象
    parser = argparse.ArgumentParser(description="Process some integers.", epilog="Written by DBA,verson 2.3.1")

    parser.add_argument('integers', metavar='N', nargs='+', type=int,
                        help='an integer for the accumulator')

    parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='%(prog)s：sum the integers (default: find the max)')

    parser.parse_args(['--sum', '7', '-1', '42'])
    args = parser.parse_args()
    print args.accumulate(args.integers)
    print type(args)
    print args.integers
    print type(args.integers)
    print sys.argv[0]


def formatter_class_help():
    # 对于输出的 description 以及 epilog 信息进行换行处理,默认情况下这些信息是按照单行输出的；
    # 一共三个方法 见名知义：
    # RawDescriptionHelpFormatter：
    # RawTextHelpFormatter：
    # ArgumentDefaultsHelpFormatter：
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Please do not mess up this text!
        --------------------------------
         I have indented it，
         exactly the way
         I want it
         '''))
    parser.print_help()


def formatter_class_default_help():
    # 对于 default 参数支持格式化显示
    parser = argparse.ArgumentParser(
        prog="prog",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--foo', type=int, default=42, help='FOO!')
    parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
    parser.print_help()
    args = parser.parse_args()
    print args.__dict__


def prefix_chars_help():
    # 用于修改前缀字符，修改的意义不大，但是可以修改
    parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
    parser.add_argument('+f', default="linux")
    parser.add_argument('++bar')
    print parser.parse_args('+f X ++bar Y'.split())
    args = parser.parse_args()
    print args.__dict__


def fromfile_prefix_chars_help():
    # 对于参数列表十分长的情况，需要通过指定的文件来传入，文件需要通过特殊的前缀来指定,通过文件传递的参数会覆盖通过命令行传递的同名参数
    #
    with open('args.txt', 'w') as fp:
        fp.write('-f\nbar')
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('-f')
    print parser.parse_args(['-f', 'foo', '@args.txt'])


def argument_default_help():
    # 一般默认参数通过 add_argument() 或者 set_defaults() 进行设置；
    # 在需要为参数指定解析器范围时，可以通过设置：argument_default=传递参数
    # 这个功能不常用
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('--foo')
    parser.add_argument('bar', nargs='?')
    print parser.parse_args(['--foo', '1', 'BAR'])


def conflict_handler_help():
    # 默认情况下，ArgumentParser 对象不允许一个字符串拥有两种行为，否则会抛出异常，通过传递conflict_handler='resolve'
    # 可以改变这种行为
    # 这个功能不常用
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
    parser.add_argument('-f', '--foo', help='old foo help')
    parser.add_argument('--foo', help='new foo help')
    parser.print_help()


def add_help_help():
    # 默认情况下，会显示-h --help的帮助信息下，通过传递add_help=False来禁止这种行为
    parser = argparse.ArgumentParser(prog='PROG', add_help=False)
    parser.add_argument('--foo', help='foo help')
    parser.print_help()


# add_argument() 参数解析：
#  name or flags:
#       创建一个参数，例如：foo、 -f、--foo；
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
#
#  nargs：
#       关联一个单独的命令行参数到一个单独的被执行的动作
#       命名参数关联不同数目的命令行参数到单一动作
#       N：指定一个整数，命令行中的 N 个参数会被聚集到一个列表中
#  const：
#        action 和  nargs 应该需要使用const属性；
#  default：
#       如果命令行参数缺席，可以使用的默认参数
#  type：
#       命令行参数，应该被转换成何种类型
#  choices：
#       可选值的一个集合；
#  required：
#       命令行参数是否可以省略，仅仅适合于可选参数使用；
#  help：
#       一个简短的，用于描述参数的行为；
#  metavar：
#       参数在用法信息中的名称；
#  dest：
#       需要添加到parse_args()中的对象属性名称；
#

def name_or_flags_help():
    # 传递可选参数：parser.add_argument('-f', '--foo')；
    # 传递位置参数：parser.add_argument('bar')；
    # 对于上面两种参数类型的判断是通过 - 来实现的
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('-f', '--foo')
    parser.add_argument('bar')
    parser.parse_args(['BAR'])
    args = parser.parse_args()
    print args.__dict__


# action: 表示对于存储的参数采取的行为
def action_store_help():
    #   store：表示存储这个值的行为，该行为是默认行为
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo')
    args = parser.parse_args()
    print args.__dict__


def action_store_const_help():
    # 为存储的值，添加const属性，通常与某些 flag 一起使用
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo', action='store_const', const=42)
    print parser.parse_args(['--foo'])
    args = parser.parse_args()
    print args.__dict__


def action_store_true_help():
    # store_true: 默认为假值，如果传递该参数，修改为真值；
    # 传递该参数，该选项为真
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo', action='store_true')
    args = parser.parse_args()
    print args.__dict__


def action_store_false_help():
    # store_false: 默认为真值，如果传递该参数修改为假值
    # 传递该参数，该选项为假
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo', action='store_false')
    args = parser.parse_args()
    print args.__dict__


def action_append_help():
    # 使用一个列表，并且将后面的参数添加到列表中
    # 例如：-f 1, -f 2, -f 3;
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--foo', action='append')
    args = parser.parse_args()
    print args.__dict__

def action_append_const_help():
    # 类似于 append,用于将多个参数常量，存储在同一个列表中
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--str', dest='types', action='append_const', const=str)
    parser.add_argument('-i','--int', dest='types', action='append_const', const=int)
    args = parser.parse_args()
    print args.__dict__

def action_count_help():
    # count: 用于统计传递参数的个数，通常适合于 -v 选项，可以用于显示更加详细的信息
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count')
    print parser.parse_args(['-vv'])

def action_help():
    pass

def action_version():
    # This expects a version= keyword argument in the add_argument() call, and prints version information and exits
    # 用于输出程序的版本信息
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')
    parser.parse_args(['--version'])

# nargs:
#   ArgumentParser对象用于将一个对象关联到一个单一行为，nargs 用于将不同的数量的命令行参数关联到一个动作上
#   支持以下几种类型：
#       N：表示一个整型参数，用于描述将多少个命令参数当作一个整体放到一个列表中；
#       ?：
#       *：；


def nargs_integer():
    #  N：表示一个整型参数，用于描述将多少个命令参数当作一个整体放到一个列表中；
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--foo', nargs=3)
    parser.add_argument('bar', nargs=1)
    print parser.parse_args('c --foo a b c'.split())


def nargs_question_mark():
    # 如果可能，将从命令行使用一个参数，并将其作为单个项目产生；
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs='?', const='c', default='d')
    parser.add_argument('bar', nargs='?', default='d')
    parser.parse_args(['XX', '--foo', 'YY'])


def nargs_asterisk():
    # *：用于将所有的参数传递到某个列表中；* 通常更加适合与可选参数，而不是位置参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo',nargs='*')
    parser.add_argument('--bar',nargs='*')
    parser.add_argument('baz',nargs='*')
    print parser.parse_args('a b --foo x y --bar 1 2 2 3 4 5 '.split())

def nargs_plus_mark():
    # +： 功能和 * 类似，但是如果没有传递参数，或抛出异常
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('foo', nargs='+')
    # parser.parse_args(['a', 'b'])
    parser.parse_args()

def nargs_remainder():
    # argparse.REMAINDER: 所有的参数都会被放入到一个列表中，这对于分派到其他命令行实用工具的命令行实用工具通常很有用
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo')
    parser.add_argument('command')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    print parser.parse_args('--foo B cmd --arg1 XX ZZ'.split())

# const: ;



def main():
    nargs_asterisk()

if __name__ == '__main__':
    main()
