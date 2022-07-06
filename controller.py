# Defines 'post' and other methods used to retrieve credentials
import requests
from abc import ABC
from abc import abstractmethod
from src.auth import Auth
from src.inputParser import InputParser

class Controller(ABC):
    def __init__(self):
        print("[Controller] Initializing collector")
        self.auth = None
        self.input = None


    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_header(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    def post(self):
        """
        Given APP it calls the POST operation based on data,
        url and header supplied by the app object
        :return:
        """
        url = self.get_url()
        headers = self.get_header()
        payload = self.get_data()
        print("url is", url, "headers", headers, "payload", payload)

        response = requests.put(url, data=payload, headers=headers)
        print(response.text)

    def delete(self):
        pass

    def put(self):
        pass

    def get_tenant_id(self):
        self.input = InputParser()
        return self.input.tenant_id

    def get_client_id(self):
        self.input = InputParser()
        return self.input.client_id

    def get_client_secret(self):
        self.input = InputParser()
        return self.input.client_secret

    def get_token(self):
        self.auth = Auth()
        self.auth.generate_token()
        return self.auth.token
