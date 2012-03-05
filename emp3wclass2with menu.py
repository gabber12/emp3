#                                                           Song Search And Download IN CONSOLE MODE
#--------------------------------------------------------------------------------------------------------------------------------------------------
#                                                          search and download songs

import urllib
import urllib2
import time

class emp3search:
    def __init__(self,keyword):
        self.site="http://emp3world.com/search.php"
        self.keyword=keyword
        self.type="mp3"
        self.result=[]

    def getUrl(self,page):
        self.data={'phrase':self.keyword,'type':self.type,'submit':'search','page':str(page)}
        url=self.site+"?"+urllib.urlencode(self.data)
        return url

    #opens the page in which all the search result are present
    def getPage(self,page):
        url=self.getUrl(page)
        req=urllib2.Request(url)
        page=urllib2.urlopen(req).read()
        return page

    #gets the results from the page and appends it in result
    def getResult(self,page):
        data=self.getPage(page)
        result=data.split('</div>')[-1]
        detail=""
        for i in xrange(4,35):
            try:
                s_result=result.split('<tr')[i]
                s1=s_result.split('<a href="')[1]
                link=s1.split('</a')[0]
                title=link.split('">')[1]
                search_link=link.split('">')[0]
                detail+="%d.)TITLE-%s LINK-%s\n" %(i-3,title,search_link)
            except IndexError:
                detail+="results over"  
        self.result.append(detail)
        
    #print the search result 
    #if downloaded directly the list
    #if not downloaded it calls getResult()
    def printResult(self,page):
        try:
            print self.result[page-1]
        except IndexError:
            self.getResult(page)
            print self.result[page-1]

    #returns the link of the selected songs page
    def getLink(self,page,number):
        try:
            total=self.result[page-1]
            tmp=total.split("%d.)TITLE-"%(number))[1]
            tmp1=tmp.split("LINK-")[1]
            link=tmp1.split("\n%d"%(number+1))[0]
            return link
        except IndexError:
            self.getResult(page)
            return self.getLink(page,number)


class download:
    def __init__(self,url):
        self.url=url

    #gets the download url from the song page
    #returns url and title
    def dowurl(self):
        url="http://www.emp3world.com"+self.url
        url=url.replace(" ","%20")
        req=urllib2.Request(url)
        site=urllib2.urlopen(req)
        
        page=site.read()
        
        junk=page.split('<h2><b>Download Now:</b> <a href="')[1]
        
        junk1=junk.split("rel=")[1]
        junk2=junk1.split("<u>")[1]
        title=junk2.split("</u>")[0]
        download_url=junk.split('"')[0]
        full_download_url="http://www.emp3world.com"+str(download_url)
        return full_download_url,title
        

    #supplied with url downloads file
    def download(self):
        url,title=self.dowurl()
        req=urllib2.Request(url)
        webfile=urllib2.urlopen(req)
        fp=file(title+".mp3","w")
        try:
            size=webfile.info()['content-length']
            i=0.0
            size=int(size)
            s=time.time()
            while(i<size):
                start=time.time()
                content=webfile.read(50000)
                fp.write(content)
                t=time.time()-start
                speed=50000/t
                i+=50000
                per=i/size*50
                print"-"*int(per)+">"+" "*(50-int(per))+"]"+str(speed/1024)+" Kbps "+" Time elapsed- "+str(time.time()-s)+"sec"
        except KeyError:
            print "Downloading..."
            content=webfile.read()
             
        fp.close()


def menu(keyword):
   
    s=emp3search(keyword)
    page=1
    s.printResult(page)
    while True:
        print "Menu-----------------\n1.)Download From This Page\n2.)scroll next page\n3.)Exit\n"
        choice=raw_input("enter choice")
        if choice=='1':
            number=int(raw_input())
            url=s.getLink(page,number)
            d=download(url)
            d.download()
        elif choice=='2':
            page+=1
            s.printResult(page)
        elif choice=='3':
            break;
                  
