# -*- coding: UTF-8 -*-

import re
from parsers.pager_parser import PagerParser
from parsers.blog_parser import BlogParser


class HtmlParser(object):

    def parse(self, str_page_url, html_text):
        if str_page_url is None or html_text is None:
            return None
        # http://www.cnblogs.com/sitehome/p/1
        pager_url_pat = r"sitehome/p/\d+"
        blog_url_pat = r"[\w\s-]{3,}/p/\d{6,}.html"
        obj_urls = []
        data = group = None
        if(re.search(pager_url_pat, str_page_url, re.I)):
            print 'PPPPPP ag eeeeee ======== ', str_page_url
            parser = PagerParser()
            obj_urls, data, group = parser.parse(str_page_url, html_text)
        elif(re.search(blog_url_pat, str_page_url, re.I)):
            print 'BBBB looooooo ======== ', str_page_url
            parser = BlogParser()
            obj_urls, data, group = parser.parse(str_page_url, html_text)

        return obj_urls, data, group







