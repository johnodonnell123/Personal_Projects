# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class SQLlitePipeline_Production(object):
   
    def open_spider(self,spider):
        self.connection = sqlite3.connect("Well_DataBase.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE prod_table(
                    UWI INT,
                    Pool TEXT,
                    Date DATE,
                    Days INT,
                    Oil INT,
                    Water INT,
                    Gas INT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self,spider):
        self.connection.close()
    
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO prod_table (UWI,Pool,Date,Days,Oil,Water,Gas) VALUES(?,?,?,?,?,?,?)
        ''', (
            item.get('UWI'),
            item.get('Pool'),
            item.get('Date'),
            item.get('Days'),
            item.get('Oil'),
            item.get('Water'),
            item.get('Gas')
        ))
        self.connection.commit()
        return item

class SQLlitePipeline_Headers(object):
   
    def open_spider(self,spider):
        self.connection = sqlite3.connect("Well_DataBase.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE header_table(
                    File_Number INT,
                    Well_Name TEXT,
                    UWI INT,
                    Well_Type TEXT,
                    Well_Status TEXT,
                    Location TEXT,
                    Latitude FLOAT,
                    Longitude FLOAT,
                    Current_Operator TEXT,
                    Completion_Date DATE,
                    Total_Depth INT,
                    Spud_Date DATE,
                    Perf_Interval TEXT,
                    Cum_Oil INT,
                    Cum_Gas INT,
                    Cum_Water INT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self,spider):
        self.connection.close()
    
    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO header_table (File_Number,Well_Name,UWI,Well_Type,Well_Status,Location,Latitude,Longitude,Current_Operator,Completion_Date,Total_Depth,
            Spud_Date,Perf_Interval,Cum_Oil,Cum_Gas,Cum_Water) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', (
            item.get('File_Number'),
            item.get('Well_Name'),
            item.get('UWI'),
            item.get('Well_Type'),
            item.get('Well_Status'),
            item.get('Location'),
            item.get('Latitude'),
            item.get('Longitude'),
            item.get('Current_Operator'),
            item.get('Completion_Date'),
            item.get('Total_Depth'),
            item.get('Spud_Date'),
            item.get('Perf_Interval'),
            item.get('Cum_Oil'),
            item.get('Cum_Gas'),
            item.get('Cum_Water'),
        ))
        self.connection.commit()
        return item    

    
