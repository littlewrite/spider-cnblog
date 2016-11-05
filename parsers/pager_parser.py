# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup as butfsp
import urlparse
import abstract_parser


class PagerParser(abstract_parser.AbstractParser):

    def _get_new_urls(self,current_url, soup):
        urls = []

        article_links = soup.find_all('a', class_='titlelnk')
        for a in article_links:
            url = {}
            url['url'] = urlparse.urljoin(current_url, a['href'])
            url['title'] = a.text
            urls.append(url)

        pager_links = soup.find_all('a', class_='middle')
        for a in pager_links:
            url = {}
            url['url'] = urlparse.urljoin(current_url, a['href'])
            url['title'] = a.text
            urls.append(url)

        return urls

    def _get_new_data(self, current_url, soup):
        return {}

    def parse(self, current_url, html):
        if current_url is None or html is None:
            return None
        soup = butfsp(html, 'html.parser', from_encoding = 'utf-8')
        return self._get_new_urls(current_url, soup), self._get_new_data(current_url, soup), 'pager'
