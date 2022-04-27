import base64
from typing import Dict

import pandas as pd
import requests
from requests import Response

from src.utils.utils import get_url_website_to_url_id
from src.virus_total.config import X_API_KEY


class VirusTotal:
    def __init__(self):
        self.virus_total_url_analysis_report = "https://www.virustotal.com/api/v3/urls/"
        self.headers = {
            "Accept": "application/json",
            "x-apikey": X_API_KEY
        }

    def get_url_analysis_report(self, url: str) -> Dict:
        url_id = get_url_website_to_url_id(url)
        response = self._execute_analysis_report_request(url_id)
        analysis_report_data = response.json()
        return analysis_report_data

    def _execute_analysis_report_request(self, url_id: base64) -> Response:
        url_request = self.virus_total_url_analysis_report + f"{url_id}"
        try:
            response = requests.get(url_request, headers=self.headers)
        except requests.exceptions.Timeout:
            response = self.rerun_request(url_request)
        except requests.exceptions.TooManyRedirects:
            raise Exception('please check your url')
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        if response.status_code != 200:
            raise Exception('Please check request parameters')
        return response

    def rerun_request(self, url_request: str, number_of_tries: int = 3) -> Response:
        while number_of_tries != 0:
            try:
                response = requests.get(url_request, headers=self.headers)
                return response
            except requests.exceptions.Timeout:
                number_of_tries = number_of_tries - 1
