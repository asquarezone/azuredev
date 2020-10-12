import os
import json
from azure.identity import DefaultAzureCredential
from azure.identity import ClientSecretCredential
from  azure.mgmt.resource import ResourceManagementClient

def get_credential_using_different_approach():
    """
    This method tries to read the credentials from file
    """
    
    with open('D:\\temp\\test.json') as cred_file:
        contnets = cred_file.read()
        credential_json = json.loads(contnets)
        credential = ClientSecretCredential(
            tenant_id=credential_json['tenantId'],
            client_id=credential_json['clientId'],
            client_secret=credential_json['clientSecret'])
        return credential

    


def get_credential():
    """
    This method will return the default Azure credentials
    """
    if 'AZURE_SUBSCRIPTION_ID' in os.environ and 'AZURE_TENANT_ID' in os.environ and 'AZURE_CLIENT_ID' in os.environ and 'AZURE_CLIENT_SECRET' in os.environ:
        return DefaultAzureCredential()
    else:
        documentation_location = "https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#configure-authentication"
        raise KeyError(f'This code expects the environment variables to be defined {documentation_location}')

def print_line():
    for index in range(80):
        print("#",end='')
    print()



def print_resource_groups():
    """
    This method will print the resource groups
    """
    credential = get_credential_using_different_approach()
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    client = ResourceManagementClient(credential, subscription_id)
    resource_groups = client.resource_groups.list()
    print_line()
    print("name\t\t\tlocation\t")
    print_line()
    for resource_group in resource_groups:
        print(f"{resource_group.name}\t\t{resource_group.location}")
    print_line()
    

if __name__ == "__main__":
    print_resource_groups()