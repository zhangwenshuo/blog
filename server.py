from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
import tornado.httpserver


# 主处理模块
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("好看的皮囊千篇一律,有趣的灵魂万里挑一")


if __name__ == "__main__":
    # 路由
    app = tornado.web.Application([
        (r"/", MainHandler)
    ])
    # 监听端口,多进程
    http_server = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    http_server.bind(8000)
    # 启动进程数
    http_server.start(2)
    # 启动Ioloop轮询监听
    IOLoop.instance().start()


