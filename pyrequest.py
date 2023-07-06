# https://haokan.baidu.com/

import requests
import json

def requestsURL():
    # url = 'https://haokan.baidu.com/'
    # url = 'https://www.bilibili.com/video/BV1Ra4y1w7NJ/?vd_source=6e44085d93bdee30f75d7e87f6aaf3fe'
    url = 'https://vd3.bdstatic.com/mda-pcrm3td4gxdc54z6/360p/h264/1679842609242090013/mda-pcrm3td4gxdc54z6.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1687336753-0-0-72c54247d2a9663756785c19036e95f8&bcevod_channel=searchbox_feed&pd=1&vt=1&cd=0&watermark=0&logid=0553547456&vid=9825206370131954701&pt=4&cr=0&sle=1&sl=1028&split=904399'

    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    # try:
        
    r = requests.get(url, headers=header).content
        # r.encoding = 'utf-8' # 设置响应编码为 UTF-8

        
    # except json.decoder.JSONDecodeError as e:
    #     print(f'Response was not valid JSON:{e}')
    #     r = {}
    # print(r)  # <Response [200]> 响应的状态码

    # 保存视频
    path = 'video'
    with open(path +'\'' + 'test.mp4', 'wb') as f:
        f.write(r)

def testPOST():
    url = 'https://haokan.baidu.com/'
    response = requests.get(url).content
    # print(response.text)
    with open('response.txt', 'wb') as f:
        f.write(response)


if __name__ == '__main__':
    # requestsURL()
    testPOST()