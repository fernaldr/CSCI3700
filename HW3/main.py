from flask import Flask, render_template
import util
import psycopg2

app = Flask(__name__)

username='fernaldr16'
password='test'
host='127.0.0.1'
port='54321'
database='testdb1'

@app.route('/')
def index():
 # this is your index page
    # connect to DB
    """cursor, connection = util.connect_to_db(username,password,host,port,database)"""
    conn_string = "127.0.0.1:5000"
    db =  psycopg2.connect(conn_string)
    cursor = db.cursor
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT * from customer;")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:5]
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)

@app.route('/update_basket_a', methods=['POST'])
def update_basket_a():
    conn_string = "127.0.0.1:5000/api/update_basket_a"
    db =  psycopg2.connect(conn_string)
    curs = db.cursor()
    """cursor, connection = util.connect_to_db(username,password,host,port,database)"""
    ins_statement = f"""INSERT INTO basket_a ("PRIMARY KEY", "fruit_a") VALUES (5, 'Cherry');"""
    curs.execute(ins_statement)

@app.route('/unique', methods=['POST'])
def unique():
    conn_string = "127.0.0.1:5000/api/unique"
    db =  psycopg2.connect(conn_string)
    curs = db.cursor()
    """cursor, connection = util.connect_to_db(username,password,host,port,database)"""
    record = util.run_and_fetch_sql(curs, "SELECT * from customer;")
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in curs.description]
        # only use the first five rows
        log = record[:5]
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(db,curs)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)
    
if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)