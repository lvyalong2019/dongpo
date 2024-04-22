from dongpo.service import client
from dongpo import config

v1_threshold = 3000
v2_threshold = 2000


def v0_config_init():
    shellConfigs = [
        client.ShellConfig(
            '新城璞樾门第130-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l4bp0ep300c3720040449813267/?sug=%E6%96%B0%E5%9F%8E%E7%92%9E%E6%A8%BE%E9%97%A8%E7%AC%AC',
            130, 101, 16000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '新城璞樾门第109-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea115l3bp0ep300c3720040449813267/?sug=%E6%96%B0%E5%9F%8E%E7%92%9E%E6%A8%BE%E9%97%A8%E7%AC%AC',
            130, 101, 16000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '绿地国际理想城三期-13000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba125ea10000l3l4bp0ep300c3720075280507917/?sug=%E7%BB%BF%E5%9C%B0%E5%9B%BD%E9%99%85%E7%90%86%E6%83%B3%E5%9F%8E%E4%B8%89%E6%9C%9F',
            141, 105, 13000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '绿地国际理想城四期-14000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba110ea10000l3l4bp0ep300c3720043829070546/?sug=%E7%BB%BF%E5%9C%B0%E5%9B%BD%E9%99%85%E7%90%86%E6%83%B3%E5%9F%8E%E5%9B%9B%E6%9C%9F',
            131, 100, 14000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '绿地光谷中心城-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba110ea10000l3l4bp0ep300c3720027677856744/?sug=%E7%BB%BF%E5%9C%B0%E5%85%89%E8%B0%B7%E4%B8%AD%E5%BF%83%E5%9F%8E',
            123, 91, 16000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '联投驿园一期-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba120ea10000l3l4bp0ep300c3718091092225251/?sug=%E8%81%94%E6%8A%95%E9%A9%BF%E5%9B%AD',
            125, 95, 18000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '联投驿园二期-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba120ea10000l3l4bp0ep300c37000000069193/?sug=%E8%81%94%E6%8A%95%E9%A9%BF%E5%9B%AD%E4%BA%8C%E6%9C%9F',
            125, 97, 18000 + v1_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '光谷188国际社区-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba120ea10000l3l4bp0ep300c3714278395965542/?sug=%E5%85%89%E8%B0%B7188%E5%9B%BD%E9%99%85%E7%A4%BE%E5%8C%BA',
            141, 106, 18000 + v1_threshold,
            config.my_feishu_url, 1),
    ]
    return shellConfigs


def v1_config_init():
    shellConfigs = [
        client.ShellConfig(
            '新城璞樾门第-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l3l4bp0ep10000c3720040449813267/?sug=%E6%96%B0%E5%9F%8E%E7%92%9E%E6%A8%BE%E9%97%A8%E7%AC%AC',
            130, 101, 16000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '绿地国际理想城三期-13000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3720075280507917/?sug=%E7%BB%BF%E5%9C%B0%E5%9B%BD%E9%99%85%E7%90%86%E6%83%B3%E5%9F%8E%E4%B8%89%E6%9C%9F',
            141, 105, 13000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '绿地国际理想城四期-14000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3720043829070546/?sug=%E7%BB%BF%E5%9C%B0%E5%9B%BD%E9%99%85%E7%90%86%E6%83%B3%E5%9F%8E%E5%9B%9B%E6%9C%9F',
            130, 100, 14000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '绿地光谷中心城-17000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3720027677856744/?sug=%E7%BB%BF%E5%9C%B0%E5%85%89%E8%B0%B7%E4%B8%AD%E5%BF%83%E5%9F%8E',
            130, 103, 17000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '联投驿园一期-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3718091092225251/?sug=%E8%81%94%E6%8A%95%E9%A9%BF%E5%9B%AD',
            130, 103, 18000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '联投驿园二期-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c37000000069193/?sug=%E8%81%94%E6%8A%95%E9%A9%BF%E5%9B%AD%E4%BA%8C%E6%9C%9F',
            130, 103, 18000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '光谷188国际社区-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3714278395965542/?sug=%E5%85%89%E8%B0%B7188%E5%9B%BD%E9%99%85%E7%A4%BE%E5%8C%BA',
            130, 103, 18000 + v2_threshold,
            config.my_feishu_url, 1),
    ]
    return shellConfigs


