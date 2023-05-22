# coding=utf-8

import logging
import logging.config
import os


# 获取绝对路径

BASE_DIR = os.path.dirname(__file__)
# BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
print('BASE_DIR_LOG', BASE_DIR)
print('CURRENT_DIR_LOG', os.path.abspath('.'))
CONFIG_FILE_PATH = os.path.join(BASE_DIR, "logger.ini")  # 配置文件名称
# CONFIG_FILE_PATH = os.path.join(BASE_DIR,'Config', "logger.ini")  # 配置文件名称   # -F 打包的情况
# CONFIG_FILE_PATH = os.path.join(BASE_DIR,'../Config', "logger.ini")  # 配置文件名称   # -D 打包的情况

logging.config.fileConfig(CONFIG_FILE_PATH)

print('日志配置文件加载成功！')


def get_logger(name=None):
    return logging.getLogger(name)
