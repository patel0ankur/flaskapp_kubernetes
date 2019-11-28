from flask import Flask
from flask_mysqldb import MySQL
import os

#HOST = os.environ.get('MYSQL_SERVICE_HOST')

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_ROOT_PASSWORD'] = 'root_password'

mysql = MySQL(app)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM nflteams.team_colors''')
    rv = cur.fetchall()
    return str(rv)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
