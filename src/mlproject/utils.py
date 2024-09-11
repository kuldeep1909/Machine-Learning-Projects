import pandas as pd
import os
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import sys
from dotenv import load_dotenv  # load all the data
import pymysql




# this is for generic functionality we can use whenever we want

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info('Reading Sql database started')
    try:
        mydb = pymysql.connect(
        host = host,
        user = user,
        password = password,
        db = db
        )

        logging.info("Connection established", mydb)
        df = pd.read_sql_query('Select * From students', mydb)
        print(df.head())

        return df
        






    except Exception as e:
        raise CustomException(e, sys)
