#simple downloder
import urllib2
import urllib
import time
def download(url,title):
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
    
