from flask import Flask, render_template, request,redirect, url_for, session
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'oldtown'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUser(firstName, lastName, email) VALUES (%s, %s, %s)",
         (firstName, lastName,email))
        mysql.connection.commit()
        cur.close()
        return render_template('submit.html')
    return render_template('index.html')

@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
    return render_template("clubs.html")

@app.route('/member', methods=['GET', 'POST'])
def member():
    if request.method == "POST":
        details = request.form
        firstname = details['fname']
        lastname = details['lname']
        email = details['email']
        pnum = details['pnum']
        password = details['password']
        cpassword = details['cpassword']
        gender = details['gender']
        branch = details['branch']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO register(firstname, lastname, email, pnum,password,cpassword,gender,branch) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)", (firstname, lastname,
        email,pnum,password,cpassword,gender,branch))
        mysql.connection.commit()
        cur.close()
        return render_template('submit.html')
    return render_template("member.html")



if __name__ == '__main__':
    app.run()