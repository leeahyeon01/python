import pymysql 

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='aitrading_db',
                       charset='utf8')
cur = conn.cursor()
cur2 = conn.cursor()

# 💛회사명 입력시 month테이블 출력💛
def find_code(name):
 sql = "select market,code from companylist where name LIKE '"+ name +"%' "
 cur.execute(sql)
 rows = cur.fetchall()
 print(rows)
 for i in rows:
    #   print(i)
      market = i[0]
      s1= market.lower() #소문자로 바꿈
      code =i[1]
    #   print("'"+s1+"_"+code+"_m'" ) 
      table = (""+s1+"_"+code+"_m")
      print(table)
      sql2 = "SELECT open,high FROM "+table+" "
      print(sql2)
      cur2.execute(sql2)
      rows2 = cur2.fetchall()  
  
      for a in rows2:
        print(a)

find_code("더블유게임즈") 


# Q 테이블 조인해서 종목명,증가율,하락률,종가 (거래량을 순위)
conn.commit()

