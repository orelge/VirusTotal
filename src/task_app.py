import pandas as pd
import streamlit as st
from src.database.sqlite_database import SqlLiteDataBase
from src.main_config import DB_NAME, URLS_CLASSIFICATION_TABLE

sql_lite = SqlLiteDataBase()
sql_lite.create_db(DB_NAME)
urls_df = pd.read_sql(URLS_CLASSIFICATION_TABLE, sql_lite.connection)
st.write(urls_df)
