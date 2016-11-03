# -*- coding: UTF-8 -*-

import urllib2
import requests

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        try:
            proxies = {
                "http": "http://127.0.0.1:8888",
                "https": "http://127.0.0.1:8888",
            }
            headers = {
                'Cache-Control': 'no-cache',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
            }
            re = requests.get(url, headers=headers, proxies=proxies)
            if 200 != re.status_code:
                return None
            else:
                re.encoding = 'utf-8'
                return re.text
        except BaseException as e:
            print("Download HTML Error" + e.message)


    # def download(self, url):
    #     if url is None:
    #         return None
    #     try:
    #         proxy = urllib2.ProxyHandler({'http': 'http:127.0.0.1:8888'})
    #         opener = urllib2.build_opener(proxy)
    #         urllib2.install_opener(opener)
    #         response = urllib2.urlopen(url)
    #         if 200 != response.getcode():
    #             return None
    #         else:
    #             return response.read()
    #     except BaseException as e:
    #         print("Download HTML Error" + e.message)
