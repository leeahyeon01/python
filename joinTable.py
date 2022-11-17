import pymysql 

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='aitrading_db',
                       charset='utf8')
cur = conn.cursor()


