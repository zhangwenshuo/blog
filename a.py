import tornado.ioloop
import tornado.web
import tornado.httpserver


# 主处理模块
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hi tornado, my name is zhangwenshuo")


if __name__ == "__main__":
    # 路由
    app = tornado.web.Application([
        (r"/", MainHandler)
    ])
    # 监听端口,多进程
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8000)
    http_server.start(num_processes=2)
    tornado.ioloop.IOLoop.instance().start()

