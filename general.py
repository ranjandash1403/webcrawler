import os
# new project for new folder
def create_new_dir(directory):
    # if project exist then dont create new project dir
    if not os.path.exists(directory):
        print('creating project',directory)
        os.makedirs(directory)
# create_new_dir(directory='gudu')

#the files in side project where 1 file contain queue to be crawled and 2 after crawling is completed it will in 2nd file
def create_data_files(project_name,base_url):
    # new website = new project
    # base dir= current wd
    #queue is file path here
    queue=project_name+'/queue.txt'
    crawled=project_name+'/crawled.txt'
    # check if the folder exits previously
    if  not os.path.isfile(queue):
        #write a file and create it
        # at start we have to give base url to start crawl
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        # no base url for crawled file else it will skip the base url itself at start
        write_file(crawled,'')


def write_file(filename,data_url):
    with open(filename,'w') as f:
        f.write(data_url)
# create_data_files('gudu','www.google.com')

#add data to existing file
def append_to_file(filename,data_url):
    with open(filename,'a') as f:
        f.write(data_url + '\n')


def del_file(filename):
    with open(filename,'w') as  f:pass
#for taking the queue url in a set so as to remove duplicates and then crawl one by one .

def file_to_set(path):
    results=set()
    with open(path,'rt') as f:
        for line in f:
            results.add(line.replace('\n','')) # deleting '/n' present in data appended  by append_to_file
    return results

# iterate through set and write t0 file with each new line it will take set i.e results and file to where it should be stored
#like add to queue if its new url else add to crawlwd if finished.
def set_to_file(results,file):
    # del_file(file)
    # iterate over links in results
    for link in results:
        append_to_file(file,link)