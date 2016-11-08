# -*- coding: UTF-8 -*-

import re
import logging
import urlparse
from bs4 import BeautifulSoup as butfsp


class HtmlParser(object):

    def __init__(self, config):
        self.config = config

    def _get_new_urls(self, current_url, soup):
        urls = []
        try:
            for url_config in self.config['url']:
                cur_url_config = self.config['url'][url_config]
                url_links = soup.select(cur_url_config['select'])
                for a in url_links:
                    try:
                        url = {}
                        url['url'] = urlparse.urljoin(current_url, a['href'])
                        url['title'] = a.text
                        if (None is cur_url_config['regex']) or re.search(cur_url_config['regex'], url['url'], re.I):
                            urls.append(url)
                    except Exception as e:
                        logging.error('Html Element Error!\nElement:'+a.text+'Error:'+e.message)

        except Exception as e:
            logging.error('html url parser error!\n URL:'+current_url+'Error:'+e.message)

        return urls

    def _get_new_data(self, current_url, soup):
        texts = []
        try:
            for content_config in self.config['content']:
                cur_content_config = self.config['content'][content_config]
                contents = soup.select(cur_content_config['select'])
                for content in contents:
                    try:
                        data = {}
                        data['url'] = current_url
                        data['title'] = ''
                        data['content'] = content.text
                        if (None is cur_content_config['regex']) or re.search(cur_content_config['regex'], content.text, re.I):
                            texts.append(data)
                    except Exception as e:
                        logging.error('Html Element Error!\nElement:' + content.text + 'Error:' + e.message)

        except Exception as e:
            logging.error('html data parser error!\n URL:' + current_url+'Error:'+e.message)

        return texts


    def parse(self, str_page_url, html_text):
        if str_page_url is None or html_text is None:
            return None

        soup = butfsp(html_text, 'html.parser', from_encoding='utf-8')
        return self._get_new_urls(str_page_url, soup), self._get_new_data(str_page_url, soup)







