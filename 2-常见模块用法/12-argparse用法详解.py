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

# const: 表示需要保持改参数值不变，并且这个值不是从命令行获取
# 最常见的两个用途：
#   1、当  add_argument() 使用 action='store_const' or action='append_const'；
#   2、当 add_argument() 调用位置参数使用 nargs='?'，该选项允许传递0个或者一个命令行参数，当传递的参数为空时，默认使用的是const属性的
#   参数；

# default:
#   1、当位置参数或者是命令行参数被省略时，默认default被设置为None，该参数允许被设置，在位置参数或者命令参数传递为空时，使用default传递的
#   默认参数；
#
def default_int_help():
    # 用于设置参数的默认值，这个很有用
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--foo', default=42)
    print parser.parse_args(['--foo', '2'])
    # 当传递的参数为空时，使用默认参数值 42
    print  parser.parse_args([])

def default_string_help():
    # 如果设置的参数类型不匹配，参数为int，默认类型为default为 string，解析器会进行转换;
    # 如果不提供类型，将不进行转换
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', default='10', type=int)
    parser.add_argument('--width', default='10.5')
    print  parser.parse_args([])

def default_positional_help():
    # 当位置参数使用 nargs=？|*时，当没有命令行参数传递时，使用默认参数
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', nargs='?', default=42)
    print parser.parse_args(['a'])
    print parser.parse_args([])
    # 当传递 default=argparse.SUPPRESS 时，默认值为空
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', default=argparse.SUPPRESS)
    print parser.parse_args([])
    print parser.parse_args(['--foo', '1'])

# type:
#   默认情况下，ArgumentParser 对象从命令行读取的参数是字符串类型，但是字符串类型，往往需要解释称为其他的类型
#   type用来执行这种转换;
def type_file_help():
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', type=int)
    parser.add_argument('bar', type=file)
    print parser.parse_args('2 temp.txt'.split())

def type_write_file_help():
    # 该参数支持创建文件 FileType('w') 表示创建可写文件
    parser = argparse.ArgumentParser()
    parser.add_argument('bar', type=argparse.FileType('w'))
    print parser.parse_args(['out.txt'])


# choice: 某些命令行参数支持从一个指定的列表中选择，并且会检查传递的参数是否在这个列表中;
# 参数检查发生在类型转换之后，类型需要尽可能匹配
def choice_check_help():
    parser = argparse.ArgumentParser(prog='game.py')
    parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
    print parser.parse_args(['rock'])
    # 当传递的参数不在列表中时，会抛出异常
    print parser.parse_args(['fire'])

def choice_conversions_help():
    parser = argparse.ArgumentParser(prog='doors.py')
    parser.add_argument('door', type=int, choices=range(1, 4))
    # 对于传入的字符串是可以转换成为 int 类型的
    print parser.parse_args(['3'])
    # 在进行类型转换之后，检查参数是否在列表中
    print parser.parse_args(['4'])


# required:
#   对于可选参数，默认是不强制进行传递的，如果需要修改这种行为，通过传递 require 来进行更改;

def required_help():
    # require 传递参数，要求改参数必须传递，类似于位置参数行为；
    # 如果参数设置了 required 但是却没有传递，那么会出错
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', required=True)
    print parser.parse_args(['--foo', 'BAR'])


def help_help():
    # help 对于某些选项支持静默输出，通过设置argparse.SUPPRESS
    parser = argparse.ArgumentParser(prog='frobble')
    parser.add_argument('--foo',help=argparse.SUPPRESS)
    parser.print_help()


def metavar_help():
    # metavar指定类似于：
    #   [-h] [--foo YYY] XXX
    #   XXX
    #   --foo YYY；
    # 通过上述方式指定期望传递的参数个数，需要结合 nargs 一起使用
    parser = argparse.ArgumentParser()
    parser.add_argument('bar', metavar='XXX')
    parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
    # parser.print_help()
    args = parser.parse_args()
    # 输出类似于：
    # {'foo': ['bar', 'baz'], 'bar': 'XXX'}
    print args.__dict__

def dest_help():
    # dest：
    #   通常情况，参数解析都会交给 parse_args() 来进行，可以通过dest来修改这种行为；
    parser = argparse.ArgumentParser()
    # 在传递dest之后，--foo对应的值，应该保存在bar中，而不是foo中
    parser.add_argument('--foo', dest='bar')
    print parser.parse_args('--foo XXX'.split()).__dict__


# parse_args(args=None, namespace=None)
#   用于进行命令行参数解析
#   args：支持一个参数列表，默认从 sys.argv 进行传递
#   namespace：这个默认传递为空；

def parse_args_help():
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    parser.add_argument('--foo')
    print parser.parse_args(['-x', 'X'])
    print parser.parse_args(['--foo', 'FOO'])

1



def main():
    dest_help()



if __name__ == '__main__':
    main()
