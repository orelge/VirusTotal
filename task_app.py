import pandas as pd
import streamlit as st

from src.main_deploy import MainDeploy

urls_df = MainDeploy(is_streamlit_deploy=True).run(True)
for df in urls_df:
    st.write(df)
