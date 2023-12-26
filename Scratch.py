import mysql.connector
import pandas as pd
#from streamlit_autorefresh import st_autorefresh

def get_data():
    mydb = mysql.connector.connect(    #GEt The Data from the Database
        host="127.0.0.1",

        user="ramon",
        passwd="pythos",
        database="trial",
        port=3307,
    )
    
    sql_query = pd.read_sql(
       'SELECT * FROM trial.`data`',
        mydb,
    )

    data = pd.DataFrame(sql_query)

    
    return data
data = get_data()

print(data.head(5))

