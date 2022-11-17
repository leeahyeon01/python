import pandas as pd 
import numpy as np #배열생성 
import pymysql 
from pandas import DataFrame 
#1년 평균  (2021.02.03 ~2022.02.03) 

# 데이터베이스에 연결하기위해 pymysql의 connect 함수를 이용한다
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='aitrading_db',
                       charset='utf8') 

close =[]
day =[]
def search_data(conn): 
    cur =conn.cursor() #커서 실행 
    sql = "SELECT close,day FROM kospi_006660_m WHERE day BETWEEN '2021-02-03' AND '2022-02-03'"
    cur.execute(sql) #쿼리를 실행 할 수 있다
    result = cur.fetchall() # 결과를 가져올 수 있다.
 #   print(result[0][0])
    conn.commit() 

    for i in result: 
       close.append(i[0])  
       day.append(i[1])
   
       
    print (close)
    print(type (day))
   # print (day[0:])
       



if __name__=="__main__":
    search_data(conn)  
  


#pandas로 배열 만들기 


test_day =["1","2","3","4","5","6","7","8","9","10","11","12"]
df = DataFrame(data=test_day, columns=close) 
print(df)

# data = [
#      ["037730", "3R", 1510, 7.36],
#      ["036360", "3SOFT", 1790, 1.65],
#      ["005760", "ACTS", 1185, 1.28],
#  ]

# columns = ["종목코드", "종목명", "현재가", "등락률"]
# df = DataFrame(data=data, columns=columns)
# # df = df.set_index('종목코드')
# print(df)