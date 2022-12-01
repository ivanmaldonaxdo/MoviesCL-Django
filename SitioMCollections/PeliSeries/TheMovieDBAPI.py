import requests
from requests.auth import HTTPBasicAuth
import json
from requests.adapters import HTTPAdapter, Retry
import time
import re
from django.utils import timezone

class MovieDB:
    def __init__(self,api_key,url):
        self.api_key = api_key
        self.end_point_base = url

    def get_request(self,_url,_params = None, _headers = {'Accept': 'application/json'}):
        headers = _headers
        response = requests.get(_url,headers = headers,params = _params )
        return response

    def search_genres(self):
        endpoint = "/genre/movie/list"
        params = {"api_key": self.api_key}
        url =  "{}{}" .format(self.end_point_base,endpoint)
        response = self.get_request(url,params)
        data = response.json()
        return data

    def search_multi(self,query = None):
        endpoint = "/search/movie"
        params = {
            "api_key": self.api_key,
            "query":query
        }
        url =  "{}{}" .format(self.end_point_base,endpoint)
        response = self.get_request(url,params)
        data = response.json()
        return data
    def search_top_rated(self):
        endpoint = "/search/movie"
        params = {
            "api_key": self.api_key,
            "query":query
        }
        url =  "{}{}" .format(self.end_point_base,endpoint)
        response = self.get_request(url,params)
        data = response.json()
        return data