import requests
import json

r = requests.get('https://ms.portal.azure.com/#@microsoft.onmicrosoft.com/resource/subscriptions/c99e2bf3-1777-412b-baba-d823676589c2/resourceGroups/ritushis-test-rg/providers/Microsoft.Synapse/workspaces/ri11ushi/overview')

print (r.json())

