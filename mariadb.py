import pymysql

# 데이터베이스에 연결하기위해 pymysql의 connect 함수를 이용한다
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='aitrading_db',
                       charset='utf8')

# # db닫기
# conn.close()

# # 커서생성
# 일련의 데이터에 순차적으로 액세스 할 때 검색 및 현재 위치를 포함하는 데이터 요소이다.
# 쉽게 말해 쿼리 결과를 가져오면서 여러 컬럼 중에서 특정 컬럼의 위치정보도 포함하고 있는 셈이다.
cur = conn.cursor()

sql = "select market,name from companylist "
cur.execute(sql)
rows = cur.fetchall()


for i in rows:
    print(i)

conn.commit()
