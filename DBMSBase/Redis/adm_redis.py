#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-02-09 10:37 
# user: linux
# description: 脚本用于实现基本的redis管理功能
# 

import argparse
import commands
import logging


def log_redis(msg, level):
    """
    Function is used to record the log information of redis during startup
    :return:
    """
    filename = '/home/python/test.log'
    log_format = "%(asctime)s: %(levelname)s %(levelno)s %(message)s"
    DATE_FORMAT = "%Y-%m-%d  %H:%M:%S %p"
    logging.basicConfig(filename=filename, filemode='a', format=log_format, level=logging.DEBUG, datefmt=DATE_FORMAT)

    pass


def start_redis(ip='127.0.0.1', port=4010):
    """
    1 Check if the redis instance is started
    2 If started, echo the instance is already started
    3 If not started, call the start command to start the redis instance
    4 After executing the startup, determine whether the startup was successful or failed
    :return:
    """
    redis_start_str = 'Start redis:{} ....'.format(port)
    redis_ping = '/usr/bin/redis-cli -h {} -p {} ping 2>/dev/null'.format(ip, port)
    status, output = commands.getstatusoutput(redis_ping)
    if not status:
        print "redis ip:{}  port:{} is already started".format(ip, port)
        return status
    else:
        redis_start = 'su - redis -c "numactl --interleave=all /usr/local/redis_{}/src/redis-server ' \
                      '/data/redis_{}/redis{}.conf "'.format(port, port, port)
        status, output = commands.getstatusoutput(redis_start)
        if not status:
            print 'redis ip:{} port:{} is strating'.format(ip, port)
            return True
        else:
            print "Please check /data/redis_{}_log/redis{}.log".format(port, port)
            return False


def stop_redis(ip='127.0.0.1', port=4010):
    """
    1 Check if redis status is started
    2 If not started, the output is not started
    3 If it is already started, execute the stop command
    :return:
    """
    redis_ping = '/usr/bin/redis-cli -h {} -p {} ping 2>/dev/null'.format(ip, port)
    status, output = commands.getstatusoutput(redis_ping)
    if not status:
        redis_stop = '/usr/bin/redis-cli -h {} -p {} shutdown save 2>/dev/null'.format(ip, port)
        status, output = commands.getstatusoutput(redis_stop)
        if not status:
            print "redis ip:{} port:{} stop successfully".format(ip, port)
        else:
            print "redis ip:{} port:{} stop failed".format(ip, port)
        return status
    else:
        print "redis ip:{} port:{} is not started".format(ip, port)


def restart_redis(ip='127.0.0.1', port=4010):
    stop_redis(port=port)
    start_redis(port=port)


def conn_redis(ip='127.0.0.1', port=4010):
    """
    1 View the established connections between the instance and the port
    :return:
    """
    filename = "conn_redis_{}.log".format(port)
    connection_redis = "ss -t -a -n  -o state  established '( sport = :{} )' | egrep -vi 'address|{}'  " \
                       "".format(port, ip)
    status, output = commands.getstatusoutput(connection_redis)
    with open(filename, 'w') as fwrite:
        fwrite.write(output)
    return True


def show_process_redis(ip='127.0.0.1', port=4020):
    filename = "show_process_redis_{}.log".format(port)
    redis_show_process = '/usr/bin/redis-cli -h {} -p {} client list'.format(ip, port)
    status, output = commands.getstatusoutput(redis_show_process)
    with open(filename, 'w') as fwrite:
        fwrite.write('Redis {} current connections:\n'.format(port))
        fwrite.write(output)
    return True


def main():
    parser = argparse.ArgumentParser(description='redis management commands',
                                     epilog='writen by DBA,%(prog)s version 1.0')
    parser.add_argument('port', default=4010, type=int, help='port of the redis instance')
    parser.add_argument('choice', choices=['start', 'restart', 'stop', 'conn', 'process'],
                        help='Redis supported selection list')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    port = args.port
    choice = args.choice
    if choice == 'start':
        start_redis(port=port)
    elif choice == 'stop':
        stop_redis(port=port)
    elif choice == 'conn':
        conn_redis(port=port)
    elif choice == 'process':
        show_process_redis(port=port)
    elif choice == 'restart':
        restart_redis(port=port)
    else:
        return False


if __name__ == "__main__":
    main()
