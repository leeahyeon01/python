import pymysql
import pandas as pd
import matplotlib.pyplot as plt  # 데이터를 시각화 할 수 있게 도와주는 라이브러리

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='aitrading_db',
                       charset='utf8')
cur = conn.cursor()


sql = "select day,close from kospi_950210_m"
cur.execute(sql)
rows = cur.fetchall()
print(rows)

x = []
y = []

for i in rows:
    x.append(i[0])
    y.append(i[1])
    print(x)

plt.plot(x, y)
plt.show()
