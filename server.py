from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url
from tornado.httpserver import HTTPServer
import tornado.options
import tornado.autoreload
import json
import os



# debug启动函数
tornado.autoreload.start()
# 定义默认端口
tornado.options.define('port', default=80, type=int, help="this is the port > for application")
tornado.options.define('project', default=[], type=str, multiple=True, help="it's a project dict")


# 主处理模块
class MainHandler(RequestHandler):
    def get(self):
        path = './static/images/music/'
        items = os.listdir(path)
        self.render('./templates/index.html', title='My Title', items=items)


# 图片处理模块
class ImageHandler(RequestHandler):
    def get(self):
        name = self.get_argument('name')
        path = './static/images/music/%s' % name
        path1 = '/static/images/music/%s' % name
        items = os.listdir(path)
        self.render('./templates/music.html', path=path1, items=items )



if __name__ == "__main__":
    # 引进全局变量配置
    tornado.options.parse_config_file("./config")
    print(tornado.options.options.port)
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret" : 'aaa'
    }
    # 路由
    app = Application([
        (r"/", MainHandler),
        (r'/images/music', ImageHandler)
    ], **settings)
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


