# -*- coding: UTF-8 -*-

import re
from parsers.pager_parser import PagerParser
from parsers.blog_parser import BlogParser



class HtmlParser(object):

    def parse(self, page_url, html_text):
        if page_url is None or html_text is None:
            return None
        # http://www.cnblogs.com/sitehome/p/1
        pager_url_pat = r"sitehome/p/\d+"
        blog_url_pat = r"[\w\s-]{3,}/p/\d{6,}.html"
        urls = data = group = None
        if(re.search(pager_url_pat, page_url, re.I)):
            print 'PPPPPP ag eeeeee ======== ', page_url
            parser = PagerParser()
            urls, data, group = parser.parse(page_url, html_text)
        elif(re.search(blog_url_pat, page_url, re.I)):
            print 'BBBB looooooo ======== ', page_url
            parser = BlogParser()
            urls, data, group = parser.parse(page_url, html_text)

        return urls, data, group







