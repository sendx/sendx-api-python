# swagger_client.CampaignApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaign_campaign_id_delete**](CampaignApi.md#campaign_campaign_id_delete) | **DELETE** /campaign/{campaignId} | Deletes a campaign
[**campaign_campaign_id_get**](CampaignApi.md#campaign_campaign_id_get) | **GET** /campaign/{campaignId} | Find campaign by ID
[**campaign_campaign_id_put**](CampaignApi.md#campaign_campaign_id_put) | **PUT** /campaign/{campaignId} | Update a campaign by ID
[**campaign_get**](CampaignApi.md#campaign_get) | **GET** /campaign | Get information about all campaigns
[**campaign_post**](CampaignApi.md#campaign_post) | **POST** /campaign | Add a new campaign


# **campaign_campaign_id_delete**
> campaign_campaign_id_delete(api_key, campaign_id)

Deletes a campaign



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignApi()
api_key = 'api_key_example' # str | 
campaign_id = 789 # int | Campaign ID to delete

try: 
    # Deletes a campaign
    api_instance.campaign_campaign_id_delete(api_key, campaign_id)
except ApiException as e:
    print "Exception when calling CampaignApi->campaign_campaign_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **campaign_id** | **int**| Campaign ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_campaign_id_get**
> Campaign campaign_campaign_id_get(api_key, campaign_id)

Find campaign by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignApi()
api_key = 'api_key_example' # str | 
campaign_id = 789 # int | ID of campaign that needs to be fetched

try: 
    # Find campaign by ID
    api_response = api_instance.campaign_campaign_id_get(api_key, campaign_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignApi->campaign_campaign_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **campaign_id** | **int**| ID of campaign that needs to be fetched | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_campaign_id_put**
> InlineResponse2002 campaign_campaign_id_put(api_key, campaign_id, body)

Update a campaign by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignApi()
api_key = 'api_key_example' # str | 
campaign_id = 789 # int | ID of campaign that needs to be updated
body = swagger_client.CampaignAddUpdate() # CampaignAddUpdate | Campaign object that needs to be added

try: 
    # Update a campaign by ID
    api_response = api_instance.campaign_campaign_id_put(api_key, campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignApi->campaign_campaign_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **campaign_id** | **int**| ID of campaign that needs to be updated | 
 **body** | [**CampaignAddUpdate**](CampaignAddUpdate.md)| Campaign object that needs to be added | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_get**
> InlineResponse200 campaign_get(api_key)

Get information about all campaigns



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignApi()
api_key = 'api_key_example' # str | 

try: 
    # Get information about all campaigns
    api_response = api_instance.campaign_get(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignApi->campaign_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_post**
> InlineResponse2001 campaign_post(api_key, body)

Add a new campaign



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignApi()
api_key = 'api_key_example' # str | 
body = swagger_client.CampaignAddUpdate() # CampaignAddUpdate | Campaign object that needs to be added

try: 
    # Add a new campaign
    api_response = api_instance.campaign_post(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CampaignApi->campaign_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**CampaignAddUpdate**](CampaignAddUpdate.md)| Campaign object that needs to be added | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

