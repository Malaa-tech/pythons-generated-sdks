import fastapi_sdk
from fastapi_sdk.apis.tags import default_api
from fastapi_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fastapi_sdk.Configuration(
    host = "http://localhost:8000"
)

# Enter a context with an instance of the API client
with fastapi_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'item_id': 1,
    }
    query_params = {
    }
    try:
        # Read Item
        api_response = api_instance.read_item_items_item_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except fastapi_sdk.ApiException as e:
        print("Exception when calling DefaultApi->read_item_items_item_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'item_id': 1,
    }
    query_params = {
        'query_param': "query_param_example",
    }
    try:
        # Read Item
        api_response = api_instance.read_item_items_item_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except fastapi_sdk.ApiException as e:
        print("Exception when calling DefaultApi->read_item_items_item_id_get: %s\n" % e)