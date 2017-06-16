#coding:utf-8

import requests
from lxml import etree  # 导入xpath

import sys
import os
sys.path.append('..')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
reload(sys)
sys.setdefaultencoding('utf-8')

def get_html(url):

    ###content = urllib2.urlopen(url).read()
    ###return content

    hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

    html = requests.get(url, headers=hea)

    html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
    #print html.text
    return html.text
    pass

def select_from_xpath(html, xpath_str):

    selector = etree.HTML(str(html), parser=None, base_url=None)
    # 提取文本
    context = selector.xpath(xpath_str)
    #print '>>>>>>>contxt:', context
    #import pdb
    #pdb.set_trace()
    #print '>>>>>:', context[0].get('href')
    return context

def __get_wxb_xpath(id):
    xpath_str = '//*[@id="root"]/div/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/span/div/table/tbody/tr['+ str(id) + ']/td[1]/div/a'
    return xpath_str


def get_weixin_url_from_wxb(url = 'http://data.wxb.com/rankArticle?cate='):
    # http://data.wxb.com/rankArticle?cate=1
    urls_list = []
    for i in xrange(1, 21):
        base_url = url + str(i)
        html = get_html(base_url)
        for j in xrange(1,20):
            xpath_str = __get_wxb_xpath(j)
            content = select_from_xpath(html, xpath_str)
            if content[0].get('href') is not None:
                urls_list.append(content[0].get('href'))

    print urls_list

    pass

def is_vaild_weixin_url(url):
    xpath_str = '/html/body/div/div[2]/p[2]/a'
    html = get_html(url)
    content = select_from_xpath(html, xpath_str)
    if content == []:
        return True
    else:
        href = content[0].get('href')

    if href == 'http://mp.weixin.qq.com/mp/opshowpage?action=oplaw&id=26&t=operation/faq_index#wechat_redirect':
        return False
    else:
        return True

def test():
    #1
    #print 'start...'
    #url = 'http://data.wxb.com/rankArticle?cate=1'
    #url = 'http://www.cnblogs.com/bluestorm/archive/2011/06/20/2298174.html'
    #html = get_html(url)
    #pass

    #xpath_str = '//*[@id="root"]/div/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/span/div/table/tbody/tr[1]/td[1]/div/a'
    #'//*[@id="root"]/div/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div/span/div/table/tbody/tr[2]/td[1]/div/a'


    #select_from_xpath(html, xpath_str)

    # 3
    url = 'http://mp.weixin.qq.com/s?__biz=MzIwMTk1NjkyNA==&mid=2247484225&idx=1&sn=471f60388cb5a2b19d50361f5a4ed252&chksm=96e74812a190c104142d6bf865efdc4e4b06ab7fa2e173b6c9fe3a02fbdc6bd43a0a1084dbd0#rd'

    #url = 'http://mp.weixin.qq.com/s?__biz=MzA3NzcyNjIyNg==&mid=2650843219&idx=1&sn=f72038c33bc60487cd7d881d285e33be&chksm=84b99f2eb3ce163840420209ee3fbba7b0f0f1783917035a41bf019557e0946c4103a6a76c15#rd'
    print is_vaild_weixin_url(url) #filter_weixin_url(url)

    from data import weixin
    urls = weixin.weixin_doc_url
    filter_url = [url for url in urls if is_vaild_weixin_url(url)]
    print filter_url, len(filter_url)

def main():
    get_weixin_url_from_wxb()

if __name__ == '__main__':
    test()
    #main()