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


class WXBSpider(Spider):
    parms = {
        'cate': 0
    }
    BASE_URL = 'http://data.wxb.com/rankArticle'
    WEIXIN_PRIVACE_URL = 'http://mp.weixin.qq.com/mp/opshowpage?action=oplaw&id=26&t=operation/faq_index#wechat_redirect'

    def get_url_list(self):
        url_list = []
        for i in xrange(21):
            self.parms['cate'] = i
            url = WXBSpider.origin_url(self.BASE_URL, self.parms)
            self.url_list.append(url)
        return url_list

    def _get_wxb_xpath(self, id):
        xpath_str = '//*[@id="root"]/div/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/span/div/table/tbody/tr[' + str(id) + ']/td[1]/div/a'
        return xpath_str

    def get_result(self):

        urls_list = self.get_url_list()
        result = []
        for url in urls_list:
            html = WXBSpider.html(url)
            for j in xrange(1, 20):
                xpath_str = self._get_wxb_xpath(j)
                content = WXBSpider.select_from_xpath(html, xpath_str)
                if content[0].get('href') is not None:
                    result.append(content[0].get('href'))

        return result

    def filter_result(self, result):
        return [url for url in result if not WXBSpider.is_privace_weixin_url(url)]

    @staticmethod
    def is_privace_weixin_url(url, privace_url=WEIXIN_PRIVACE_URL):
        xpath_str = '/html/body/div/div[2]/p[2]/a'
        html = WXBSpider.html(url)
        content = WXBSpider.select_from_xpath(html, xpath_str)
        if content == []:
            return True
        else:
            href = content[0].get('href')

        return False if href == privace_url else True


def test():
    #1
    pass


def main():
    spider = WXBSpider()
    result = spider.get_result()
    result_filter = spider.filter_result(result)
    print result_filter

if __name__ == '__main__':
    test()
    # main()
