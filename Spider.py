
'''working:
we give a page link  from queue to spider it will go to that page
it will call link_finder to gather links from that html page and add links to waiting list or queue
once the page is completed it will add the link to crawled page since its done and then grab next link fron
queue and start doinng the same also and  check url with crawled file so that crawling should not get repeated for same url
for same url'''

#            queue            crawled

#spider1 #spider2 #spider3 #spider4 #spider5...

# all spider will share same queue and crawled file so that it can be fast aka =Multithreadibng

import requests
import urllib
import ssl
# help to open url
from Web_Crawling.link_finder import Linkfinder
from Web_Crawling.general import *
from urllib.request import urlopen


class spider:
    #we have make some class variable which can be accessed to each all instances
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''   # this is the file which will be stored in your storage
    crawled_file='' # this is the file which will be stored in your storage
    queue=set()     # this will be stored in RAM and can be appended later to queue file
                    # the above process of storing in variable is lot faster than everytime writing to a file
    crawled=set()   # also these set write to queue_file and crawled_file and read data from it eg. set_to_file & file_to_set

    def __init__(self,project_name,base_url,domain_name):
        #accessable all spiders
        spider.project_name=project_name
        spider.base_url=base_url
        spider.domain_name =domain_name
        spider.queue_file=spider.project_name + '/queue.txt'    #queue path
        spider.crawled_file=spider.project_name + '/crawled.txt'    #crawled path
        self.boot() # start start the spider
        self.crawl_page('first spider',spider.base_url)
        # at first 1 spider will crawl the home page and collect links in queue and then assign it to all spiders
    #boot() will be first spider which will be creating project directory (project_name),create empty queue and empty crawl file
    @staticmethod
    def boot():
        create_new_dir(spider.project_name)
        create_data_files(spider.project_name,spider.base_url)
        # queue set will be created
        # crewled set will be created
        spider.queue=file_to_set(spider.queue_file) # path=(spider.queue_file)
        spider.crawled=file_to_set(spider.crawled_file) # path=spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        # it will crawl the page_url and also its not in crawl.set()
        if page_url not in spider.crawled:
            print(thread_name+' now crawing '+page_url)
            print('in queue '+str(len(spider.queue)) + ' already crawled '+str(len(spider.crawled)))
            links_set=spider.gather_links(page_url)  # set of links is generated on current page
            spider.add_links_to_queue(links_set)
            # remove link from queue
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            # now update the queue_file and crawled_file by calling set_to_file()
            spider.update_files()


    @staticmethod
    def gather_links(page_url):
        #our link finder will take readable html as input so we need to convert given byte links to html_string which
        #which can be passed in link_finder
        html_string=''
        gcontext = ssl.SSLContext()
        try:
            from encodings.utf_8 import decode
            # reading is in byte mode so has to be decoded bfore passing in finder.feed()
            response = urllib.request.urlopen(page_url,context=gcontext)
            x = response.read()
            reader=x.decode()
            # create finder object for link finder and pass attributes

            finder = Linkfinder(spider.base_url,page_url)

            finder.feed(reader)    # it will pass the full html page in readble format
        except:
            print('Error:cannot crawl page')
            return ''
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links_set):
        #gather list if  not be in queue or crawled then add

        for urls in links_set:
            if urls in spider.queue:
                continue
            if urls in spider.crawled:
                continue
            if spider.domain_name not in urls:
                continue
            spider.queue.add(urls)

    @staticmethod
    def update_files():
    ## now update the queue_file and crawled_file by calling set_to_file()
        set_to_file(spider.queue,spider.queue_file)
        set_to_file(spider.crawled, spider.crawled_file)



