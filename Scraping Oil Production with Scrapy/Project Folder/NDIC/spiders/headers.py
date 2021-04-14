# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import pandas as pd

df = pd.read_csv(r'C:\Users\johno\Python\CSVs\file_numbers.csv')
file_numbers = df['FileNo'].astype(str).tolist()

base_url = 'https://www.dmr.nd.gov/oilgas/feeservices/getwellprod.asp?filenumber='


class HeadersSpider(scrapy.Spider):
    name = 'headers'
    start_urls = [base_url + file_number for file_number in file_numbers]

    def parse(self, response):
        # inspect_response(response, self)
        yield {
            'File_Number': response.xpath("(//text()[contains(., 'NDIC File No: ')]//following-sibling::node()/text())[1]").get(),
            'Well_Name' : response.xpath("normalize-space((//text()[contains(., 'Current Well Name: ')]//following-sibling::node()/text())[1])").get(),
            'UWI' : response.xpath("(//text()[contains(., 'API')]//following-sibling::node()/text())[1]").get().replace("-",""),
            'Well_Type' : response.xpath("(//text()[contains(.,'Well Type')]//following-sibling::node()/span/text())[1]").get(),
            'Well_Status' : response.xpath("(//text()[contains(.,'Well Status')]//following-sibling::node()/span/text())[1]").get(),
            'Location' : response.xpath("(//text()[contains(., 'Location: ')]//following-sibling::node()/text())[1]").get(),
            'Latitude' : response.xpath("(//text()[contains(., 'Latitude: ')]//following-sibling::node()/text())[1]").get(),
            'Longitude' : response.xpath("(//text()[contains(., 'Longitude: ')]//following-sibling::node()/text())[1]").get(),
            'Current_Operator' : response.xpath("(//text()[contains(., 'Operator: ')]//following-sibling::node()/text())[1]").get(),
            'Completion_Date' : response.xpath("((//text()[contains(.,'Comp:')])[1]//following-sibling::node()/text())[1]").get(),
            'Total_Depth' : response.xpath("((//text()[contains(.,'Depth:')])[1]//following-sibling::node()/text())[1]").get(),
            'Spud_Date' : response.xpath("(//text()[contains(., 'Spud')]//following-sibling::node()/text())[1]").get(),
            'Perf_Interval' : response.xpath("((//text()[contains(., 'Perf')])[1]//following-sibling::node()/text())[1]").get().replace("=","-"),
            'Cum_Oil' : response.xpath("((//text()[contains(.,'Oil')])[1]//following-sibling::node()/text())[1]").get(),
            'Cum_Gas' : response.xpath("((//text()[contains(.,'Gas')])[1]//following-sibling::node()/text())[1]").get(),
            'Cum_Water' : response.xpath("((//text()[contains(.,'Water')])[1]//following-sibling::node()/text())[1]").get()
        }
