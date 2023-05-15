from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure the base URL to localhost:8000
configuration = swagger_client.Configuration()
configuration.host = "http://localhost:8000"

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
query_param = 'query_param_example' # str |  (optional)

try:
    # Read Item
    api_response = api_instance.get_item(item_id, query_param=query_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_item: %s\n" % e)