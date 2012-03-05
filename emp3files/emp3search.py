#search emp3world.com
import urllib
import urllib2
def search(keyword,page=1):
    data={'phrase':keyword,'type':'mp3','submit':'search','page':str(page)}
    url='http://www.emp3world.com/search.php'
    full_url=url+'?'+urllib.urlencode(data)
    req=urllib2.Request(full_url)
    page=urllib2.urlopen(req)
    data=page.read()
    result=data.split('</div>')[-1]
    split(result)
    num=raw_input("select the song")
    d_link,title=get(result,int(num))
    d_link=d_link.replace(' ','%20')
    return d_link,title
    
def split(result):
    for i in xrange(4,35):
        try:
            s_result=result.split('<tr')[i]
            s1=s_result.split('<a href="')[1]
            link=s1.split('</a')[0]
            title=link.split('">')[1]
            search_link=link.split('">')[0]
            print str(i-3)+".)"+str(title)+" link="+str(search_link)
            
        except IndexError:
            return "results over"
            
def get(result,num):
    try:
        s_result=result.split('<tr')[num+3]
        s1=s_result.split('<a href="')[1]
        link=s1.split('</a')[0]
        search_link=link.split('">')[0]
        title=link.split('">')[1]
        return search_link,title
    except IndexError:
        print "index out of range"


    
