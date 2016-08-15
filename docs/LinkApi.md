# swagger_client.LinkApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_get**](LinkApi.md#link_get) | **GET** /link | Get information about all links
[**link_link_id_delete**](LinkApi.md#link_link_id_delete) | **DELETE** /link/{linkId} | Deletes a link
[**link_link_id_get**](LinkApi.md#link_link_id_get) | **GET** /link/{linkId} | Find link by ID
[**link_link_id_put**](LinkApi.md#link_link_id_put) | **PUT** /link/{linkId} | Update a link by ID
[**link_post**](LinkApi.md#link_post) | **POST** /link | Add a new link


# **link_get**
> InlineResponse2005 link_get(api_key)

Get information about all links



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkApi()
api_key = 'api_key_example' # str | 

try: 
    # Get information about all links
    api_response = api_instance.link_get(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LinkApi->link_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_link_id_delete**
> link_link_id_delete(api_key, link_id)

Deletes a link



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkApi()
api_key = 'api_key_example' # str | 
link_id = 789 # int | Link ID to delete

try: 
    # Deletes a link
    api_instance.link_link_id_delete(api_key, link_id)
except ApiException as e:
    print "Exception when calling LinkApi->link_link_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **link_id** | **int**| Link ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_link_id_get**
> Link link_link_id_get(api_key, link_id)

Find link by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkApi()
api_key = 'api_key_example' # str | 
link_id = 789 # int | ID of link that needs to be fetched

try: 
    # Find link by ID
    api_response = api_instance.link_link_id_get(api_key, link_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LinkApi->link_link_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **link_id** | **int**| ID of link that needs to be fetched | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_link_id_put**
> InlineResponse2002 link_link_id_put(api_key, link_id, body)

Update a link by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkApi()
api_key = 'api_key_example' # str | 
link_id = 789 # int | ID of link that needs to be updated
body = swagger_client.LinkAddUpdate() # LinkAddUpdate | Link object that needs to be added

try: 
    # Update a link by ID
    api_response = api_instance.link_link_id_put(api_key, link_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LinkApi->link_link_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **link_id** | **int**| ID of link that needs to be updated | 
 **body** | [**LinkAddUpdate**](LinkAddUpdate.md)| Link object that needs to be added | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_post**
> InlineResponse2006 link_post(api_key, body)

Add a new link



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkApi()
api_key = 'api_key_example' # str | 
body = swagger_client.LinkAddUpdate() # LinkAddUpdate | Link object that needs to be added

try: 
    # Add a new link
    api_response = api_instance.link_post(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LinkApi->link_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**LinkAddUpdate**](LinkAddUpdate.md)| Link object that needs to be added | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

