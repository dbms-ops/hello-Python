#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/19 10:16
# @user: Administrator
# @fileName: redis_mut_alive.sh.py
# @description: 检测 redis 的状态,包含三种类型的 redis 服务:
#        单个实例节点故障: redis 节点自身故障, 对于 ping 命令不会相应,检查时间持续 2 秒钟, 检查五次;
#           shutdown: 主节点 shutdown, 主节点自身故障,主节点被关闭;
#           连接满:
#        对于 sentinel 服务: 主节点会自动进行切换, 判定类型单个实例节点故障;
#        对于非 sentinel 服务: 主节点无法自动切换, 对于该故障通过 replication 节点可以进行判定 ;
#


def main():
    pass


if __name__ == '__main__':
    main()
