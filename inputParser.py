# Python script that sets the parser by reading from the instance cache. If cache is empty, configuration of
# the parser is retrieved and validated from config.json file. If credential is not present in config file,
# an exception is raised.Otherwise, the value is set.
import os
import json


class InputParser:
    _instances_cache = {}
    _instances = None

    def __new__(cls, *args, **kwargs):
        if "object" not in cls._instances_cache:
            print("[Input Parser] Initializing the parser")
            obj = super(InputParser, cls).__new__(cls, *args, **kwargs)
            obj.config = {}
            obj.type = None
            obj.client_secret = None
            obj.client_id = None
            obj.tenant_id = None
            obj.Oak_uri = None
            obj.Synapse_Endpoint = None
            obj.Data_Partition = None
            cls._instances_cache["object"] = obj
            cls._instances = obj
            obj.get_config()
            obj.validate_config()
        return cls._instances_cache["object"]

    def get_config(self):
        print("Reading the config")
        file_path = os.path.dirname(__file__)
        with open(os.path.abspath(file_path + "/config.json"), "r") as f:
            self._instances.config = json.load(f)

    def validate_config(self):

        print("Validating the Config {}".format(self._instances.config))
        if "synapse" not in self._instances.config:
            print("Invalid Config file format")
            raise Exception("Sorry, Must provide a valid config file")
        '''
           hard coded now, we will make it dynamic as per the source.
        '''
        self._instances.type = "synapse"
        if "client_id" not in self._instances.config["synapse"] or not self._instances.config["synapse"][
            "client_id"]:
            print("Client ID is must for the rest connector")
            raise Exception("Sorry, Client ID is mandatory for the rest connector")
        self.set_client_id(self._instances.config["synapse"]["client_id"])

        if "client_secret" not in self._instances.config["synapse"] or not self._instances.config["synapse"][
            "client_secret"]:
            print("Client Secret is must for the rest connector")
            raise Exception("Sorry, Client Secret is mandatory for the rest connector")
        self.set_client_secret(self._instances.config["synapse"]["client_secret"])

        if "tenant_id" not in self._instances.config["synapse"] or not self._instances.config["synapse"][
            "tenant_id"]:
            print("Tenant ID is must for the rest connector")
            raise Exception("Sorry, Tenant ID is mandatory for the rest connector")
        self.set_tenant_id(self._instances.config["synapse"]["tenant_id"])

        if "Oak_uri" not in self._instances.config["synapse"] or not self._instances.config["synapse"]["Oak_uri"]:
            print("OAK URI is must for the rest connector")
            raise Exception("Sorry, Oak URI is mandatory for the rest connector")
        self.set_Oak_uri(self._instances.config["synapse"]["Oak_uri"])

        if "Synapse_Endpoint" not in self._instances.config["synapse"] or not self._instances.config["synapse"][
            "Synapse_Endpoint"]:
            print("Synapse Endpoint is must for the rest connector")
            raise Exception("Sorry, Synapse Endpoint is mandatory for the rest connector")
        self.set_Synapse_Endpoint(self._instances.config["synapse"]["Synapse_Endpoint"])

        if "Data_Partition" not in self._instances.config["synapse"] or not self._instances.config["synapse"][
            "Data_Partition"]:
            print("Data Partition ID is must for the rest connector")
            raise Exception("Sorry, Data Partition ID is mandatory for the rest connector")
        self.set_Data_Partition(self._instances.config["synapse"]["Data_Partition"])
        print("Valid Config is present for Authentication")

    def get_tenant_id(self):
        return self._instances.tenant_id

    def set_tenant_id(self, tenant):
        self._instances.tenant_id = tenant

    def get_client_id(self):
        return self._instances.client_id

    def set_client_id(self, client):
        self._instances.client_id = client

    def get_client_secret(self):
        return self._instances.client_secret

    def set_client_secret(self, secret):
        self._instances.client_secret = secret

    def get_Oak_uri(self):
        return self._instances.Oak_uri

    def set_Oak_uri(self, uri):
        self._instances.Oak_uri = uri

    def get_Synapse_endpoint(self):
        return self._instances.Synapse_Endpoint

    def set_Synapse_Endpoint(self, endpoint):
        self._instances.Synapse_Endpoint = endpoint

    def get_Data_Partition(self):
        return self._instances.Data_Partition

    def set_Data_Partition(self, partition):
        self._instances.Data_Partition = partition

    def get_cur_status(self):
        print("Parsed the input for Synapse")
