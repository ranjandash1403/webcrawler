from html.parser import HTMLParser
from urllib import parse
 # html parser parse through the html files for links
#we are inheriting HTMLParser to linkfinder class so that we can add functionality to the existing HTML parser

class Linkfinder(HTMLParser):
    def __init__(self,base_url,page_url):

        super().__init__() # for accessing parent class objects i.e HTMLparser
        self.base_url=base_url
        self.page_url=page_url
        self.links=set() # where full urls will be stored


    # all anchhor tag <a> href=</a> contains urls in
    #but the urls are relative like "/video_feed.php" so we  need to add base url to it fo get full url
    def handle_starttag(self, tag, attrs):

        if tag:
            #<a class="A TasksTask__title"
            # href="https://github.com/thenewboston-developers/Account-Manager/issues/356"
            # rel="noopener noreferrer" target="_blank">
            # Crawl for Banks &amp; Validators</a>
            ## we require href as attribute and url as value both are stored in attrs


            for (attributes,value) in attrs:
                # attrs gives a list of [(name,value)] eg>>>>>>[('href', 'https://www.cwi.nl/')].

                if attributes in ('href','src'):
                    url=parse.urljoin(self.base_url,value) # eg fb login page>>>https://www.fb.com/login>>>>www.fb.com(base_url)&& /login(value)
                    self.links.add(url) # add full link set
    def page_links(self):
        return self.links

