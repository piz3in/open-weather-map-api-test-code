import requests
import mysql.connector
import json

# APIに接続するための情報
url = 'https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=669223c8adb361058677b90c36b64806&units=metric'

# API接続の実行
response = requests.get(url)

dataj = json.loads(response.text)

weather = dataj["weather"][0]
data = weather["main"]
print(data)
print(type(data))

# DBパラメータ
HOST = 'localhost'
PORT = 3306
USER = 'root'
PSWD = {password}
DB = 'api_test'
TBL = 'test_tb'


# データベース接続
conn = mysql.connector.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PSWD,
        database=DB
    )


sql = 'INSERT INTO ' + TBL +'(name)'+ ' VALUES (%s)'
cur = conn.cursor()
cur.execute(sql, data)
conn.commit()
cur.close()
