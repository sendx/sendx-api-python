# swagger_client.TagApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tag_get**](TagApi.md#tag_get) | **GET** /tag | Get information about all tags
[**tag_post**](TagApi.md#tag_post) | **POST** /tag | Add a new tag
[**tag_tag_id_contact_delete**](TagApi.md#tag_tag_id_contact_delete) | **DELETE** /tag/{tagId}/contact | Remove a contact from a tag
[**tag_tag_id_contact_post**](TagApi.md#tag_tag_id_contact_post) | **POST** /tag/{tagId}/contact | Add a contact to a tag
[**tag_tag_id_contacts_get**](TagApi.md#tag_tag_id_contacts_get) | **GET** /tag/{tagId}/contacts | Find contacts belonging to a tag
[**tag_tag_id_delete**](TagApi.md#tag_tag_id_delete) | **DELETE** /tag/{tagId} | Deletes a tag
[**tag_tag_id_get**](TagApi.md#tag_tag_id_get) | **GET** /tag/{tagId} | Find tag by ID
[**tag_tag_id_put**](TagApi.md#tag_tag_id_put) | **PUT** /tag/{tagId} | Update a tag by ID


# **tag_get**
> InlineResponse2009 tag_get(api_key)

Get information about all tags



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 

try: 
    # Get information about all tags
    api_response = api_instance.tag_get(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagApi->tag_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_post**
> InlineResponse20010 tag_post(api_key, body)

Add a new tag



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
body = swagger_client.TagAddUpdate() # TagAddUpdate | Tag object that needs to be added

try: 
    # Add a new tag
    api_response = api_instance.tag_post(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagApi->tag_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**TagAddUpdate**](TagAddUpdate.md)| Tag object that needs to be added | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_tag_id_contact_delete**
> tag_tag_id_contact_delete(api_key, tag_id, body)

Remove a contact from a tag



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
tag_id = 789 # int | ID of tag for which contact needs to be remove
body = swagger_client.TagContact() # TagContact | Contact email and team id

try: 
    # Remove a contact from a tag
    api_instance.tag_tag_id_contact_delete(api_key, tag_id, body)
except ApiException as e:
    print "Exception when calling TagApi->tag_tag_id_contact_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tag_id** | **int**| ID of tag for which contact needs to be remove | 
 **body** | [**TagContact**](TagContact.md)| Contact email and team id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_tag_id_contact_post**
> InlineResponse20011 tag_tag_id_contact_post(api_key, tag_id, body)

Add a contact to a tag



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
tag_id = 789 # int | ID of tag for which the contact needs to be added
body = swagger_client.TagContact() # TagContact | Contact email and team id

try: 
    # Add a contact to a tag
    api_response = api_instance.tag_tag_id_contact_post(api_key, tag_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagApi->tag_tag_id_contact_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tag_id** | **int**| ID of tag for which the contact needs to be added | 
 **body** | [**TagContact**](TagContact.md)| Contact email and team id | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_tag_id_contacts_get**
> list[DeepTeamEmailContact] tag_tag_id_contacts_get(api_key, tag_id, limit=limit, offset=offset, contact_type=contact_type, search=search)

Find contacts belonging to a tag



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
tag_id = 789 # int | ID of tag that needs to be fetched
limit = 56 # int | Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. (optional)
offset = 56 # int | Offset from where we contacts should be retrieved. Default value is 0. (optional)
contact_type = 'contact_type_example' # str | Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all (optional)
search = 'search_example' # str | search term which shall be run against contact's first name, last name and email. (optional)

try: 
    # Find contacts belonging to a tag
    api_response = api_instance.tag_tag_id_contacts_get(api_key, tag_id, limit=limit, offset=offset, contact_type=contact_type, search=search)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagApi->tag_tag_id_contacts_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tag_id** | **int**| ID of tag that needs to be fetched | 
 **limit** | **int**| Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. | [optional] 
 **offset** | **int**| Offset from where we contacts should be retrieved. Default value is 0. | [optional] 
 **contact_type** | **str**| Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all | [optional] 
 **search** | **str**| search term which shall be run against contact&#39;s first name, last name and email. | [optional] 

### Return type

[**list[DeepTeamEmailContact]**](DeepTeamEmailContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_tag_id_delete**
> tag_tag_id_delete(api_key, tag_id)

Deletes a tag



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
tag_id = 789 # int | Tag ID to delete

try: 
    # Deletes a tag
    api_instance.tag_tag_id_delete(api_key, tag_id)
except ApiException as e:
    print "Exception when calling TagApi->tag_tag_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tag_id** | **int**| Tag ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_tag_id_get**
> Tag tag_tag_id_get(api_key, tag_id)

Find tag by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
tag_id = 789 # int | ID of tag that needs to be fetched

try: 
    # Find tag by ID
    api_response = api_instance.tag_tag_id_get(api_key, tag_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagApi->tag_tag_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tag_id** | **int**| ID of tag that needs to be fetched | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_tag_id_put**
> InlineResponse2002 tag_tag_id_put(api_key, tag_id, body)

Update a tag by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagApi()
api_key = 'api_key_example' # str | 
tag_id = 789 # int | ID of tag that needs to be updated
body = swagger_client.TagAddUpdate() # TagAddUpdate | Tag object that needs to be added

try: 
    # Update a tag by ID
    api_response = api_instance.tag_tag_id_put(api_key, tag_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagApi->tag_tag_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **tag_id** | **int**| ID of tag that needs to be updated | 
 **body** | [**TagAddUpdate**](TagAddUpdate.md)| Tag object that needs to be added | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

