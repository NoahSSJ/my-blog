import requests
import re
import random
import json
from pprint import pprint
from pathlib import Path

class TencentCaptchaCrack():
    session = requests.Session()
    session.headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://cloud.tencent.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Storage-Access': 'active',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0',
        'sec-ch-ua': '"Not:A-Brand";v="8", "Chromium";v="156", "Microsoft Edge";v="156"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    session.proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
    }

    def __init__(self, aid: str = '192962660', tkid: str = '1056529123'):
        self.aid = aid
        self.tkid = tkid
        self.static_url = 'https://turing.captcha.qcloud.com'

    def run(self):
        callback = f'_aq_{random.randint(000000, 999999)}'
        params = {
            'aid': self.aid,
            'protocol': 'https',
            'accver': '1',
            'showtype': 'popup',
            'ua': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE1Ni4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xNTYuMC4wLjA=',
            'noheader': '1',
            'fb': '1',
            'aged': '0',
            'enableAged': '0',
            'enableDarkMode': '0',
            'grayscale': '1',
            'clientype': '2',
            'cap_cd': '',
            'uid': '',
            'lang': 'zh-cn',
            'entry_url': 'https://cloud.tencent.com/product/captcha',
            'elder_captcha': '0',
            'js': '/tgJCap.2f0b2c65.js',
            'login_appid': '',
            'wb': '2',
            'tkid': self.tkid,
            'subsid': '1',
            'callback': callback,
            'sess': '',
        }

        response = self.session.get('https://turing.captcha.qcloud.com/cap_union_prehandle', params=params)
        pattern = rf"{callback}\((.*?)\)"
        match = re.search(pattern, response.text, re.S)
        if match:
            json_str = match.group(1)
            json_dict = json.loads(json_str)
            pprint(json_dict)
            md5 = json_dict['data']['comm_captcha_cfg']['pow_cfg']['md5']
            prefix = json_dict['data']['comm_captcha_cfg']['pow_cfg']['prefix']
            bg_url = self.static_url + json_dict['data']['dyn_show_info']['bg_elem_cfg']['img_url']
            bg_path = Path(__file__).parent.resolve().joinpath('bg.png')
            bg_bytes = self.session.get(bg_url).content
            bg_path.write_bytes(bg_bytes)
            slide_url = self.static_url + json_dict['data']['dyn_show_info']['sprite_url']
            slide_path = Path(__file__).parent.resolve().joinpath('slide.png')
            slide_bytes = self.session.get(slide_url).content
            slide_path.write_bytes(slide_bytes)
            y = json_dict['data']['dyn_show_info']['fg_elem_list'][1]['init_pos'][0]
            sess = json_dict['sess']
            

a = TencentCaptchaCrack().run()