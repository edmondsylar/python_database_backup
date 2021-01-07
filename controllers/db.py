import pymysql # import database library, in my case am using {pymysql}.
import pandas as pd
import os

# let get the file patht to later use it 
dir_path = os.path.dirname(os.path.realpath(__file__))
print ('current directory is {}'.format(dir_path))

conn = pymysql.connect(host="localhost", 
                        user="dev", 
                        password="password", 
                        database="ukwelys", 
                        charset='utf8mb4', 
                        cursorclass=pymysql.cursors.DictCursor) # we using the dictCursor because we need to have our outputs in dictionary object types.
cursor = conn.cursor()

def get_version():
    with conn.cursor() as cur:
        cur.execute('SELECT VERSION()')
        version = cur.fetchone()
        return version

def export_db(db):
    # this function is going to export the database passed in as the function's parameter.
    # we can name the file bassing on date of backup
    try:
        with cursor as cur:
            cur.execute('SELECT * FROM boards')
            data = cur.fetchall()
            df = pd.DataFrame(data)
            df.to_csv(r'{}\db-backups\{}.csv'.format(dir_path, 'file'), index=False)
            
            # print('exported database successfully')
            return 'exported database successfully'
    except Exception as err:
        print(err)
        return str(err)
    
    return False


