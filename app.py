import sqlite3
from flask import Flask , render_template , redirect , request
#flaskのflask,render_templateを使用します宣言
app = Flask(__name__)

@app.route("/test")
def test():
    name = "flask"
    print("いけてます！！")
    return render_template("test.html",name = name)

@app.route("/greet/<text>")
def hello(text):
    return text + "さん、仲良くしてね"

@app.route("/dbtest")
def dbtest():
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
    c.excute("select name , age , address from users where id = 1")
    
    user_info = c.fetchone()
    c.close()
    return render_template("dbtest.html , user_info = user_info")
    
# @app.route("/add , methods=["GET"])
#     def add_get():
    
    
@app.route("/list")
def task_list():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("select id ,task from task ")
    task_list = []
    for row in c.fetchall():
        task_list.append({"id":row[0], "task":row[1]})
    c.close()
    return render_template("list.html" , task_list = task_list)


@app.route("/del/<int:id>")
def del_task(id):
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("delete from task where id =?",(id,))
    conn.commit()
    conn.close()
    return redirect("/list")

@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("select task from task where id = ?",(id,))
    task = c.fetchone()
    conn.close()
    return render_template("edit.html",task = task)

@app.route("/edit" , methods = ["POST"]) 
def update_task():
    item_id = request.form.get("task_id")
    item_id = int(item_id)
    task = request.form.get("task")
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("update task set task = ? where id = ?",(task , item_id))
    task = c.fetchone()
    conn.close()
    return redirect("/list")



if __name__ == "__main__":
    #サーバーを起動するよ
    app.run(debug=True)
    #デバッグモードを有効にするよ