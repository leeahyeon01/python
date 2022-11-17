from flask import Flask, render_template
from dao import cursor
from flask import Flask,jsonify,request
from flask_cors import CORS


# 서버 띄우기
app = Flask(__name__)

CORS(app) 

app.config['JSON_AS_ASCII'] =False
#한글 글씨 깨질때 


@app.route('/')
def home(): 
     if request.method == 'GET': 
        sql =" select * from companylist"
        cursor.execute(sql) 
        res =cursor.fetchall()
        return res
      


if __name__ == '__main__':
    app.run(debug=True)
