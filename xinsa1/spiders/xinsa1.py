import re


import scrapy
from bs4 import BeautifulSoup
from scrapy.http import  Request

from xinsa1.items import Xinsa1Item





class Myspider(scrapy.Spider):
    name='xinsa1'
    allowed_domains=['zjfgj.cn']
    bash_url='http://www.zjfgj.cn/allpg_BF3B4147E4C989FA_216_6B4D7028B861DF60F4A082D5E56483F5_'
    bashurl='.html'

    def start_requests(self):
        url=self.bash_url +'1'+self.bashurl
        yield Request(url, self.parse)

    def parse(self,response):
        bash_url = 'http://www.zjfgj.cn/allpg_BF3B4147E4C989FA_216_6B4D7028B861DF60F4A082D5E56483F5_'
        bashurl = '.html'
        max_num= int(BeautifulSoup(response.text,'lxml').find(id= "UCList_Pages").get_text())

        # print('最大值等于'+max_num)
        for num in range(1,55):
            url=bash_url+str(num)+bashurl
            # print(url)
            yield Request(url,callback=self.get_corp_name)

    def get_corp_name(self,response):
        # print(response.text)
        tables=BeautifulSoup(response.text,'lxml').find_all("table",background='images/zj08.gif')
        tr=tables.pop()

        # for td in tds:


        teams=tr.find_all("tr")
        for team in teams:
            # print(team)
            houseDeal=team.find_all("td")
            # for deal in houseDeal:
            #  print(deal.text)
            item=Xinsa1Item()
            item['corp_name']=houseDeal[0].text.strip()
            item['book_num']=houseDeal[1].text
            item['order_num'] = houseDeal[2].text
            item['amount'] = houseDeal[3].text
            item['ts'] = houseDeal[4].text
            print(item)
            yield item
             # print(novelname)
             # novlurl=td.find()
             # yield Request(novlurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novlurl})

