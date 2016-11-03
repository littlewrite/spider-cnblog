# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup as butfsp
import urlparse
import abstract_parser


class PagerParser(abstract_parser.AbstractParser):

    def _get_new_urls(self,current_url, soup):
        urls = set()
        data = {}
        article_links = soup.find_all('a', class_='titlelnk')
        for a in article_links:
            url = a['href']
            urls.add(urlparse.urljoin(current_url, url))
            data['title'] = a.text
            data['content'] = ''
        pager_links = soup.find_all('a', class_='middle')
        for a in pager_links:
            url = a['href']
            urls.add(urlparse.urljoin(current_url, url))
        return urls, data

    def _get_new_data(self, current_url, soup):
        return None

    def parse(self, current_url, html):
        if current_url is None or html is None:
            return None
        soup = butfsp(html, 'html.parser', from_encoding = 'utf-8')
        urls, data = self._get_new_urls(current_url, soup)
        return urls, data, 'pager'
