# swagger_client.ContactApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_contact_id_delete**](ContactApi.md#contact_contact_id_delete) | **DELETE** /contact/{contactId} | Deletes a contact
[**contact_contact_id_get**](ContactApi.md#contact_contact_id_get) | **GET** /contact/{contactId} | Find contact by ID
[**contact_contact_id_put**](ContactApi.md#contact_contact_id_put) | **PUT** /contact/{contactId} | Update a contact by ID
[**contact_get**](ContactApi.md#contact_get) | **GET** /contact | Get information about all contacts
[**contact_post**](ContactApi.md#contact_post) | **POST** /contact | Add a new contact


# **contact_contact_id_delete**
> contact_contact_id_delete(api_key, contact_id)

Deletes a contact



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
contact_id = 789 # int | Contact ID to delete

try: 
    # Deletes a contact
    api_instance.contact_contact_id_delete(api_key, contact_id)
except ApiException as e:
    print "Exception when calling ContactApi->contact_contact_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **contact_id** | **int**| Contact ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_contact_id_get**
> Contact contact_contact_id_get(api_key, contact_id)

Find contact by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
contact_id = 789 # int | ID of contact that needs to be fetched

try: 
    # Find contact by ID
    api_response = api_instance.contact_contact_id_get(api_key, contact_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactApi->contact_contact_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **contact_id** | **int**| ID of contact that needs to be fetched | 

### Return type

[**Contact**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_contact_id_put**
> InlineResponse2002 contact_contact_id_put(api_key, contact_id, body)

Update a contact by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
contact_id = 789 # int | ID of contact that needs to be updated
body = swagger_client.ContactAddUpdate() # ContactAddUpdate | Contact object that needs to be added

try: 
    # Update a contact by ID
    api_response = api_instance.contact_contact_id_put(api_key, contact_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactApi->contact_contact_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **contact_id** | **int**| ID of contact that needs to be updated | 
 **body** | [**ContactAddUpdate**](ContactAddUpdate.md)| Contact object that needs to be added | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_get**
> InlineResponse2003 contact_get(api_key, limit=limit, offset=offset)

Get information about all contacts



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
limit = 56 # int | Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. (optional)
offset = 56 # int | Offset from where we contacts should be retrieved. Default value is 0. (optional)

try: 
    # Get information about all contacts
    api_response = api_instance.contact_get(api_key, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactApi->contact_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **limit** | **int**| Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. | [optional] 
 **offset** | **int**| Offset from where we contacts should be retrieved. Default value is 0. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_post**
> InlineResponse2004 contact_post(api_key, body)

Add a new contact



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
body = swagger_client.ContactAddUpdate() # ContactAddUpdate | Contact object that needs to be added

try: 
    # Add a new contact
    api_response = api_instance.contact_post(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ContactApi->contact_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**ContactAddUpdate**](ContactAddUpdate.md)| Contact object that needs to be added | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

