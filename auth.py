# Imports the Input Parser file for client credentials and generates the access token.
from src.inputParser import InputParser
import json
import requests


class Auth:

    def __init__(self):
        print("[Auth] Initializing the Auth module")
        self.input = InputParser()
        self.config = {}
        self.base_uri = "https://login.microsoftonline.com/"
        self.url = self.base_uri + "{}/oauth2/token".format(self.input.tenant_id)
        self.data = {'grant_type': 'client_credentials',
                     'client_id': self.input.client_id,
                     'client_secret': self.input.client_secret,
                     'resource': 'https://login.microsoftonline.com'
                     }
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.token = None

    def generate_token(self):
        url = self.url
        headers = self.header
        payload = self.data
        files = []
        response = requests.post(url, headers=headers, data=payload, files=files)
        data = response.json()
        self.token = data["access_token"]
        print(self.token)
        return self.token


var = Auth()
var.__init__()
var.generate_token()
