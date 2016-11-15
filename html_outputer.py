#-*- coding: UTF-8 -*-


class HtmlOutputer(object):

    def __init__(self):
        self.titles = []
        self.article = []

    def collect_titles(self, titles):
        if titles is None or 0 == len(titles):
            return None
        for title in titles:
            self.titles.append(title)

    def collect_articles(self, data):
        if data is None or not any(data):
            return None
        for item in data:
            self.article.append(item)

    def output_html(self):
        html_body1 = u'''
<html>
    <head>
        <title>爬取结果</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    <body>'''
        html_body2 = u'''
    </body>
</html>'''
        html_content = u"<ul>"
        for data in self.titles:
            html_content += u"\n<li>%s</li>" % data['title']
        html_content += u"</ul>"

        file_out = open('out.titles.html', 'w')
        file_out.write(html_body1.encode('utf-8', 'ignore'))
        file_out.write(html_content.encode('utf-8', 'ignore'))
        file_out.write(html_body2.encode('utf-8', 'ignore'))
        file_out.close()

        html_content = u"<table>"
        for data in self.article:
            html_content += u"\n<tr>"
            html_content += u"\n<td>%s</td>" % data['type']
            html_content += u"\n<td>%s</td>" % data['article']
            html_content += u"</tr>"
        html_content += u"</table>"

        file_out = open('out.article.html', 'w')
        file_out.write(html_body1.encode('utf-8', 'ignore'))
        file_out.write(html_content.encode('utf-8', 'ignore'))
        file_out.write(html_body2.encode('utf-8', 'ignore'))
        file_out.close()