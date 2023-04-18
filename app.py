from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL HOST"] = "localhost"
app.config["MYSQL USER"] = "root"
app.config["MYSQL PASSWORD"] = "coderprem"
app.config["MYSQL DB"] = "crud"
app.config["MYSOL CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "select * from user"
    con.execute(sql)
    res = con.fetchall()
    return render_template("index.html", datas=res)


if __name__ == "__main__":
    app.run(debug=True)
