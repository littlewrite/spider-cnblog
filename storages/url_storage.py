# -*- coding: UTF-8 -*-

from storages.abstract_stroage import AbstractStorage as abstsg


class UrlStorage(abstsg):

    def _get_url(self):
        pass

    def has_url(self, url):
        sql = u"select `url_id` from `urls` where `url` = %s"
        re = self.query(sql, (url['url'],))
        if any(re):
            return True
        return False

    def has_new_url(self):
        sql = u"select `url_id` from `urls` where `visited` = 0 and `deleted` = 0"
        re = self.query(sql)
        if (None == re or 0 == re):
            return False
        return True

    def save_url(self, url):
        sql = u"insert into `urls` (`url`, `title`, `visited`) value (%s, %s, %s)"
        return self.execute(sql, (url['url'], url['title'], 0))

    def save_urls(self, urls):
        for url in urls:
            if not self.has_url(url):
                self.save_url(url)

    def get_new_url(self):
        sql = u"select * from `urls` where `visited` = 0 and `deleted` = 0 limit 0"
        re = self.query(sql)
        sql = u"update `urls` where `url_id` = %s"
        re = self.execute(sql, (re[0]['id'],))
        return re
