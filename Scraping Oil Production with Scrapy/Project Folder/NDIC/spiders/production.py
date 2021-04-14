# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import pandas as pd

df = pd.read_csv(r'C:\Users\johno\Python\CSVs\file_numbers.csv')
file_numbers = df['FileNo'].astype(str).tolist()

base_url = 'https://www.dmr.nd.gov/oilgas/feeservices/getwellprod.asp?filenumber='

class ProdSpider(scrapy.Spider):
    name = 'production'
    start_urls = [base_url + file_number for file_number in file_numbers]

    def parse(self, response):
        # inspect_response(response, self)
        rows = response.xpath("//table[@id='largeTableOutput']//tr")
        for row in rows:
            yield {
                'UWI' : response.xpath("(//text()[contains(., 'API')]//following-sibling::node()/text())[1]").get().replace("-",""),
                'Pool' : row.xpath('.//td[1]/text()').get(),
                'Date' : row.xpath('.//td[2]/text()').get(),
                'Days' : row.xpath('.//td[3]/text()').get(),
                'Oil' : row.xpath('.//td[4]/text()').get(),
                'Water' : row.xpath('.//td[6]/text()').get(),
                'Gas' : row.xpath('.//td[7]/text()').get()
            }
