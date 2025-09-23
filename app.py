from flask import Flask, render_template, request, session, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# DB (for login/register)
# auth_db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="vikas",
#     database="",
#     autocommit=True
# )
# auth_cursor = auth_db.cursor()


@app.route("/")
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True, port=5010,host='0.0.0.0')
