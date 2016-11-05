# -*- coding: UTF-8 -*-

import MySQLdb


class Singleton(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst=super(Singleton,cls).__new__(cls, *args, **kwargs)
        return cls._inst


class AbstractStorage(Singleton):

    db_handle = None

    def get_db(self):
        if(None == self.db_handle):
            self.db_handle = MySQLdb.connect('127.0.0.1', 'test', 'test', 'spider-cnblog')
            self.db_handle.set_character_set('utf8')
        return self.db_handle

    def execute(self, sql, quote = None):
        db = self.get_db()
        cursor = db.cursor()
        re = cursor.execute(sql, quote)
        db.commit()
        cursor.close()
        return re

    def query(self, sql, quote = None):
        db = self.get_db()
        cursor = db.cursor()
        re = cursor.execute(sql, quote)
        db.commit()
        re = cursor.fetchall()
        cursor.close()
        return re

    def __del__(self):
        if (None == self.db_handle):
            self.db_handle.close()