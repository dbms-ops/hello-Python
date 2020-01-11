# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# ConfigParser 模块：
#   该模块在 Python 3 中命名为 configparser，该模块主要用改修改和读取配置文件；
#
import ConfigParser
import os


# 创建一个简答的配置文件：
#

# RawConfigParser Objects 支持的方法
#   RawConfigParser.defaults()：
#       返回实例section 为 default 对应的 option ；
#   RawConfigParser.sections():
#       返回所有的section列表；
#   RawConfigParser.add_section(section)：
#       用于添加一个section，如果添加一个已经存在的，会抛出异常，如果传递DEFAULT，也会抛出异常；
#   RawConfigParser.has_section(section)：
#       用于判断是否拥有某个section，在添加之前应该先进行判断；
#   RawConfigParser.options(section)：
#       返回这个 section 包含的选项列表；
#   RawConfigParser.read(filenames)；
#       filenames：接受一个文件名称的列表
#       对于传递的文件名进行解析，并且返回一个文件名解析后的列表；
#   RawConfigParser.readfp(fp[, filename])：
#       解析filename读取配置数据；
#   RawConfigParser.get(section, option)：
#       获取选项对应的值
#   RawConfigParser.getint(section, option)：
#       用于将指定选项中的值转换成为整数；
#   RawConfigParser.getfloat(section, option)：
#       用于将指定选项中的值转换成为浮点数；
#   RawConfigParser.getboolean(section, option)：
#       布尔值的转换；对于：1，yes，true，on返回True；
#       对于：0、no、false、off，返回值是False；
#       其他类类型值，会抛出：ValueError 异常
#   RawConfigParser.items(section)：
#       用于返回 section 对应的 key-value 列表；
#   RawConfigParser.set(section, option, value)：
#       根据 section option value设置对应的选项
#   RawConfigParser.write(fileobject):
#       像文件对象中写入配置信息，可以通过调用read来解析该文件对象
#   RawConfigParser.remove_option(section, option)：
#       用于移除某个 section 的 option，如果 section 不存在，抛出异常，如果 option 存在，会返回true，否则返回false；
#   RawConfigParser.remove_section(section):
#       移除某个 section，如果section 不存在，抛出异常；
#   RawConfigParser.optionxform(option)：
#       ；
#   ；

def write_a_config_file(cnf):
    config = ConfigParser.ConfigParser()
    config.add_section("MySQL")
    config.set('MySQL', 'port', 6301)
    config.set('MySQL', 'innodb_buffer_size', '4G')
    config.add_section("mysqld")
    config.set('mysqld', 'a_float', '3.1415')
    config.set('mysqld', 'baz', 'fun')
    config.set('mysqld', 'bar', 'Python')
    config.set('mysqld', 'foo', '%(bar)s is %(baz)s!')

    with open(cnf, 'wb') as fp:
        config.write(fp)


def delete_cnf(cnf):
    if os.path.exists(cnf):
        os.remove(cnf)


def read_files(filenames):
    # 函数用于解析文件名，并且返回一个文件名列表
    config = ConfigParser.ConfigParser()
    result = config.read(filenames)
    print result


def read_config(configfile):
    config = ConfigParser.ConfigParser()
    config.read(configfile)
    print config.get('mysqld', 'a_float')
    print config.get('MySQL', 'port')
    config.set('MySQL', 'port', 1)
    config.set('mysqld', 'a_float', 1)


def add_default(cnf):
    config = ConfigParser.ConfigParser()
    config.set('DEFAULT', 'replayer.collection_parallel', 6)
    config.set('DEFAULT', 'replayer.document_parallel', 8)
    config.set('DEFAULT', 'replayer.collection_drop', False)
    with open(cnf, 'wb') as fp:
        config.write(fp)


def main():
    configfile = "/root/config.cnf"
    add_default(configfile)


if __name__ == '__main__':
    main()
