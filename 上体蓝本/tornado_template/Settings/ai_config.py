# coding=utf-8
# !/usr/bin/env python

import os
import configparser


# 获取绝对路径
BASE_DIR = os.path.dirname(__file__)
# BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
#print('BASE_DIR', BASE_DIR)
CONFIG_FILE_PATH = os.path.join(BASE_DIR, "config.ini")
#CONFIG_FILE_PATH = os.path.join(BASE_DIR, 'Config',"config.ini") # -F 打包的情况
#CONFIG_FILE_PATH = os.path.join(BASE_DIR, '../Config',"config.ini")   # -D 打包的情况
class AiConfig:
    # 初始化
    def __init__(self):
        self.sFile = CONFIG_FILE_PATH
        try:
            self.conf = configparser.ConfigParser()
            self.conf.read(self.sFile)
            self.GetDBConfig()
            print('系统配置文件加载成功！')
        except Exception as err:
            raise

    # 判断sections是否存在
    def isExistsSection(self, sections):
        if self.conf.has_section(section=sections):
            return True
        else:
            return False

    # 判断option是否存在
    def isExistsOption(self, section, option):
        if self.conf.has_option(section=section, option=option):
            return True
        else:
            return False

    # 获取配置信息的数据，返回string类型
    def GetStrValue(self, section, option):
        try:
            value = self.conf.get(section, option)
            return value
        except Exception:
            return 0

    # 获取配置信息的数据，返回int类型
    def GetIntValue(self, section, option):
        try:
            value = self.conf.getint(section, option)
            return value
        except Exception:
            return 0

    # 获取配置信息的数据，返回float类型
    def GetFloatValue(self, section, option):
        try:
            value = self.conf.getfloat(section, option)
            return value
        except Exception:
            return 0

    # 获取配置信息的数据，返回bool类型
    def GetBoolValue(self, section, option):
        try:
            value = self.conf.getboolean(section, option)
            return value
        except Exception:
            return 0

    # 修改更新数据
    def UpdateValue(self, section, option, value):
        try:
            self.conf.set(section, option, value)
            with open(self.sFile, 'r+') as f:
                self.conf.write(f)
        except Exception:
            return False

    # 添加数据
    def AddValue(self, section, option, value):
        try:
            self.conf.add_section(section)
            self.conf.set(section, option, value)
            with open(self.sFile, 'r+') as f:
                self.conf.write(f)
        except Exception:
            return False

    # 获取数据库配置信息
    def GetDBConfig(self):
        try:
            self.ip = self.GetStrValue('db', 'IP')
            self.port = self.GetIntValue('db', 'PORT')
            self.dbname = self.GetStrValue('db', 'DBNAME')
            self.username = self.GetStrValue('db', 'USERNAME')
            self.dbpwd = self.GetStrValue('db', 'PASSWORD')
            self.charset = self.GetStrValue('db', 'CHARSET')
        except:
            pass


ai_config = AiConfig()
