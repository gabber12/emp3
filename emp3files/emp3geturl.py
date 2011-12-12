#emp3site--2......downloader

import urllib2
def get_url(url):
    req=urllib2.Request(url)
    site=urllib2.urlopen(req)
    page=site.read()
    download_url=split(page)
    full_download_url="www.emp3world.com"+str(download_url)
    return full_download_url

def split(page):
    junk=page.split('<h2><b>Download Now:</b> <a href="')[1]
    url=junk.split('"')[0]
    return url
