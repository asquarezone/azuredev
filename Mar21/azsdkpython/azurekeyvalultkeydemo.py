import os
from azure.identity import AzureCliCredential
from azure.keyvault.keys import KeyClient

key_vault_name = os.environ['KEY_VAULT_NAME']
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"

credential = AzureCliCredential()
key_client = KeyClient(key_vault_uri, credential)

key_name = input("Enter your key name in azure key vault: ")
retrievedkey = key_client.get_key(key_name)

print(f"retrieved key is {retrievedkey.key.y}")