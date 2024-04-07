import requests
import json


# 飞书接口文档：https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot
def get_text_data(text):
    data = {
        'msg_type': 'text',
        'content': {
            'text': text
        }
    }
    return json.dumps(data, ensure_ascii=True).encode('utf-8')


def get_post_data(title, content):
    data = {
        'msg_type': 'post',
        'content': {
            'post': {
                'zh_cn': {
                    'title': title,
                    'content': content
                }
            }
        }
    }
    return json.dumps(data, ensure_ascii=True).encode('utf-8')


def send_msg(url, data):
    # webhook
    header = {
        'Content-type': 'application/json',
        'charset': 'utf-8'
    }
    requests.post(url, data=data, headers=header)
