from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os

# Acquire credential object
credential = AzureCliCredential()

# Lets Get the subscription id from environment variable
subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']

# Lets create the resource manager client object
resource_client = ResourceManagementClient(credential, subscription_id)

# Lets fetch the list of resource groups
resourcegroup_list = resource_client.resource_groups.list()

for resourcegroup in resourcegroup_list:
    print("Name = {}, Location= {}".format(resourcegroup.name, resourcegroup.location)) 