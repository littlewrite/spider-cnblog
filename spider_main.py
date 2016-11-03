# -*- coding: UTF-8 -*-

import pdb
import url_manager,html_downloader,html_parser, html_outputer

class SpiderMain(object):

    def __init__(self, max = 10):
        self.max = max
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        # pdb.set_trace()
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_text = self.downloader.download(new_url)
                print('#%d craw: %s' % (count, new_url))
                new_urls, new_data, group = self.parser.parse(new_url, html_text)
                if('pager' == group) :
                    self.outputer.collect_titles(new_data)
                elif('blog' == group):
                    self.outputer.collect_article(new_data)
                self.urls.add_new_urls(new_urls)
                count += 1
                if self.max == count:
                    break
            except BaseException, e:
                print e
                print 'craw failed'

        self.outputer.output_html()




if "__main__" == __name__:
    # root_url = "http://cl.c7e.biz/thread0806.php?fid=20" # adult literature
    root_url = "http://www.cnblogs.com/sitehome/p/1" # cnblog
    obj_spider = SpiderMain(20)
    obj_spider.craw(root_url)
