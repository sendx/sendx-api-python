# swagger_client.ContactApi

All URIs are relative to *http://app.sendx.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_identify_post**](ContactApi.md#contact_identify_post) | **POST** /contact/identify | Identify a contact as user
[**contact_track_post**](ContactApi.md#contact_track_post) | **POST** /contact/track | Add tracking info using tags to a contact


# **contact_identify_post**
> ContactResponse contact_identify_post(api_key, team_id, body)

Identify a contact as user



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
team_id = 'team_id_example' # str | 
body = swagger_client.Contact() # Contact | Contact details

try: 
    # Identify a contact as user
    api_response = api_instance.contact_identify_post(api_key, team_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_identify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **str**|  | 
 **body** | [**Contact**](Contact.md)| Contact details | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_track_post**
> TrackResponse contact_track_post(api_key, team_id, contact_id, tag)

Add tracking info using tags to a contact



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
api_key = 'api_key_example' # str | 
team_id = 'team_id_example' # str | 
contact_id = 'contact_id_example' # str | 
tag = 'tag_example' # str | 

try: 
    # Add tracking info using tags to a contact
    api_response = api_instance.contact_track_post(api_key, team_id, contact_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_track_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **str**|  | 
 **contact_id** | **str**|  | 
 **tag** | **str**|  | 

### Return type

[**TrackResponse**](TrackResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

