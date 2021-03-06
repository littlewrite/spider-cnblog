# -*- coding: UTF-8 -*-

from storages.abstract_stroage import AbstractStorage as abstsg


class BlogStorage(abstsg):

    def _get_blog(self):
        pass

    def has_blog(self, blog):
        sql = u"select `cnblog_blog_id` from `cnblog_blogs` where `blog` = %s"
        re = self.query(sql, (blog['title'],))
        if(None == re or 0 == re):
            return False
        return True

    def has_new_blog(self):
        sql = u"select `cnblog_blog_id` from `cnblog_blogs` where `visited` = 0 and `deleted` = 0"
        re = self.query(sql)
        if (None == re or 0 == re):
            return False
        return True

    def save_blog(self, blog):
        if None is not blog:
            sql = u"insert into `cnblog_blogs` (`url`, `type`, `article`) value (%s, %s, %s)"
            return self.execute(sql, (blog['url'], blog['type'], blog['article']))

    def save_blogs(self, blogs):
        if None is not blogs and any(blogs):
            for blog in blogs:
                self.save_blog(blog)

    def get_new_blog(self):
        sql = u"select * from `cnblog_blogs` where `visited` = 0 and `deleted` = 0 limit 0"
        re = self.query(sql)
        sql = "update `cnblog_blogs` where `cnblog_blog_id` = %d" % re[0]['id']
        re = self.execute(sql)
        return re


