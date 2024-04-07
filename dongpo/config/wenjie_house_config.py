from dongpo.service import client
from dongpo import config


def wenjie_config_init():
    shellConfigs = [
        client.ShellConfig(
            '绿地国际理想城四期-14000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba90ea100l3c3720043829070546/?sug=%E7%BB%BF%E5%9C%B0%E5%9B%BD%E9%99%85%E7%90%86%E6%83%B3%E5%9F%8E%E5%9B%9B%E6%9C%9F',
            97, 73, 14000 + 2000,
            config.wenjie_feishu_url, 0),
        client.ShellConfig(
            '绿地国际理想城五期-14000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba90ea100l3c3720050049162387/?sug=%E7%BB%BF%E5%9C%B0%E5%9B%BD%E9%99%85%E7%90%86%E6%83%B3%E5%9F%8E%E4%BA%94%E6%9C%9F',
            97, 71, 14000 + 2000,
            config.wenjie_feishu_url, 0),
        client.ShellConfig(
            '中建星光城二期-14000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba90ea100l3c3720039252092290/?sug=%E4%B8%AD%E5%BB%BA%E6%98%9F%E5%85%89%E5%9F%8E%E4%BA%8C%E6%9C%9F',
            99, 76, 14000 + 2000,
            config.wenjie_feishu_url, 0),
    ]
    return shellConfigs
