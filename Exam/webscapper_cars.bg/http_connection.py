
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

class HttpConnection:

    def __init__(self):
        self.requestSession = requests.Session()
        retry = Retry(connect=5, redirect=5, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.requestSession.mount('http://', adapter)
        self.requestSession.mount('https://', adapter)
