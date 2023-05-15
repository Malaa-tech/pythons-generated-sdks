# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item**](DefaultApi.md#get_item) | **GET** /items/{item_id} | Read Item

# **get_item**
> object get_item(item_id, query_param=query_param)

Read Item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
item_id = 56 # int | 
query_param = 'query_param_example' # str |  (optional)

try:
    # Read Item
    api_response = api_instance.get_item(item_id, query_param=query_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **query_param** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

