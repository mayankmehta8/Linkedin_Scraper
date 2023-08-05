import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from googlesearch import search
emails=[]
l1=[]
l2=[]
regex = r'/(http(s)?:\/\/)?([\w]+\.)?linkedin\.com\/(company)\/([-a-zA-Z0-9]+)\/*/gm'
def gsearch():
    l3=[]
    l4=[]
    query="transportation companies"
        
    for el in search(query, num_results=5, sleep_interval=2):
        l3.append(el)
        l4e=el.split("//")[-1]
        if l4e[-1]=='/':
            l4e=l4e[:-1]
        if not(l4e.find("/")==-1):
            l4e=l4e[:l4e.find("/")]
        l4.append(l4e)
    return (l3,l4)
class MailsSpider(CrawlSpider):
    
    
    ad=gsearch()
    name = 'mails'
    allowed_domains = ad[1]
    start_urls = ad[0]
    print(allowed_domains)
    print(start_urls)
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        for el in response.text.split(' '):
            if ("linkedin.com" in el):
                emails.append(el)

        for email in emails:
            lp= email.split("\"")
            for el in lp:
                if "linkedin" in el:
                    if  not( el in l1):
                        l1.append(el)
                        yield{
                            "URL": response.url,
                            "Email": el
                        }
