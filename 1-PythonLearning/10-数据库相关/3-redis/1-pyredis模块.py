#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-16 22:53 
# user: lixun
# filename: 
# description: 
# 

import redis

def testRedis(port):
    redisClient = redis.Redis(host="127.0.0.1", port=4013, db=0)
    redisClient.ping()


def main():
    pass


if __name__ == "__main__":
    main()
