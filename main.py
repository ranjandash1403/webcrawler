from threading import *
from queue import Queue
from Web_Crawling.general import *
from Web_Crawling.Spider import *
from Web_Crawling.domain import *

PROJECT_NAME='bentley'
HOMEPAGE="http://www.bentley.com/en"
DOMAINPAGE = get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=16
threading_queue=Queue()
# when first spider is called it will run and crrate project,crawled & queue all from homepage
spider(PROJECT_NAME,HOMEPAGE,DOMAINPAGE)

#Multiple spiders
def new_spiders():
    for _ in range(NUMBER_OF_THREADS):
    #create thread eath time
        t=Thread(target=work)
        t.start()
    import threading
    print(">>>>>>>>>>>>>>>>>>>>>>>",threading.active_count())

# all spiders except 1st spider has only 1 work that is crawlpage
def work():
    import threading
    while True:
        url=threading_queue.get()
        spider.crawl_page(threading.current_thread().getName(),url)
        threading_queue.task_done() # enqued task complated and is free


#put set of Qlist into thread_Q so as to create multiple threads
def add_to_threadQ(Qlist):
    for url in Qlist:
        threading_queue.put(url)
    #wait until 1 thread completes job
    threading_queue.join()
    crawl()

def crawl():
    #after spider 1 executes check data in QUEUE_FILE if its empty  thread finished else continue
    Qlist=file_to_set(QUEUE_FILE)
    if len(Qlist) > 0:
        print(str(len(Qlist))+"  remaining in queue")
        # if link exist crrate jobs
        add_to_threadQ(Qlist)

#first spiders need to be created then crawl else only main main thread will execute
new_spiders()
crawl()
