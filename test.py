# flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
import flask
from dongpo.service import base
from dongpo import manager
from dongpo import config

# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# http://127.0.0.1:8888/login?name=***&pwd=***
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    manager.query_house_info(config.test_config_init())
    return base.login()


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
