# coding=utf-8
# !/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
from Router.router import Application
from Settings.ai_config import ai_config
from Logger.ai_logger import get_logger
from traceback import format_exc
logger = get_logger(ai_config.GetStrValue('server', 'LOG_FILE_NAME'))

if __name__ == '__main__':
    try:
        ws_app = Application()
        server = tornado.httpserver.HTTPServer(ws_app)
        # 从配置文件读取ip和port
        server_ip = ai_config.GetStrValue('server', 'SERVER_IP')
        server_port = ai_config.GetIntValue('server', 'SERVER_PORT')
        #
        server.listen(server_port, address=server_ip)
        logger.info('AiServer启动成功!')
        print('server start')
        tornado.ioloop.IOLoop.instance().start()
    except:
        logger.error(format_exc())
