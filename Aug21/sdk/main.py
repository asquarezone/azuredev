from azure.identity import AzureCliCredential
import os
from azure.mgmt.resource import ResourceManagementClient

def resource_group():
    crediential = AzureCliCredential()
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']

    resource_client = ResourceManagementClient(crediential,subscription_id)
    print(resource_client.resource_groups)

    for group in resource_client.resource_groups.list():
        print(f"Printing resources in {group.name}")
        # print all the resources in resource group
        resources_list = resource_client.resources.list_by_resource_group(group.name)
        for resource in list(resources_list):
            print(resource.name)
        
    if not resource_client.resource_groups.check_existence("FromPython"):
        resource_client.resource_groups.create_or_update("FromPython", { "location": "eastus" })



if __name__ == "__main__":
    resource_group()