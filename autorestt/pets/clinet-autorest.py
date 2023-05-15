from azure.identity import DefaultAzureCredential
from azure.pets import Pe

client = PetsClient(credential=DefaultAzureCredential())
item = client.get_item(item_id=1)

