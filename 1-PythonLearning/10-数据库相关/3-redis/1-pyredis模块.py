#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-16 22:53 
# user: lixun
# filename: 
# description: 
# 

import redis


def testRedis(port):
    redisClient = redis.Redis(host="127.0.0.1", port=port, db=0)
    info = {}
    print redisClient.ping()
    for line in str(redisClient.execute_command("info")).splitlines():
        if line.find(":") != -1:
            print line
            info[line.split(":")[0]] = line.split(":")[1]
    print len(info.keys())
    print info.get('role')
    print info.get("slave0")


def main():
    testRedis(4018)


if __name__ == "__main__":
    main()
