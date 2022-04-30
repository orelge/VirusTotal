from datetime import datetime, timedelta
from typing import List

import pandas as pd

from src.database.sqlite_database import SqlLiteDataBase
from src.main_config import URLS_COLUMN, URL_COLUMN, URL_CLASSIFICATION_COLUMN, URLS_CLASSIFICATION_TABLE, VOTING_TABLE, \
    CATEGORIES_TABLE, GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY, IS_TABLE_EXIST_QUERY, DB_NAME, URLS_LIST, \
    TABLE_IS_NOT_IN_DB_ERROR_STRING, INSERTION_TIME_COLUMN
from src.main_config import URLS_CSV_FILE_PATH
from src.url_report_utils.url_report_utils import UrlReportUtils


class MainDeploy:
    def __init__(self, urls_path: str = URLS_CSV_FILE_PATH, db_name: str = DB_NAME,
                 urls_table_name: str = URLS_CLASSIFICATION_TABLE, is_streamlit_deploy: bool = False):
        sql_lite = SqlLiteDataBase().create_db(db_name)
        self.urls_path = urls_path
        self.sql_lite_connection = sql_lite.connection
        self.urls_table_name = urls_table_name
        self.is_streamlit_deploy = is_streamlit_deploy

    def get_urls_list(self) -> List:
        if not self.is_streamlit_deploy:
            urls_list = list(pd.read_csv(self.urls_path)[URLS_COLUMN])
        else:
            urls_list = URLS_LIST
        return urls_list

    def run(self, return_df=False):
        urls_classifications_rows = []
        final_urls_voting_df = pd.DataFrame(columns=['voting_value', 'voting_count', 'url'])
        final_urls_category_df = pd.DataFrame(columns=['category_value', 'category_count', 'url'])
        urls_list = self.get_urls_list()
        final_urls_category_df, final_urls_voting_df = self.iterate_over_urls_and_build_data(final_urls_category_df,
                                                                                             final_urls_voting_df,
                                                                                             urls_classifications_rows,
                                                                                             urls_list)
        final_url_classification_df = pd.DataFrame(urls_classifications_rows,
                                                   columns=[URL_COLUMN, URL_CLASSIFICATION_COLUMN,
                                                            INSERTION_TIME_COLUMN])
        self.insert_and_update_url_classifications_table(final_url_classification_df)
        final_urls_voting_df.to_sql(VOTING_TABLE, self.sql_lite_connection, if_exists='replace')
        final_urls_category_df.to_sql(CATEGORIES_TABLE, self.sql_lite_connection, if_exists='replace')
        if return_df:
            return final_url_classification_df, final_urls_voting_df, final_urls_category_df

    def insert_and_update_url_classifications_table(self, final_url_classification_df):
        exist_rows = pd.DataFrame(columns=[final_url_classification_df.columns])
        try:
            exist_rows = pd.read_sql(GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY,
                                     self.sql_lite_connection, parse_dates=[INSERTION_TIME_COLUMN])
            exist_rows = exist_rows[
                exist_rows[URL_COLUMN].apply(lambda url: url not in list(final_url_classification_df[URL_COLUMN]))]
        except Exception as e:
            if str(e) == TABLE_IS_NOT_IN_DB_ERROR_STRING:
                pass
        if len(exist_rows) != 0:
            df = pd.concat([exist_rows, final_url_classification_df])
            df.to_sql(URLS_CLASSIFICATION_TABLE, self.sql_lite_connection,
                      if_exists='replace')
        else:
            final_url_classification_df.to_sql(URLS_CLASSIFICATION_TABLE, self.sql_lite_connection,
                                               if_exists='replace')

    def iterate_over_urls_and_build_data(self, final_urls_category_df, final_urls_voting_df, urls_classifications_rows,
                                         urls_list):
        un_update_urls_list = self.drop_updated_urls(urls_list.copy())
        for url in un_update_urls_list[:]:
            url_report_utils = UrlReportUtils(url)
            self.build_url_classification(url, url_report_utils, urls_classifications_rows)
            url_voting_df = self.build_voting_df(url, url_report_utils)
            url_categories_df = self.build_category_df(url, url_report_utils)
            final_urls_voting_df = pd.concat([final_urls_voting_df, url_voting_df])
            final_urls_category_df = pd.concat([final_urls_category_df, url_categories_df])
        return final_urls_category_df, final_urls_voting_df

    @staticmethod
    def build_category_df(url, url_report_utils):
        url_categories_df = url_report_utils.get_url_categories()
        url_categories_df = url_categories_df.reset_index().rename(columns={'index': 'category_value'}, inplace=False)
        url_categories_df[URL_COLUMN] = url
        return url_categories_df

    @staticmethod
    def build_voting_df(url, url_report_utils):
        url_voting_df = url_report_utils.get_url_voting()
        url_voting_df = url_voting_df.reset_index().rename(columns={'index': 'voting_value'}, inplace=False)
        url_voting_df[URL_COLUMN] = url
        return url_voting_df

    def build_url_classification(self, url, url_report_utils, urls_classifications_rows):
        url_classification = url_report_utils.get_url_risk_classification()
        insertion_time = datetime.now()
        urls_classifications_rows.append([url, url_classification, insertion_time])

    def drop_updated_urls(self, urls_list: List) -> List:
        is_classification_updated = None
        for url in urls_list:
            try:
                urls_classification_data = pd.read_sql(GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY,
                                                       self.sql_lite_connection, parse_dates=[INSERTION_TIME_COLUMN])
                if len(urls_classification_data) == 0:
                    pass
                else:
                    is_classification_updated = self.check_if_risk_value_is_update(urls_classification_data, url)
            except Exception as e:
                if str(e) == TABLE_IS_NOT_IN_DB_ERROR_STRING:
                    return urls_list
                else:
                    ValueError(str(e))
            if is_classification_updated:
                urls_list.pop(urls_list.index(url))
            else:
                pass
        return urls_list

    def check_if_risk_value_is_update(self, urls_classification_data, url) -> bool:
        if len(urls_classification_data[urls_classification_data[URL_COLUMN] == url][
                   URL_CLASSIFICATION_COLUMN]) == 0:
            return False
        else:
            return urls_classification_data[urls_classification_data[URL_COLUMN] == url][
                       INSERTION_TIME_COLUMN].iloc[0] >= datetime.now() - timedelta(minutes=30)

    def is_table_exist_in_db(self):
        tables_list = list(pd.read_sql(IS_TABLE_EXIST_QUERY, self.sql_lite_connection)['tbl_name'])
        return self.urls_table_name in tables_list


if __name__ == '__main__':
    deploy = MainDeploy().run(True)
