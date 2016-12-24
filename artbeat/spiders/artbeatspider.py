import time
import scrapy
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re


from exhibitrecs.items import artbeatItem

chromedriver = "/Users/meghajain/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

class exhibitspider(scrapy.Spider):
    name = "artbeatspider"
    
    
    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver)
        scrapy.Spider.__init__(self)
        self.links = []
  
    def start_requests(self):
        url  = 'http://www.nyartbeat.com/events/JustStarted'
        yield scrapy.Request(url = url, callback = self.mainpage)
        

    def mainpage(self, response):
     
        self.driver.get(response.request.url)
        
        for item in self.driver.find_elements_by_xpath("//ul[@id='events_list']//li"):
            self.links.append(item.find_element_by_xpath("./a").get_attribute('href'))
                
        for link in self.links:
            yield scrapy.Request(url = link, callback = self.showpage, dont_filter = True)
            
    
    def showpage(self, response):
        self.driver.get(response.request.url)
        
        show_item = artbeatItem()
        
        
        try:
            show_item["title"] = [self.driver.find_element_by_xpath("//h2[@class='event_title']").text]
        except:
            show_item["title"] = ["Blank"]
            
        
        try:
            find_artists = self.driver.find_element_by_xpath('//span[@class="artistname"]/a')
            artist = []
            for item in find_artists:
                artist.append(item.text)

            show_item["artist"] = [", ".join(artist)]
            
        except:
            show_item["artist"] = ["Blank"]

            
        try:
            show_item["brief_descript"] = [self.driver.find_element_by_xpath("//p[@class='intro_event']").text]
        except:
            show_item["brief_descript"] = ["Blank"]
        
        
        try:
            show_item["venue"] = [self.driver.find_element_by_xpath("//h3[@class='venue']").text]
        except:
            show_item["venue"] = ["Blank"]
        
        
        try:
            show_item["dates"] = [self.driver.find_element_by_xpath("//div[@class='full_details']//p").text]
        except:
            show_item["dates"] = ["Blank"]
          
        
        try:
            show_item["location"] = [re.sub('Address: ', '', self.driver.find_element_by_xpath("//div[@class='half_details'][@id='half_33']//p").text.split('\n')[0])]
        except:
            show_item["location"] = ["Blank"]

            
        ## get full description
        
        try:
            self.driver.find_element_by_xpath("//p[@id='readmoreLink']/a").click()
            full_descript = ''
            paragraphs = self.driver.find_elements_by_xpath("//p[@style='display: block;']")
            for i in range(len(paragraphs)):
                full_descript += paragraphs[i].text
            show_item["full_descript"] = [full_descript, ]
        except:
            show_item["full_descript"] = ["Blank"]
            
            
        try:
            image_link = self.driver.find_element_by_xpath("//img").get_attribute("src")
            show_item['image'] = image_link
        except:
            show_item["image"] = ["No image"]
           
        
        
        yield show_item
        
