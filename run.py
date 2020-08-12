from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'aws 홈페이지'


if __name__ == '__main__':
    # debug를 True를 하면 내용을 고치면  다시 서버를 재가동한다
    app.run(debug=True, host='0.0.0.0')
