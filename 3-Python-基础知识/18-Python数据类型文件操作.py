# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7

# Python常见数据类型写入到文件中

import pickle
# pickle 表示数据持久性模块

# 用于将list写入到wb文件中
random_string = [1,2,3,4,5,6,"Nothing dries sooner than a tear"]
path = "/root/tmp/pycharm_project_179/3-Python-基础知识/pickle.dump"

with open(path,'wb') as file_pickle_write:
    pickle.dump(random_string,file_pickle_write)

# 从写入的文件中读取对应的list
with open(path,'rb') as file_pickle_read:
    list_out = pickle.load(file_pickle_read)
    print list_out

# 对于 tuple，dict，set的操作是一样的


if __name__ == '__main__':
    pass

