import pymysql 

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='aitrading_db',
                       charset='utf8')
cur = conn.cursor()
cur2 = conn.cursor()

# πνμ¬λͺ μλ ₯μ monthνμ΄λΈ μΆλ ₯π
def find_code(name):
 sql = "select market,code from companylist where name LIKE '"+ name +"%' "
 cur.execute(sql)
 rows = cur.fetchall()
 print(rows)
 for i in rows:
    #   print(i)
      market = i[0]
      s1= market.lower() #μλ¬Έμλ‘ λ°κΏ
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

find_code("λλΈμ κ²μμ¦") 


# Q νμ΄λΈ μ‘°μΈν΄μ μ’λͺ©λͺ,μ¦κ°μ¨,νλ½λ₯ ,μ’κ° (κ±°λλμ μμ)
conn.commit()

