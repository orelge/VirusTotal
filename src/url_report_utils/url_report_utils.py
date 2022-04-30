import pandas as pd

from src.main_config import LOCAL_REPORT
from src.virus_total.virus_total import VirusTotal


class UrlReportUtils:

    def __init__(self, url: str, get_local_report=True):
        self.url = url
        self.virus_total = VirusTotal()
        if get_local_report:
            self.url_report = LOCAL_REPORT
        else:
            self.url_report = self.virus_total.get_url_analysis_report(self.url)

    def get_url_risk_classification(self) -> str:
        results = []
        risk_values = ['malicious', 'phishing', 'malware']
        analysis_results = self.url_report['data']['attributes']['last_analysis_results']
        for key in list(analysis_results.keys())[:]:
            results.append(analysis_results[key]['result'])
        results_se = pd.Series(results)
        results_se = results_se[results_se.apply(lambda val: val in risk_values)]
        if any(list(results_se.value_counts() > 1)):
            return 'risk'
        else:
            return 'safe'

    def get_url_voting(self) -> pd.DataFrame:
        results = []
        analysis_results = self.url_report['data']['attributes']['last_analysis_results']
        for key in list(analysis_results.keys())[:]:
            results.append(analysis_results[key]['result'])
        results_se = pd.Series(results)
        voting_df = pd.DataFrame(results_se.value_counts(), columns=['voting_count'])
        return voting_df

    def get_url_categories(self) -> pd.DataFrame:
        categories_list = []
        categories = self.url_report['data']['attributes']['categories']
        for key in self.url_report['data']['attributes']['categories'].keys():
            categories_list.append(categories[key])
        categories = pd.Series(categories_list)
        categories_df = pd.DataFrame(categories.value_counts(), columns=['category_count'])
        return categories_df
