import urllib2
from bs4 import BeautifulSoup

url = "https://schedule.sxsw.com/2018/artists"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
all_l = soup.find_all("h4")
print len("<h4><a href=/2018/artists/18906>") + 2
for l in all_l:
    s = str(l)
    print s[34:].split("<")[0]