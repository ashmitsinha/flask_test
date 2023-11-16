# from flask import Flask, render_template,request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         # Perform signup logic here (e.g., store the user in a database)
#         # For simplicity, we'll just print the values for now
#         print(f"Username: {username}, Password: {password}")
#         return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
# app = Flask(__name__)


# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(name, email) VALUES (%s, %s)", (name, email))
#         mysql.cinnection.commit()
#         cur.close()
#         # Perform any processing with the form data here
#         return f"Submitted Form Data: Name - {name}, Email - {email}"

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect
# from flask_mysqldb import MySQL
# import yaml

# app = Flask(__name__)

# db = yaml.safe_load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)
# print(mysql)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         userDetails = request.form
#         name = userDetails['name']
#         email = userDetails['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
#         mysql.connection.commit()
#         cur.close()
#         return redirect('/users')
#     return render_template('index.html')

# # @app.route('/users')
# # def users():
# #     cur = mysql.connection.cursor()
# #     resultValue = cur.execute("SELECT * FROM users")
# #     if resultValue > 0:
# #         userDetails = cur.fetchall()
# #         return render_template('users.html',userDetails=userDetails)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# # db = yaml.safe_load(open('db.yaml'))#
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'flaskapp'

import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='root', host='localhost', database='flaskapp'
)
print(conn)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# mysql = MySQL(app)
# print(mysql)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        
        # Check if the connection is established

        cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/users')
    
    return render_template('index.html')
#
# @app.route('/users')
# def users():
#     # Check if the connection is established
#     with mysql.connection.cursor() as cur:
#         resultValue = cur.execute("SELECT * FROM users")
#         if resultValue > 0:
#             userDetails = cur.fetchall()
#             return render_template('index.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)