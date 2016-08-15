# swagger_client.ListApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_get**](ListApi.md#list_get) | **GET** /list | Get information about all lists
[**list_list_id_contacts_get**](ListApi.md#list_list_id_contacts_get) | **GET** /list/{listId}/contacts | Find contacts belonging to a list
[**list_list_id_delete**](ListApi.md#list_list_id_delete) | **DELETE** /list/{listId} | Deletes a list
[**list_list_id_get**](ListApi.md#list_list_id_get) | **GET** /list/{listId} | Find list by ID
[**list_list_id_put**](ListApi.md#list_list_id_put) | **PUT** /list/{listId} | Update a list by ID
[**list_post**](ListApi.md#list_post) | **POST** /list | Add a new list


# **list_get**
> InlineResponse2007 list_get(api_key)

Get information about all lists



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListApi()
api_key = 'api_key_example' # str | 

try: 
    # Get information about all lists
    api_response = api_instance.list_get(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListApi->list_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_list_id_contacts_get**
> list[DeepListEmailContact] list_list_id_contacts_get(api_key, list_id, limit=limit, offset=offset, contact_type=contact_type, search=search)

Find contacts belonging to a list



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListApi()
api_key = 'api_key_example' # str | 
list_id = 789 # int | ID of list that needs to be fetched
limit = 56 # int | Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. (optional)
offset = 56 # int | Offset from where we contacts should be retrieved. Default value is 0. (optional)
contact_type = 'contact_type_example' # str | Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all (optional)
search = 'search_example' # str | search term which shall be run against contact's first name, last name and email. (optional)

try: 
    # Find contacts belonging to a list
    api_response = api_instance.list_list_id_contacts_get(api_key, list_id, limit=limit, offset=offset, contact_type=contact_type, search=search)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListApi->list_list_id_contacts_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **list_id** | **int**| ID of list that needs to be fetched | 
 **limit** | **int**| Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. | [optional] 
 **offset** | **int**| Offset from where we contacts should be retrieved. Default value is 0. | [optional] 
 **contact_type** | **str**| Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all | [optional] 
 **search** | **str**| search term which shall be run against contact&#39;s first name, last name and email. | [optional] 

### Return type

[**list[DeepListEmailContact]**](DeepListEmailContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_list_id_delete**
> list_list_id_delete(api_key, list_id)

Deletes a list



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListApi()
api_key = 'api_key_example' # str | 
list_id = 789 # int | List ID to delete

try: 
    # Deletes a list
    api_instance.list_list_id_delete(api_key, list_id)
except ApiException as e:
    print "Exception when calling ListApi->list_list_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **list_id** | **int**| List ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_list_id_get**
> List list_list_id_get(api_key, list_id)

Find list by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListApi()
api_key = 'api_key_example' # str | 
list_id = 789 # int | ID of list that needs to be fetched

try: 
    # Find list by ID
    api_response = api_instance.list_list_id_get(api_key, list_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListApi->list_list_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **list_id** | **int**| ID of list that needs to be fetched | 

### Return type

[**List**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_list_id_put**
> InlineResponse2002 list_list_id_put(api_key, list_id, body)

Update a list by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListApi()
api_key = 'api_key_example' # str | 
list_id = 789 # int | ID of list that needs to be updated
body = swagger_client.ListAddUpdate() # ListAddUpdate | List object that needs to be added

try: 
    # Update a list by ID
    api_response = api_instance.list_list_id_put(api_key, list_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListApi->list_list_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **list_id** | **int**| ID of list that needs to be updated | 
 **body** | [**ListAddUpdate**](ListAddUpdate.md)| List object that needs to be added | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_post**
> InlineResponse2008 list_post(api_key, body)

Add a new list



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListApi()
api_key = 'api_key_example' # str | 
body = swagger_client.ListAddUpdate() # ListAddUpdate | List object that needs to be added

try: 
    # Add a new list
    api_response = api_instance.list_post(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListApi->list_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**ListAddUpdate**](ListAddUpdate.md)| List object that needs to be added | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

