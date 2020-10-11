import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def get_subscription_id():
    """
    This method will get subscription id
    """
    if 'AZURE_SUBSCRIPTION_ID' not in os.environ:
        raise KeyError(message='AZURE_SUBSCRIPTION_ID environment variable is not defined')
    return os.environ['AZURE_SUBSCRIPTION_ID']

def get_resource_groups():
    """
    This method will return the resource groups
    """
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, get_subscription_id())
    for group in client.resource_groups.list():
        print(f"name: {group.name} location: {group.location}")

if __name__ == "__main__":
    get_resource_groups()