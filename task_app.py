import pandas as pd
import streamlit as st

from src.database.sqlite_database import SqlLiteDataBase
from src.main_config import DB_NAME, URLS_CLASSIFICATION_TABLE
from src.main_deploy import MainDeploy

sql_lite = SqlLiteDataBase()
sql_lite.create_db(DB_NAME)
urls_df = MainDeploy().run(True)
st.write(pd.DataFrame(urls_df[0]))
