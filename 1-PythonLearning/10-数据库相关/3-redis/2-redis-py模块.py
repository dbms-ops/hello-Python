#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/17 14:19
# @user: Administrator
# @fileName: 2-redis-py模块.py
# @description: redis 模块 是 redis 官方提供的用于连接redis 的模块,支持redis 客户端命令, redis sentinel API,
#   redis cluster API
#


import redis


def connectRedis(host, port):
    redisClient = redis.Redis(host="localhost", port=port, db=0)
    print redisClient.info("Replication")["role"]
    redisServerInfo = redisClient.info("server")
    print redisServerInfo['redis_version']
    print redisServerInfo["redis_mode"]
    print redisClient.ping()
    print redisClient.config_get("maxmemory")
    print redisClient.slowlog_len()
    print redisClient.slowlog_get(10)
    print redisClient.cluster("info")


def connectSentinel(host, port):
    # 对于是否是 sentinel 节点,应该首先进行判断,避免不是 sentinel 节点;
    # 通过 redis mode 进行判断: redis_mode: sentinel; 或者 info sentinel 字段进行判断
    pass


def connectCluster(host, port):
    # 通过 redis mode 进行判断是都为 cluster, 如果是cluster 输出结果为: redis_mode:cluster;
    # 通过 info cluster 的 cluster_enabled 是否打开也可以进行判断
    pass


def main():
    connectRedis(host="127.0.0.1", port=4010)


if __name__ == '__main__':
    main()
