from typing import List

import pandas as pd

from src.database.sqlite_database import SqlLiteDataBase
from src.main_config import URLS_COLUMN, URL_COLUMN, URL_CLASSIFICATION_COLUMN, URLS_CLASSIFICATION_TABLE, VOTING_TABLE, \
    CATEGORIES_TABLE, GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY, IS_TABLE_EXIST_QUERY, DB_NAME
from src.main_config import URLS_CSV_FILE_PATH
from src.url_report_utils.url_report_utils import UrlReportUtils


class MainDeploy:
    def __init__(self, urls_path: str = URLS_CSV_FILE_PATH, db_name: str = DB_NAME,
                 urls_table_name: str = URLS_CLASSIFICATION_TABLE):
        sql_lite = SqlLiteDataBase().create_db(db_name)
        self.urls_path = urls_path
        self.sql_lite_connection = sql_lite.connection
        self.urls_table_name = urls_table_name

    def get_urls_list(self) -> List:
        urls_list = list(pd.read_csv(self.urls_path)[URLS_COLUMN])
        return urls_list

    def run(self):
        urls_classifications_rows = []
        final_urls_voting_df = pd.DataFrame(columns=['voting_value', 'voting_count', 'url'])
        final_urls_category_df = pd.DataFrame(columns=['category_value', 'category_count', 'url'])
        urls_list = self.get_urls_list()
        final_urls_category_df, final_urls_voting_df = self.iterate_over_urls_and_build_data(final_urls_category_df,
                                                                                             final_urls_voting_df,
                                                                                             urls_classifications_rows,
                                                                                             urls_list)
        final_url_classification_df = pd.DataFrame(urls_classifications_rows,
                                                   columns=[URL_COLUMN, URL_CLASSIFICATION_COLUMN])
        final_url_classification_df.to_sql(URLS_CLASSIFICATION_TABLE, self.sql_lite_connection)
        final_urls_voting_df.to_sql(VOTING_TABLE, self.sql_lite_connection)
        final_urls_category_df.to_sql(CATEGORIES_TABLE, self.sql_lite_connection)

    def iterate_over_urls_and_build_data(self, final_urls_category_df, final_urls_voting_df, urls_classifications_rows,
                                         urls_list):
        for url in urls_list[:]:
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
        if not self.is_classification_updated(url, url_classification):
            urls_classifications_rows.append([url, url_classification])
        else:
            pass

    def is_classification_updated(self, url: str, url_risk_classification: str):
        if not self.is_table_exist_in_db():
            return False
        else:
            urls_classification_data = pd.read_sql(GET_DATA_FROM_URLS_CLASSIFICATION_TABLE_QUERY,
                                                   self.sql_lite_connection)
            is_classification_updated = urls_classification_data[urls_classification_data[URL_COLUMN] == url][
                                            URL_CLASSIFICATION_COLUMN] == url_risk_classification
            return is_classification_updated

    def is_table_exist_in_db(self):
        tables_list = list(pd.read_sql(IS_TABLE_EXIST_QUERY, self.sql_lite_connection)['tbl_name'])
        return self.urls_table_name in tables_list


if __name__ == '__main__':
    deploy = MainDeploy().run()
