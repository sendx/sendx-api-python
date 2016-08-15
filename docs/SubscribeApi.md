# swagger_client.SubscribeApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscribe_encrypted_list_id_post**](SubscribeApi.md#subscribe_encrypted_list_id_post) | **POST** /subscribe/{encryptedListId} | Subscribe a new user a list
[**subscribe_encrypted_list_id_put**](SubscribeApi.md#subscribe_encrypted_list_id_put) | **PUT** /subscribe/{encryptedListId} | Subscribe an existing user a list


# **subscribe_encrypted_list_id_post**
> subscribe_encrypted_list_id_post(encrypted_list_id, body)

Subscribe a new user a list



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscribeApi()
encrypted_list_id = 'encrypted_list_id_example' # str | encrypted list Id of the list to which you want to add user
body = swagger_client.ContactAddUpdate() # ContactAddUpdate | Contact object that needs to be added

try: 
    # Subscribe a new user a list
    api_instance.subscribe_encrypted_list_id_post(encrypted_list_id, body)
except ApiException as e:
    print "Exception when calling SubscribeApi->subscribe_encrypted_list_id_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypted_list_id** | **str**| encrypted list Id of the list to which you want to add user | 
 **body** | [**ContactAddUpdate**](ContactAddUpdate.md)| Contact object that needs to be added | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_encrypted_list_id_put**
> subscribe_encrypted_list_id_put(encrypted_list_id, body)

Subscribe an existing user a list



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscribeApi()
encrypted_list_id = 'encrypted_list_id_example' # str | encrypted list Id of the list to which you want to add user
body = swagger_client.Email() # Email | Contact Emil needs to be added

try: 
    # Subscribe an existing user a list
    api_instance.subscribe_encrypted_list_id_put(encrypted_list_id, body)
except ApiException as e:
    print "Exception when calling SubscribeApi->subscribe_encrypted_list_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypted_list_id** | **str**| encrypted list Id of the list to which you want to add user | 
 **body** | [**Email**](Email.md)| Contact Emil needs to be added | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

