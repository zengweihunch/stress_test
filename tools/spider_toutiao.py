# coding:utf-8
import requests
from lxml import etree

import sys
import os
from spider_base import Spider
sys.path.append('..')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
reload(sys)
sys.setdefaultencoding('utf-8')


class ToutiaoSpider(Spider):

    KEYWORDS = ['杨幂', '姜丝达', '人工智能', '范冰冰', '张雨', '斐济', '飞机', '越南', '日本', '美年达', '小米', '网易', '百度', '阿里', '变形金刚', '优酷']
    BASE_URL = 'http://www.toutiao.com/search_content/'
    params = {
        'offset': 0,
        'format': 'json',
        'keyword': 'default',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
    }

    def get_url_list(self):
        url_list = []
        for keyword in self.KEYWORDS:
            self.params['keyword'] = keyword
            url = ToutiaoSpider.origin_url(self.BASE_URL, self.params)
            url_list.append(url)
        return url_list

    def get_result(self):
        url_list = self.get_url_list()
        result = []
        for url in url_list:
            res = ToutiaoSpider.response(url)
            data = res['data']
            # 去掉纯图片（has_gallery），含视频（has video），问答
            urls = [article.get('article_url') for article in data if article.get('article_url') and article['has_video'] is False and u'问答' not in article['source'] and article['has_gallery'] is False]
            result = result + urls
        return result

    def filter_result(self, results):
        # 去重复
        result_filter_list = ToutiaoSpider.dedup(results)

        # 过滤头条链接
        result_filter_toutiao_list = [url for url in result_filter_list if 'http://toutiao.com' in url]
        return result_filter_toutiao_list


if __name__ == '__main__':
    spider = ToutiaoSpider()
    result = spider.get_result()
    print '2:', len(result)
    print '3:', spider.filter_result(result)

