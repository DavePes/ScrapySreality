import scrapy
import json
import psycopg2
import time
# coding=utf8
class srealSpider(scrapy.Spider):
    name = 'sreal'
    allowed_domain = "www.sreality.cz"
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&tms=20914']

       
    def openPostgres(self):
        sqlDropTable = "DROP TABLE IF EXISTS sreal_content;"
        sqlCreateTable = "CREATE TABLE IF NOT EXISTS sreal_content ( \
    sreal_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),\
    jmeno text,\
    odkaz text, \
    CONSTRAINT sreal_content_pkey PRIMARY KEY (sreal_id) \
)"
        hostname = 'db'
        username = 'postgres'
        password = 'postgres'
        database = 'postgres'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=5432)
        self.cur = self.connection.cursor()
        self.cur.execute(sqlDropTable)
        self.cur.execute(sqlCreateTable)

    def closePostgres(self):
        self.cur.close()
        self.connection.close()
    def processItem(self, jmeno,odkaz):
        self.cur.execute("insert into sreal_content(jmeno,odkaz) values(%s,%s)",(jmeno,odkaz))
        self.connection.commit()
        #return item

    def parse(self, response):
        data = json.loads(response.body)
        data = data['_embedded']['estates']
        self.openPostgres()
        for jeden in data:
            jmeno = jeden['name']
            odkaz = jeden['_links']['dynamicDown'][0]['href']

            odkaz = odkaz.replace('{width}','400')
            odkaz = odkaz.replace('{height}','300')
            self.processItem(jmeno,odkaz)
        self.closePostgres()
        root = '/sreal/zpracovani_z_databaze.py'
        exec(open(root).read())
