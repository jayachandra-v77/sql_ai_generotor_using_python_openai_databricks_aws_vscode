from databricks import sql
from config import *
import os
from dotenv import load_dotenv


load_dotenv()



def run_query(query):

    connection = sql.connect(
        server_hostname=DATABRICKS_HOST,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_TOKEN
    )

    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    return result

