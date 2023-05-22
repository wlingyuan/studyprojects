# coding=utf-8
import tornado.web
import tornado.ioloop
from tornado_template.Handler.handlers import Register
from tornado_template.Handler.handlers import Login
from tornado_template.Handler.handlers import IndexPageHandler
from tornado_template.Handler.handlers import Page1
from tornado_template.Handler.handlers import Release
from tornado_template.Handler.handlers import Attend
from tornado_template.Handler.handlers import Inquire
from tornado_template.Handler.handlers import View

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/login',Login),
            (r'/register',Register),
            (r'/page1',Page1),
            (r'/attend', Attend),
            (r'/release',Release),
            (r'/inquire',Inquire),
            (r'/view',View),
        ]
        settings = {
            'template_path':  "templates",
            'static_path':  'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)
