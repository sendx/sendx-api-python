# swagger_client.UnsubscribeApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unsubscribe_encrypted_list_id_post**](UnsubscribeApi.md#unsubscribe_encrypted_list_id_post) | **POST** /unsubscribe/{encryptedListId} | Unsubscribe a user from list based on email id


# **unsubscribe_encrypted_list_id_post**
> unsubscribe_encrypted_list_id_post(encrypted_list_id, body)

Unsubscribe a user from list based on email id



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnsubscribeApi()
encrypted_list_id = 'encrypted_list_id_example' # str | encrypted list Id of the list to which you want to add user
body = swagger_client.Email() # Email | Email object of the user that needs to be unsubscribed.

try: 
    # Unsubscribe a user from list based on email id
    api_instance.unsubscribe_encrypted_list_id_post(encrypted_list_id, body)
except ApiException as e:
    print "Exception when calling UnsubscribeApi->unsubscribe_encrypted_list_id_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypted_list_id** | **str**| encrypted list Id of the list to which you want to add user | 
 **body** | [**Email**](Email.md)| Email object of the user that needs to be unsubscribed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