def v2_config_init():
    shellConfigs = [
        client.ShellConfig(
            '中粮光谷祥云A区-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l3l4c3720039772205211/?sug=%E4%B8%AD%E7%B2%AE%E5%85%89%E8%B0%B7%E7%A5%A5%E4%BA%91A%E5%8C%BA',
            130, 100, 16000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '中建星光城二期-14000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000c3720039252092290/?sug=%E4%B8%AD%E5%BB%BA%E6%98%9F%E5%85%89%E5%9F%8E%E4%BA%8C%E6%9C%9F',
            130, 100, 14000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '新希望锦粼-12000',
            'https://wh.ke.com/ershoufang/co41lc2lc3c37000000078013/?sug=%E6%96%B0%E5%B8%8C%E6%9C%9B%E9%94%A6%E7%B2%BC%E4%B9%9D%E9%87%8C%E4%B8%80%E6%9C%9F',
            130, 100, 12000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '朗诗里程-12000',
            'https://wh.ke.com/ershoufang/co41lc2lc3c3711062903685/?sug=%E6%9C%97%E8%AF%97%E9%87%8C%E7%A8%8B',
            130, 100, 12000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '中建光谷之星-20000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba90ea10000l3l4c378367069474404/?sug=%E4%B8%AD%E5%BB%BA%E5%85%89%E8%B0%B7%E4%B9%8B%E6%98%9F',
            130, 100, 20000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '国采光立方-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3711100009391/?sug=%E5%9B%BD%E9%87%87%E5%85%89%E7%AB%8B%E6%96%B9',
            130, 100, 18000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '金地格林东郡-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3ba0ea10000l3l4c3711063729022/?sug=%E9%87%91%E5%9C%B0%E6%A0%BC%E6%9E%97%E4%B8%9C%E9%83%A1',
            130, 100, 16000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '保利时代北区-18000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l3l4c3720050698299526/?sug=%E4%BF%9D%E5%88%A9%E6%97%B6%E4%BB%A3%E5%8C%97%E5%8C%BA',
            130, 100, 18000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '坐标城九期-17000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l3l4c3710613625205264/?sug=%E9%95%BF%E5%9F%8E%E5%9D%90%E6%A0%87%E5%9F%8E%E4%B9%9D%E6%9C%9F',
            130, 100, 17000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '江城雅居-20000',
            'https://wh.ke.com/ershoufang/co41lc2lc3c3710637673247345/?sug=%E8%81%94%E6%83%B3%E6%B1%9F%E5%9F%8E%E9%9B%85%E5%B1%85',
            130, 100, 20000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '金地天悦-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l3l4c3711063505085/?sug=%E9%87%91%E5%9C%B0%E5%A4%A9%E6%82%A6',
            130, 100, 16000 + v2_threshold,
            config.my_feishu_url, 1),
        client.ShellConfig(
            '金地雄楚一号-15000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l3l4c3714958695035089/?sug=%E9%87%91%E5%9C%B0%E9%9B%84%E6%A5%9A%E4%B8%80%E5%8F%B7D%E5%8C%BA',
            130, 100, 15000 + v2_threshold,
            config.my_feishu_url, 1),
    ]
    return shellConfigs


def test_config_init():
    shellConfigs = [
        client.ShellConfig(
            '新城璞樾门第-16000',
            'https://wh.ke.com/ershoufang/co41lc2lc3l4bp0ep10000c3720040449813267/?sug=%E6%96%B0%E5%9F%8E%E7%92%9E%E6%A8%BE%E9%97%A8%E7%AC%AC',
            130, 101, 16000 + v1_threshold,
            config.my_feishu_url, 1),
    ]
    return shellConfigs
