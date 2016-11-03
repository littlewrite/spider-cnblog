# -*- coding: UTF-8 -*-

import re
from parsers.pager_parser import PagerParser


class HtmlParser(object):

    def parse(self, page_url, html_text):
        if page_url is None or html_text is None:
            return None
        # http://www.cnblogs.com/sitehome/p/1
        pager_url_pat = r"sitehome/p/\d+"
        urls = None
        data = None
        if(re.search(pager_url_pat, page_url, re.I)):
            parser = PagerParser()
            urls, data = parser.parse(page_url, html_text)

        return urls,data







