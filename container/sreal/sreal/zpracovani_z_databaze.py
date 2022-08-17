from jinja2 import Environment, FileSystemLoader
import psycopg2
import os
# coding=utf8
class Databaze():
    def openPostgres(self):
        hostname = 'db'
        username = 'postgres'
        password = 'postgres'
        database = 'postgres'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=5432)
        self.cur = self.connection.cursor()

    def closePostgres(self):
        self.cur.close()
        self.connection.close()

    def processItem(self):
        self.cur.execute("select jmeno, odkaz from sreal_content")
        return self.cur.fetchall()

dat = Databaze()
dat.openPostgres()
data = dat.processItem()
dat.closePostgres()


root = os.path.dirname(os.path.abspath(__file__))
templates_dir = root + '/../templates'
env = Environment( loader = FileSystemLoader(templates_dir) )


template = env.get_template('index.html')
jmenoOdkaz = []
for k in range(200):
    jmenoOdkaz.append([None,None])
    jmenoOdkaz[k][0] = data[k][0].replace("m\xb2","&#13217")
    jmenoOdkaz[k][1] = data[k][1]
filename = "/sreal/html/index.html"
with open(filename, 'w+') as fh:#, encoding='utf-8') as fh:
    fh.write(template.render(names = jmenoOdkaz))
#exec(open(root).read())
#f = open(filename,'r')
#print(f.read())
#f.close()
