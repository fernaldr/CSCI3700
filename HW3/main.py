from flask import Flask, render_template
import util
import psycopg2

app = Flask(__name__)

username='fernaldr16'
password='test'
host='127.0.0.1'
port='54321'
database='testdb1'

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
    host=host,
    database="testdb1",
    user=username,
    password=password)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

"""@app.route('/')
def index():
 # this is your index page
    # connect to DB

    cursor, connection = util.connect_to_db(username,password,host,port,database)

    conn = psycopg2.connect(
    host=host,
    database="testdb1",
    user=username,
    password=password)

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


    cursor, connection = util.connect_to_db(username,password,host,port,database)


    ins_statement = fINSERT INTO basket_a ("PRIMARY KEY", "fruit_a") VALUES (5, 'Cherry');
    
    curs.execute(ins_statement)

@app.route('/unique', methods=['POST'])
def unique():
    conn_string = "127.0.0.1:5000/api/unique"
    db =  psycopg2.connect(conn_string)
    curs = db.cursor()
    
    
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    


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
    app.run(host=ip) """