# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
import os
import sys
import pathlib




class Synapse:
    def __init__(self):
        self.url = None
        self.headers = {}
        self.payload = {}
        self.config = {}
        self.get_parameter()

    def get_parameter(self):
        # The input json file is being opened, read as "f" and closed in this context managed block
        with open("inputParameters.json", "r") as f:
            #  "f" is being passed as an argument and the json object is being returned as a dictionary and stored in config instance
            self.config = json.load(f)

    def get_url(self):
        self.url = "https://management.azure.com/subscriptions/c99e2bf3-1777-412b-baba-d823676589c2/resourcegroups/ritushis-test-rg/providers/Microsoft.Resources/deployments/ritushiarmtemplate?api-version=2020-10-01"
        return self.url

    def get_header(self):
        # This access token can be retrieved from Azure Cloud shell by entering "az account get-access-token" command in the terminal. The token remains active for 1 hour.
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyIsImtpZCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNjU1MjkyMDE2LCJuYmYiOjE2NTUyOTIwMTYsImV4cCI6MTY1NTI5NjQ5MiwiX2NsYWltX25hbWVzIjp7Imdyb3VwcyI6InNyYzEifSwiX2NsYWltX3NvdXJjZXMiOnsic3JjMSI6eyJlbmRwb2ludCI6Imh0dHBzOi8vZ3JhcGgud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3L3VzZXJzLzc1ZDliZTUyLWU1ODQtNGQ1NS04Mjg1LWE4NmVhYjM2YWViMC9nZXRNZW1iZXJPYmplY3RzIn19LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFRBQUFBelVyVDBYZVAydGx6RTZvU1dTQkZMVU44OTE2TnZJNmhjR29WcS9IL1VkbHh1eDdyUVErdFpKSmVFY1J3cTVya0w1clgrNTZtMWlraVhwOGN5LzdtMStGWG9iTGhKdG5OcS9wTHd5c2lXOEk9IiwiYW1yIjpbInB3ZCIsInJzYSIsIndpYSIsIm1mYSJdLCJhcHBpZCI6ImI2NzdjMjkwLWNmNGItNGE4ZS1hNjBlLTkxYmE2NTBhNGFiZSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiZTU4OWIwY2ItYjIyMS00NGZmLWExZDgtYzljOWZkMTI0YTcxIiwiZmFtaWx5X25hbWUiOiJTaGFua2VyIiwiZ2l2ZW5fbmFtZSI6IlJpdHVzaGkiLCJpbl9jb3JwIjoidHJ1ZSIsImlwYWRkciI6IjIwLjU2LjE5My4xNzMiLCJuYW1lIjoiUml0dXNoaSBTaGFua2VyIiwib2lkIjoiNzVkOWJlNTItZTU4NC00ZDU1LTgyODUtYTg2ZWFiMzZhZWIwIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTIxMjc1MjExODQtMTYwNDAxMjkyMC0xODg3OTI3NTI3LTU3NTI1MzM2IiwicHVpZCI6IjEwMDMyMDAxRjk4NzMwNEEiLCJyaCI6IjAuQVJvQXY0ajVjdkdHcjBHUnF5MTgwQkhiUjBaSWYza0F1dGRQdWtQYXdmajJNQk1hQUNrLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6IkdIYWl2RHlsSHFWa0luSkhTc1g2cXozay1ocElxUWRrNEhjZU55ZlhDNVEiLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1bmlxdWVfbmFtZSI6InQtcnNoYW5rZXJAbWljcm9zb2Z0LmNvbSIsInVwbiI6InQtcnNoYW5rZXJAbWljcm9zb2Z0LmNvbSIsInV0aSI6Ijl2Y0RVZ21LamtHelFsaHgtZk5KQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfdGNkdCI6MTI4OTI0MTU0N30.SQ4i5yq0EbfQ7YqEBHbx4hwn3Dc3uMr8ox8FQfNyHlwCrd3J1DHPwb6zrJzciEDa4GkKJez5VqWvvsiqNyp-ycr5e9KjflFYHeKVPCps1qcwv6sb0-Ki2sFvi5jFu49WngffSxH_ul1XP3-OOEJ1b4mnwpXIHf0uvWqOgc8NAaTLuyEL-BmZpFOdG3czaW11GZovvjEH7Apw7eFFYxfyRX0UYPHeCDEcpK7WuMhZoCj70JgPHmGWpEycE6OhtNxxsGW9vvG27NVEGNaO5zyllzxukk-2WJtgGwnvPW5zt2491QkWwbKYWv05bz3T4BFgK4wQcso0MZq-GOR63LxGUQ"
        self.headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
            'tenantId': '72f988bf-86f1-41af-91ab-2d7cd011db47',
            'clientId': '90fb8b03-6445-4377-83af-ba4564c20f84',
            'clientSecret': 'Uja8Q~LsP54BIVCOY-wOxxEP29uryPH00XdDvcY0'
        }
        return self.headers

    def get_data(self):
        # Input dictionary stored in the config instance is converted to string in the payload instance
        self.payload = json.dumps({
            "properties": {
                "templateLink": {
                    "uri": "https://janrajcjprod.blob.core.windows.net/janraj/template.json"
                },
                "parameters": {
                    "name": {
                        "value": self.config["synapse"]["parameters"]["name"]
                    },
                    "location": {
                        "value": self.config["synapse"]["parameters"]["location"]
                    },
                    "defaultDataLakeStorageAccountName": {
                        "value": self.config["synapse"]["parameters"]["defaultDataLakeStorageAccountName"]
                    },
                    "defaultDataLakeStorageFilesystemName": {
                        "value": self.config["synapse"]["parameters"]["defaultDataLakeStorageFilesystemName"]
                    },
                    "sqlAdministratorLogin": {
                        "value": self.config["synapse"]["parameters"]["sqlAdministratorLogin"]
                    },
                    "setWorkspaceIdentityRbacOnStorageAccount": {
                        "value": False
                    },
                    "createManagedPrivateEndpoint": {
                        "value": False
                    },
                    "defaultAdlsGen2AccountResourceId": {
                        "value": "/subscriptions/c99e2bf3-1777-412b-baba-d823676589c2/resourceGroups/ritushis-test-rg/providers/Microsoft.Storage/storageAccounts/ritushitestADLS"
                    },
                    "azureADOnlyAuthentication": {
                        "value": False
                    },
                    "allowAllConnections": {
                        "value": True
                    },
                    "managedVirtualNetwork": {
                        "value": ""
                    },
                    "tagValues": {
                        "value": {}
                    },
                    "storageSubscriptionID": {
                        "value": self.config["synapse"]["parameters"]["storageSubscriptionID"]
                    },
                    "storageResourceGroupName": {
                        "value": self.config["synapse"]["parameters"]["storageResourceGroupName"]
                    },
                    "storageLocation": {
                        "value": self.config["synapse"]["parameters"]["storageLocation"]
                    },
                    "storageRoleUniqueId": {
                        "value": "ea7876ee-81e7-4f25-9159-c06b39567030"
                    },
                    "isNewStorageAccount": {
                        "value": True
                    },
                    "isNewFileSystemOnly": {
                        "value": False
                    },
                    "adlaResourceId": {
                        "value": ""
                    },
                    "managedResourceGroupName": {
                        "value": ""
                    },
                    "storageAccessTier": {
                        "value": "Hot"
                    },
                    "storageAccountType": {
                        "value": "Standard_RAGRS"
                    },
                    "storageSupportsHttpsTrafficOnly": {
                        "value": True
                    },
                    "storageKind": {
                        "value": "StorageV2"
                    },
                    "minimumTlsVersion": {
                        "value": "TLS1_2"
                    },
                    "storageIsHnsEnabled": {
                        "value": True
                    },
                    "userObjectId": {
                        "value": "04eff046-d35f-452e-a297-65b5bda1d274"
                    },
                    "setSbdcRbacOnStorageAccount": {
                        "value": False
                    },
                    "setWorkspaceMsiByPassOnStorageAccount": {
                        "value": False
                    },
                    "workspaceStorageAccountProperties": {
                        "value": {}
                    }
                },
                "mode": "Incremental",
                "debugSetting": {
                    "detailLevel": "requestContent, responseContent"
                }
            }
        })
        return self.payload

    def post_hook_for_post_api(self, response):
        pass

    def post_hook_for_put_api(self, response):
        pass

    def set_retry_strategy(self):
        pass

    def create_synapse_workspace(self):
        url = self.get_url()
        headers = self.get_header()
        payload = self.get_data()

        response = requests.put(url, data=payload, headers=headers)
        print(response.text)



if __name__ == '__main__':
    obj = Synapse()
    obj.create_synapse_workspace()
