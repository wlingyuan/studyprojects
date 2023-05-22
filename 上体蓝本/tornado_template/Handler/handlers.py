# coding=utf-8
from tornado_template.MysqlDB.MyDbHelper import SQLManager
import tornado.web
import tornado.ioloop
class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('base.html')
class Login(tornado.web.RequestHandler):
    def post(self):
        db = SQLManager()
        stunumber = self.get_argument('stunumber')
        name = self.get_argument('name')
        college = self.get_argument('college')
        password = self.get_argument('password')
        select_sql = "select * from users where stunumber=('%s')"%(stunumber)
        result=db.single_query(select_sql)
        if result == None:
            self.write('用户不存在请输入正确的用户名和密码')
        else:
            user_info = result['password']
            if password == user_info:
                self.render('page1.html')
            else:
                self.write('用户名或密码错误')
class Register(tornado.web.RequestHandler):
    # def get(self):
    def post(self):
        db=SQLManager()
        stunumber = self.get_argument('stunumber')
        name = self.get_argument('name')
        college =self.get_argument('college')
        password=self.get_argument('password')
        select_sql = "select * from users where stunumber=('%s')" % (stunumber)
        result = db.single_query(select_sql)
        if result:
               self.write('用户已存在，请重新输入')
        else:
               insert_sql = "insert into users values('%s','%s','%s','%s')" % (stunumber, name, college, password)
               db.modify(insert_sql)
class Page1(tornado.web.RequestHandler):
    def get(self):
         self.render('page1.html')
class Release(tornado.web.RequestHandler):
    def get(self):
        self.render('release.html')
    def post(self):
        db = SQLManager()
        acname = self.get_argument('acname')
        score=self.get_argument('score')
        col = self.get_argument('col')
        insert_sql = "insert into activity(score,acname,col) values('%s','%s','%s')"%(score,acname,col)
        db.modify(insert_sql)
class Attend(tornado.web.RequestHandler):
    def get(self):
        self.render('attend.html')
    def post(self):
        db = SQLManager()
        acnumber = self.get_argument('acnumber')
        stunumber = self.get_argument('stunumber')
        name = self.get_argument('name')
        col = self.get_argument('col')
        if not (acnumber and stunumber and name and col):
            self.write('请将活动编号、学号、姓名、活动所属栏目填完整')
        else:
            insert_sql = "insert into attend (acnumber,stunumber,name,col) values('%s','%s','%s','%s')"%(acnumber,stunumber,name,col)
            db.modify(insert_sql)
class Inquire(tornado.web.RequestHandler):
    def get(self):
        self.render('inquire.html')
    def post(self):
        stunumber = self.get_argument("stunumber")
        name = self.get_argument("name")
        college = self.get_argument("college")
        if not (stunumber and name and college):
             self.write('请将学号、姓名、学院填完整')
        else:
           db = SQLManager()
           select_sql = "select * from scoreall1 where stunumber=('%s')"%(stunumber)
           a = db.single_query(select_sql)
           if  not a:
                self.write('请输入正确学号')
           else:
                score1=a['col1']
                score2=a['col2']
                score3=a['col3']
                score4=a['col4']
                score5= a['col5']
                score6=a['col6']
                all=a['all']
                self.render('inquirescore.html',a=stunumber,b=name,c=college,d=score1,e=score2,f=score3,g=score4,h=score5,i=score6,j=all)
class View(tornado.web.RequestHandler):
    def get(self):
        db = SQLManager()
        select_sql = "select * from activity"
        db.many_query(select_sql)
        a = db.many_query(select_sql)
        list1 = []
        for i in a:
            c = list(i.values())
            list1.append(c)
        self.render('view.html',list1=list1)


