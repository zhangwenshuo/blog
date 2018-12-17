from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url
from tornado.httpserver import HTTPServer
import tornado.options
import tornado.autoreload
import json


# debug启动函数
tornado.autoreload.start()
# 定义默认端口
tornado.options.define('port', default=80, type=int, help="this is the port > for application")
tornado.options.define('project', default=[], type=str, multiple=True, help="it's a project dict")

# 主处理模块
class MainHandler(RequestHandler):
    def get(self):
        self.redirect('/regist', permanent=True)


# 索引处理模块
class IndexHandler(RequestHandler):
    def get(self):
        self.write("<a href='" + self.reverse_url("login") + "'>用户登录</a>")


# 注册处理模块
class RegisterHandler(RequestHandler):
    def initialize(self, title):
        self.title = title

    def get(self):
        self.write("注册业务处理:" + str(self.title))


# 登录处理模块
class LoginHandler(RequestHandler):
    def get(self):
        self.write("用户登录页面展示")

    def post(self):
        self.write("用户登录功能处理")


if __name__ == "__main__":
    # 引进全局变量配置
    tornado.options.parse_config_file('./config')
    print(tornado.options.options.port)
    # 路由
    app = Application([
        (r"/", MainHandler),
        (r"/regist", RegisterHandler, {'title': '会员注册'}),
        url(r"/login", LoginHandler, name="login")
    ])
    # 看不懂
    tornado.options.parse_command_line()
    # 监听端口,多进程
    http_server = HTTPServer(app)
    # 绑定端口
    http_server.bind(tornado.options.options.port)
    # 启动进程数
    http_server.start(num_processes=1)
    # 启动Ioloop轮询监听
    IOLoop.instance().start()


