from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10041996'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.197.252.45'
mysql.init_app(app)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)


# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    	cur = mysql.connection.cursor() #create a connection to the SQL instance
    	cur.execute('''SELECT * FROM students''') # execute an SQL statment
    	rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    	return str(rv)      #Return the data in a string format


@app.route("/add")
def addRecord():
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO students (studentName, email) values ("third student", "thirdtudent@mydit.ie")''')
	cur.execute('''SELECT * FROM students''') # execute an SQL statment
	rv = cur.fetchall() #Retreive all rows returend by the SQL statment
	return str(rv)

@app.route("/update")
def updateRecord():
	cur = mysql.connection.cursor()
	cur.execute('''UPDATE students SET studentName = 'Raul Alvarez', email= 'raul.alvarez@mydit.ie' WHERE studentID = 1''')
	cur.execute('''SELECT * FROM students''') # execute an SQL statment
	rv = cur.fetchall() #Retreive all rows returend by the SQL statment
	return str(rv)

@app.route("/delete")
def deleteRecord():
	cur = mysql.connection.cursor()
	cur.execute('''DELETE FROM student WHERE studentID = 1''')
	cur.execute('''SELECT * FROM students''') # execute an SQL statment
	rv = cur.fetchall() #Retreive all rows returend by the SQL statment
	return str(rv)



if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

