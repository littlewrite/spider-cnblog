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

    def collect_article(self, data):
        if data is None:
            return None
        self.article.append(data)

    def output_html(self):
        file_out = open('out.titles.html', 'w')
        file_out.write("<html>")
        file_out.write("<head><title>爬取结果</title></head>")
        file_out.write("<body>")
        file_out.write("<ul>")
        for data in self.titles:
            file_out.write("<li>%s</li>" % data['title'].encode('utf-8'))
        file_out.write("</ul>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()

        file_out = open('out.article.html', 'w')
        file_out.write("<html>")
        file_out.write("<head><title>爬取结果</title></head>")
        file_out.write("<body>")
        file_out.write("<table>")
        for data in self.article:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data['title'].encode('utf-8'))
            file_out.write("<td>%s</td>" % data['content'].encode('utf-8'))
            file_out.write("</tr>")
        file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")
        file_out.close()