#!/data1/Python-2.7.4/bin/python
# coding=utf-8
# by zengjiabin

import argparse
import json
import logging.handlers
import os
import sys
import traceback

reload(sys)
sys.setdefaultencoding("utf-8")


### 定义格式化日志模块
def logger(Level="debug", logfile=None):
    Loglevel = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR, "warning": logging.WARNING,
                "critical": logging.CRITICAL}
    logger = logging.getLogger()
    if logfile is None:
        hdlr = logging.StreamHandler(sys.stderr)
    else:
        hdlr = logging.handlers.RotatingFileHandler(logfile, maxBytes=33554432, backupCount=2)
    formatter = logging.Formatter('%(asctime)s %(lineno)5d %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(Loglevel[Level])
    return logger


def toJson(msg, simple=True):
    if simple:
        msg = json.dumps(msg, ensure_ascii=False)
    else:
        msg = json.dumps(msg, ensure_ascii=False, indent=2, separators=(",", ":"))
    return msg


def lg(msg, level=1):
    if isinstance(msg, tuple): msg = list(msg)
    if isinstance(msg, dict) or isinstance(msg, list):
        msg = toJson(msg)
    if level == 1:
        log.info(msg)
    elif level == 0:
        log.debug(msg)
    elif level == 2:
        log.warning(msg)
    elif level == 3:
        log.error(msg)
    elif level == 4:
        log.critical(msg)
    else:
        log.info(msg)


###自定义函数块,
def myfunc():
    msg = {"code": 1, "message": "", "step": sys._getframe().f_code.co_name}
    try:

        msg["message"] = "success"
        msg["code"] = 0
    except:
        msg["message"] = "exectue error: " + traceback.format_exc()
    return msg


### 主函数
if __name__ == "__main__":
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    logdir, filename = os.path.split(os.path.abspath(sys.argv[0]))
    logfile = "/data/dba_logs/script/%s_logfile.log" % (filename.rstrip(".py"))
    os.popen("mkdir -p /data/dba_logs/script ").close()
    log = logger(logfile=logfile)
    parser = argparse.ArgumentParser(prog="函数名称", version="版本", description='说明', epilog="说明末尾展示,如写作者")
    parser.add_argument("-p", "--myport", action="store", type=int, required=True, default=0, help="server port")
    parser.add_argument("-l", "--mylist", action="append", type=str, required=False, default="", help="参数可以多次指定,保留在列表")
    parser.add_argument("-c", "--choice", action="store", type=int, required=False, default=0, choices=[0, 1, 2],
                        help="只能从列表中选择值")
    parser.add_argument("-b", "--mybool", action="store_true", default=False, help="布尔值")
    args = parser.parse_args()
    myport = args.myport
    mylist = args.mylist
    choice = args.choice
    mybool = args.mybool
    msg = myfunc()
    lg(msg)
    print toJson(msg)


