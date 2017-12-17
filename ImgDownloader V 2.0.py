import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def main():
    depth = 5
    start_url = 'http://www.nenmj.com/1/5798.html'
    urllist = []
    for i in range(depth):
        url = start_url + '?page=' + str(i + 1)
        html = getHtml(url)
        reg = r'src="(.+?\.jpg)" alt="IMISS爱蜜社 166期 杨晨晨sugar"'
        imgre = re.compile(reg)
        html = html.decode('utf-8')  # python3
        imglist = re.findall(imgre, html)
        urllist.extend(imglist)
        x = 0
        for imgurl in urllist:
            urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
            x += 1
main()