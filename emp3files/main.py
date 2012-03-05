#emp3main
import emp3geturl
import emp3search
import download

keyword=raw_input("enter the keyword to be searched")
page=raw_input("enter the page number")
url,title=emp3search.search(keyword,page)
downloadurl=emp3geturl.get_url("http://www.emp3world.com"+url)
download.download("http://"+downloadurl,title)
