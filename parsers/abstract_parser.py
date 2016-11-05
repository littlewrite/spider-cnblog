# -*- coding: UTF-8 -*-


class AbstractParser:

    def _get_new_urls(self, page_url, soup):
       pass

    def _get_new_data(self, page_url, soup):
        pass

    def parse(self, page_url, html_text):
        pass