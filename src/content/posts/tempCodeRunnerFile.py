import time
import requests
from pprint import pprint
import random
import hashlib

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://www.dxy.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.dxy.cn/',
    'sec-ch-ua': '"Not:A-Brand";v="8", "Chromium";v="156", "Microsoft Edge";v="156"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0',
    'cookie': 'JUTE_SESSION_ID=6599ae4d-31ee-49d7-853d-289f5b3ea9a3',
}

def random_str(length=8, charset_type="number"):
    charset = {
        "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "number": "0123456789",
    }[charset_type]
    return "".join(random.choice(charset) for _ in range(length))

params = {
    'cursor': 'AoJw88/8waEDKDUzODg2OTQ2',
    'source': '1',
    'pageSize': '10',
    'timestamp': f'{int(time.time() * 1000)}',
    'noncestr': random_str(),
    # 'sign': '0a1ba8f42c9e45d121ab674b725453c01991bc78',
}
app_sign_key = "4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3"
s = "&".join(f"{k}={params[k]}" for k in sorted(params))
s = f"appSignKey={app_sign_key}&{s}"
sign = hashlib.sha1(s.encode('utf-8')).hexdigest()
params['sign'] = sign

response = requests.get('https://bbsapi.dxy.cn/pc/case-bank/post/page', params=params, headers=headers)
pprint(response.json())