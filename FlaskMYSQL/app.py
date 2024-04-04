from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']='flaskDB'

mysql=MySQL(app)

@app.route('/', methods=['GET','POST'])
def hello():

    if request.method=='POST':
        username= request.form['username']
        email= request.form['email']

        cur=mysql.connection.cursor()

        cur.execute("INSERT INTO user_db (name,email) VALUES(%s,%s)",(username, email))
        mysql.connection.commit()
        cur.close()
        
        # return render_template('index.html')
        return "Data Insert Successfully"
    return render_template('index.html')


@app.route('/users')
def users():
    cur=mysql.connection.cursor()

    users=cur.execute("SELECT * FROM user_db")

    if users > 0:
        userDetails=cur.fetchall()

        return render_template('users.html', userDetails=userDetails)

if __name__=="__main__":
    app.run(debug=True)