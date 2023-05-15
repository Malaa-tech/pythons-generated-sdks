from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.api_client import ApiClient
from pprint import pprint

# Configure the base URL to localhost:8000
configuration = swagger_client.Configuration()
configuration.host = "http://localhost:8000"

# Create an instance of the ApiClient class
api_client = ApiClient(configuration)

# Define the required and optional input parameters for the GetItem operation
item_id = 1  # Replace this with the item ID you want to retrieve
query_param = "example_query_param"  # You can set this to None if you don't want to pass a query_param

# Build the endpoint path and query parameters
path = f'/items/{item_id}'
query_params = {'query_param': query_param}

try:
    # Call the GetItem operation
    api_response = api_client.call_api(path,
                                       'GET',
                                       query_params=query_params,
                                       header_params={},
                                       response_type='object')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiClient->get_item: %s\n" % e)
