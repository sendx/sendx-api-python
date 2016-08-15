# swagger_client.SendApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email_post**](SendApi.md#send_email_post) | **POST** /send/email | Send transactional email to user


# **send_email_post**
> send_email_post(api_key, body)

Send transactional email to user



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SendApi()
api_key = 'api_key_example' # str | 
body = swagger_client.EMessage() # EMessage | EMessage object that needs to be added

try: 
    # Send transactional email to user
    api_instance.send_email_post(api_key, body)
except ApiException as e:
    print "Exception when calling SendApi->send_email_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**EMessage**](EMessage.md)| EMessage object that needs to be added | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

