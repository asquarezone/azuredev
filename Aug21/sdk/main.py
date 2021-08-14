from azure.identity import AzureCliCredential
import os
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
import random

credential = None
def get_credential():
    global credential
    if credential is None:
        credential = AzureCliCredential()
    return credential



def resource_group():
    crediential = get_credential()
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']

    resource_client = ResourceManagementClient(crediential,subscription_id)
    print(resource_client.resource_groups)

    for group in resource_client.resource_groups.list():
        print(f"Printing resources in {group.name}")
        # print all the resources in resource group
        resources_list = resource_client.resources.list_by_resource_group(group.name)
        for resource in list(resources_list):
            print(resource.name)
        
    


def storage():
    crediential =  get_credential()
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']

    resource_client = ResourceManagementClient(crediential,subscription_id)
    rg_name = "FromPython"
    location = "eastus"
    if not resource_client.resource_groups.check_existence(rg_name):
        resource_client.resource_groups.create_or_update(rg_name, { "location": location })

    storage_client = StorageManagementClient(crediential, subscription_id)
    STORAGE_ACCOUNT_NAME = f"qtfrompython{random.randint(1,10000)}"
    is_name_available = storage_client.storage_accounts.check_name_availability({
        "name": STORAGE_ACCOUNT_NAME
    })

    if is_name_available:
        poller = storage_client.storage_accounts.begin_create(rg_name, STORAGE_ACCOUNT_NAME, {
            "location": location,
            "kind": "StorageV2",
            "sku": { "name": "Standard_LRS" }
        })
        account_result = poller.result()
        print(account_result.name)



if __name__ == "__main__":
    storage()