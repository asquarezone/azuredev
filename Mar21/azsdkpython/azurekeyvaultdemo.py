import os
from azure.identity import AzureCliCredential
from azure.keyvault.secrets import SecretClient

key_vault_name = os.environ['KEY_VAULT_NAME']
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"

credential = AzureCliCredential()

secret_client = SecretClient(key_vault_uri, credential)
secret_name = input("Enter your secret name in azure key vault: ")
retrieved_secret = secret_client.get_secret(secret_name)
print(f"secret = {retrieved_secret.value}")

