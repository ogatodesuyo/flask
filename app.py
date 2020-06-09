from flask import Flask , render_template

app = Flask(__name__)




if __name__ == "__main__":
    #サーバーを起動するよ
    app.run(debug=True)
    #デバッグモードを有効にするよ