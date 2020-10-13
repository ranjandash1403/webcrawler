from urllib.parse import urlparse

#domain name should be thenewboston.com sp that it will stay on that webpage rather than parsing through
#complete youtube,facebook etc
def get_domain_name(url):
    try:

        results=str(get_sub_domain_name(url)).split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''


# gives full url like(name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

print(get_domain_name('https://www.thenewboston.com/openings/Community'))