import json
from flask import request
from dongpo import config


# 参考文档：https://blog.csdn.net/songlh1234/article/details/83381642
# 登录接口，需要传url、username、passwd
def login():
    # 获取通过url请求传参的数据
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')

    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        if username == config.username and pwd == config.pwd:
            result = {'code': 200, 'message': '登录成功'}
            return json.dumps(result, ensure_ascii=False)  # 将字典转换为json串, json是字符串
        else:
            result = {'code': -1, 'message': '账号密码错误'}
            return json.dumps(result, ensure_ascii=False)
    else:
        result = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(result, ensure_ascii=False)
