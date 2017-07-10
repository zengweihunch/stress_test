# coding:utf-8
import requests
from lxml import etree

import sys
import os
from abc import abstractmethod

import requests
sys.path.append('..')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
reload(sys)
sys.setdefaultencoding('utf-8')


class Spider(object):
    HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}


    @staticmethod
    def html(url, head=HEAD):
        # 适用于静态页面的爬取
        html = requests.get(url, headers=head)
        html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
        return html.text

    @staticmethod
    def response(url):
        # 适用于爬带返回值页面
        return requests.get(url).json()

    def select_from_xpath(self, html, xpath_str):
        selector = etree.HTML(str(html), parser=None, base_url=None)
        context = selector.xpath(xpath_str)
        return context

    @staticmethod
    def origin_url(root_url, param=None):
        if param is not None and param != {}:
            url_param = '&'.join(['%s=%s' % (key.lower(), param[key]) for key in sorted(param)])
            url = root_url + '?' + url_param
        else:
            url = root_url
        return url

    def dedup(self, results):
        return list(set(results))

    def save_result(self, result, file_path = ''):
        # todo
        pass

    @abstractmethod
    def filter_result(self, result):
        return result

    @abstractmethod
    def get_result(self):
        result = []
        return result