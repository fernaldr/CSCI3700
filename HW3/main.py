from flask import Flask, render_template
import util


app = Flask(__name__)

# update to match your values
username='fernaldr16'
password='test'
host='127.0.0.1'
port='5432'
database='testdb1'


@app.route('/')

def index():
   
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    if recordA == -1 or recordB ==-1:
        
        print('Something is wrong with the SQL command')
    else:

        recordA = util.run_and_fetch_sql(cursor, "SELECT * from basket_a;")
        columns = [desc[0] for desc in cursor.description]
        logA = [dict(zip(columns, row)) for row in recordB]
        recordB = util.run_and_fetch_sql(cursor, "SELECT * from basket_b;")
        columns = [desc[0] for desc in cursor.description]
        logB = [dict(zip(columns, row)) for row in recordA]
        
    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', logA=logA, logB=logB)


if __name__ == '__main__':
	
    app.debug = True
    
    ip = '127.0.0.1'
    app.run(host=ip)