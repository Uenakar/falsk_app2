#必要なモジュールのインポート
from flask import Flask

#Flaskのインスタンス化
app=Flask(__name__)

#ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def hell():
    return 'Hello World!'

#エントリーポイント
if __name__=='__main__':
    app.run()

    