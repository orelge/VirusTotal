import streamlit as st
import pandas as pd
from src.database.sqlite_database import SqlLiteDataBase
from src.main_config import DB_NAME, URLS_CLASSIFICATION_TABLE, CATEGORIES_TABLE, VOTING_TABLE
from src.main_deploy import MainDeploy

# task_dfs = MainDeploy(is_streamlit_deploy=True).run(return_df=True)
task_dfs= []
sql_lite = SqlLiteDataBase().connect_db(DB_NAME)
task_dfs.append(pd.read_sql(f'''select * from {URLS_CLASSIFICATION_TABLE}''',sql_lite.connection))
task_dfs.append(pd.read_sql(f'''select * from {CATEGORIES_TABLE}''',sql_lite.connection))
task_dfs.append(pd.read_sql(f'''select * from {VOTING_TABLE}''',sql_lite.connection))

for df, title in zip(task_dfs, [URLS_CLASSIFICATION_TABLE, CATEGORIES_TABLE, VOTING_TABLE]):
    st.title(title)
    st.write(df)

# if __name__ == '__main__':
#     task_dfs = MainDeploy(is_streamlit_deploy=True).run(return_df=True)
#     # task_dfs.append(pd.read_sql(f'''select * from {URLS_CLASSIFICATION_TABLE}''',sql_lite.connection))
#     # task_dfs.append(pd.read_sql(f'''select * from {CATEGORIES_TABLE}''',sql_lite.connection))
#     # task_dfs.append(pd.read_sql(f'''select * from {VOTING_TABLE}''',sql_lite.connection))
#
#     for df, title in zip(task_dfs, [URLS_CLASSIFICATION_TABLE, CATEGORIES_TABLE, VOTING_TABLE]):
#         st.title(title)
#         st.write(df)