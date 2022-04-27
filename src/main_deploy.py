from typing import List

import pandas as pd

from src.main_config import URLS_COLUMN, URL_COLUMN
from src.main_config import URLS_CSV_FILE_PATH
from src.url_report_utils.url_report_utils import UrlReportUtils


class MainDeploy:
    def __init__(self, urls_path: str = URLS_CSV_FILE_PATH):
        self.urls_path = urls_path

    def get_urls_list(self) -> List:
        urls_list = list(pd.read_csv(self.urls_path)[URLS_COLUMN])
        return urls_list

    def run(self):
        urls_classifications_rows = []
        final_urls_voting_df = pd.DataFrame(columns=['voting_value', 'voting_count', 'url'])
        final_urls_category_df = pd.DataFrame(columns=['category_value', 'category_count', 'url'])
        urls_list = self.get_urls_list()
        for url in urls_list[:]:
            self.is_classification_updated(url)
            url_report_utils = UrlReportUtils(url)
            self.build_url_classification(url, url_report_utils, urls_classifications_rows)
            url_voting_df = self.build_voting_df(url, url_report_utils)
            url_categories_df = self.build_category_df(url, url_report_utils)
            final_urls_voting_df = pd.concat([final_urls_voting_df, url_voting_df])
            final_urls_category_df = pd.concat([final_urls_category_df, url_categories_df])
        final_urls_voting_df.to_excel(r'a.xlsx')
        final_urls_category_df.to_excel(r'b.xlsx')

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

    @staticmethod
    def build_url_classification(url, url_report_utils, urls_classifications_rows):
        url_risk_classification = url_report_utils.get_url_risk_classification()
        urls_classifications_rows.append([url, url_risk_classification])

    @staticmethod
    def is_classification_updated(url: str):
        print('Dummy check in DB')


if __name__ == '__main__':
    deploy = MainDeploy().run()
