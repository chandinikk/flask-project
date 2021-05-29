from flask import Flask, render_template, request,redirect, url_for, session
from flask_mysqldb import MySQL
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sinchana@00'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)



mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sinchanakp090@gmail.com'
app.config['MAIL_PASSWORD'] = '8971345908'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        subject = details['subject']
        message=details['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUser(name,email, subject, message) VALUES (%s, %s, %s, %s)",
         (name,email, subject, message))
        mysql.connection.commit()
        cur.close()

        msg = Message(subject, sender = 'sinchanakp090@gmail.com', recipients = [email])
        msg.body ="Dear "+ name+ "!! You will here back from us soon !!!"
        mail.send(msg)
        return render_template('submit.html')
    return render_template('index.html')



@app.route("/")
#def index():
   #msg = Message('Hello', sender = 'sinchanakp090@gmail.com', recipients = ['nayaksanjita29@gmail.com'])
   #msg.body = "Hello Flask message sent from Flask-Mail"
   #mail.send(msg)
   #return "Sent"

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
    app.run(debug="true")