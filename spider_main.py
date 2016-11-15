# -*- coding: UTF-8 -*-

import url_manager,html_downloader,html_parser, html_outputer
from storages.url_storage import UrlStorage
from storages.blog_storage import BlogStorage
import sys

class SpiderMain(object):

    config = {}

    def __init__(self, config):
        self.config = config
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser(self.config['parser'])
        self.outputer = html_outputer.HtmlOutputer()
        self.url_storage = UrlStorage()
        self.blog_storage = BlogStorage()

    def craw(self, max = 10):
        count = 1
        self.urls.add_new_url(self.config['start'])
        while self.urls.has_new_url():
            try:
                str_new_url = self.urls.get_new_url()
                html_text = self.downloader.download(str_new_url)
                print('#%d craw: %s' % (count, str_new_url))
                obj_new_urls, new_data = self.parser.parse(str_new_url, html_text)
                if any(obj_new_urls):
                    self.url_storage.save_urls(obj_new_urls)
                    self.outputer.collect_titles(obj_new_urls)
                if any(new_data):
                    self.blog_storage.save_blogs(new_data)
                    self.outputer.collect_articles(new_data)

                self.urls.add_new_urlObjects(obj_new_urls)
                count += 1
                if max == count:
                    break
            except BaseException, e:
                print e
                print 'craw failed'

        self.outputer.output_html()

spider_config = {
    '0':{
        'start':'http://www.cnblogs.com/sitehome/p/1',
        'parser':{
            'url':{
                'blog':{
                    'select':'h3 > a[class=titlelnk]',
                    'regex':r"[\w\s-]{3,}/p/\d{6,}.html",
                },
                'pager':{
                    'select':'div[class=pager] > a',
                    'regex':r"sitehome/p/\d+",
                }
            },
            'content':{
                'title':{
                    'select':'div[class=post] a#cb_post_title_url',
                },
                'article':{
                    'select':'div[class=post] div#cnblogs_post_body',
                    'length': 400,
                }
            }
        }
    }
}

if "__main__" == __name__:
    obj_spider = SpiderMain(spider_config[sys.argv[1]])
    obj_spider.craw(int(sys.argv[2]))
