import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        response = self.session.get(url, **kwargs)
        return response

    def post(self, path: str, json=None, **kwargs):
        url = f"{self.base_url}{path}"
        response = self.session.post(url, json=json, **kwargs)
        return response

    def put(self, path: str, json=None, **kwargs):
        url = f"{self.base_url}{path}"
        response = self.session.put(url, json=json, **kwargs)
        return response

    def delete(self, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        response = self.session.delete(url, **kwargs)
        return response
