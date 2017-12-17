import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def main():
    depth = 5
    start_url = ''
    urllist = []
    for i in range(depth):
        url = start_url + '?page=' + str(i + 1)
        html = getHtml(url)
        reg = r'src="(.+?\.jpg)" alt=""'
        imgre = re.compile(reg)
        html = html.decode('utf-8')  # python3
        imglist = re.findall(imgre, html)
        urllist.extend(imglist)
        x = 0
        for imgurl in urllist:
            urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
            x += 1
main()
