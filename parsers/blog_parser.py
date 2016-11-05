# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup as butfsp
import abstract_parser


class BlogParser(abstract_parser.AbstractParser):

    def _get_new_urls(self,current_url, soup):
        return []

    def _get_new_data(self, current_url, soup):
        data = {}
        title = soup.find('a', id='cb_post_title_url')
        data['url'] = current_url
        data['title'] = title.text
        content = soup.find('div', id='cnblogs_post_body')
        data['content'] = content.text
        return data

    def parse(self, current_url, html):
        if current_url is None or html is None:
            return None
        soup = butfsp(html, 'html.parser', from_encoding = 'utf-8')
        return self._get_new_urls(current_url, soup), self._get_new_data(current_url, soup), 'blog'
