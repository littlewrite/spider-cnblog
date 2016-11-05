# -*- coding: UTF-8 -*-

import url_manager,html_downloader,html_parser, html_outputer
from storages.url_storage import UrlStorage
from storages.blog_storage import BlogStorage


class SpiderMain(object):

    def __init__(self, max = 10):
        self.max = max
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.url_storage = UrlStorage()
        self.blog_storage = BlogStorage()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url['url'])
        while self.urls.has_new_url():
            try:
                str_new_url = self.urls.get_new_url()
                html_text = self.downloader.download(str_new_url)
                print('#%d craw: %s' % (count, str_new_url))
                obj_new_urls, new_data, group = self.parser.parse(str_new_url, html_text)
                if('pager' == group) :
                    self.url_storage.save_urls(obj_new_urls)
                    self.outputer.collect_titles(obj_new_urls)
                elif('blog' == group):
                    self.blog_storage.save_blog(new_data)
                    self.outputer.collect_article(new_data)

                self.urls.add_new_urlObjects(obj_new_urls)
                count += 1
                if self.max == count:
                    break
            except BaseException, e:
                print e
                print 'craw failed'

        self.outputer.output_html()




if "__main__" == __name__:
    # root_url = "http://cl.c7e.biz/thread0806.php?fid=20" # adult literature
    root_url = {'url':'http://www.cnblogs.com/sitehome/p/1','title':''} # cnblog
    obj_spider = SpiderMain(4000)
    obj_spider.craw(root_url)
