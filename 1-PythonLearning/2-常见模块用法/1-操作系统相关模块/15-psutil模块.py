#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/19 10:37
# @user: Administrator
# @fileName: 15-psutil模块.py
# @description: psutil 模块:  process and system utilities, 用于检查操作系统的状态信息;
# https://psutil.readthedocs.io/en/latest/#system-related-functions

import datetime
import time

import psutil


def portStatusStat(port=22):
    statusList = ["LISTEN", "ESTABLISHED", "TIME_WAIT", "CLOSE_WAIT", "LAST_ACK", "SYN_SENT"]
    statusTemp = []
    portStatus = {}
    netConnections = psutil.net_connections()
    for netStatus in netConnections:
        if netStatus.laddr[1] == port:
            statusTemp.append(netStatus.status)

    for status in statusList:
        portStatus[status] = statusTemp.count(status)
    return portStatus


def cpuTimes():
    # CPU 的暂时用不到, 等到需要的时候再来整理
    print psutil.cpu_times(percpu=False)
    #
    print psutil.cpu_percent(interval=None, percpu=False)
    time.sleep(0.2)
    print psutil.cpu_percent(interval=0.2, percpu=True)

    # 统计 cpu 的数量
    print psutil.cpu_count()

    # 统计 CPU 的状态信息
    print psutil.cpu_stats()

    # 输出 CPU的频率
    print psutil.cpu_freq(percpu=False)

    # 输出系统的平均负载: 1 分钟, 5 分钟, 15 分钟
    print psutil.getloadavg()
    print [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]


def memoryStats():
    # 统计内存使用的相关信息,输出信息为字节
    print psutil.virtual_memory().total / 1024 / 1024 / 1024
    print psutil.virtual_memory().percent
    print psutil.virtual_memory().available
    print psutil.version_info

    # 用于计算交换分区的使用情况
    print psutil.swap_memory()


def diskStats():
    # 统计磁盘分区的相关情况
    print psutil.disk_partitions()

    # 用于统计磁盘的使用情况,
    print psutil.disk_usage("/data/")
    print psutil.disk_usage("/")

    # 系统的 IO 统计信息
    print psutil.disk_io_counters(perdisk=False, nowrap=True)


def networkStats():
    # 输出全局的 网络 IO 统计信息
    #
    print psutil.net_io_counters()
    print psutil.net_io_counters(pernic=True)

    # 全局的 socket 套接字统计信息
    print psutil.net_connections()

    # 返回 网卡 设备分配的地址信息
    print psutil.net_if_addrs()

    # 返回网卡设备的速率信息
    print psutil.net_if_stats()


def sensorsStats():
    # 返回各种设备的温度信息
    # centos 上面不支持
    print psutil.sensors_temperatures(fahrenheit=False)

    # 风扇的速度信息
    print psutil.sensors_fans()

    # 电池的相关信息
    print psutil.sensors_battery()


def systemInfo():
    # 返回自 计算机元年开始计算到计算机启动一刻经历的秒数, 固定在启动的那一刻
    print psutil.boot_time()
    print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    # 返回当前登录的用户名
    print psutil.users()


def processStats():
    # 返回当前运行的所有的 pid 列表, 当进程很多很容易发生阻塞
    print psutil.pids()
    # 是否存在某个 pid 进程
    print psutil.pid_exists(2)
    # 通过 process_iter 逐个返回进程的相关信息
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline']):
        print proc.info


def main():
    processStats()


if __name__ == '__main__':
    main()
