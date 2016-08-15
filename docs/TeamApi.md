# swagger_client.TeamApi

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_get**](TeamApi.md#team_get) | **GET** /team | Get information about all teams
[**team_post**](TeamApi.md#team_post) | **POST** /team | Add a new team
[**team_team_id_campaigns_get**](TeamApi.md#team_team_id_campaigns_get) | **GET** /team/{teamId}/campaigns | Find campaigns of a team by ID
[**team_team_id_contacts_get**](TeamApi.md#team_team_id_contacts_get) | **GET** /team/{teamId}/contacts | Find contacts of a team by ID
[**team_team_id_delete**](TeamApi.md#team_team_id_delete) | **DELETE** /team/{teamId} | Deletes a team
[**team_team_id_get**](TeamApi.md#team_team_id_get) | **GET** /team/{teamId} | Find team by ID
[**team_team_id_lists_get**](TeamApi.md#team_team_id_lists_get) | **GET** /team/{teamId}/lists | Find lists of a team by ID
[**team_team_id_put**](TeamApi.md#team_team_id_put) | **PUT** /team/{teamId} | Update a team by ID
[**team_team_id_tags_get**](TeamApi.md#team_team_id_tags_get) | **GET** /team/{teamId}/tags | Find tags of a team by ID


# **team_get**
> InlineResponse20012 team_get(api_key)

Get information about all teams



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 

try: 
    # Get information about all teams
    api_response = api_instance.team_get(api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_post**
> InlineResponse20013 team_post(api_key, body)

Add a new team



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
body = swagger_client.TeamAddUpdate() # TeamAddUpdate | Team object that needs to be added

try: 
    # Add a new team
    api_response = api_instance.team_post(api_key, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **body** | [**TeamAddUpdate**](TeamAddUpdate.md)| Team object that needs to be added | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_id_campaigns_get**
> list[Campaign] team_team_id_campaigns_get(api_key, team_id)

Find campaigns of a team by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | ID of team whose campaigns need to be fetched

try: 
    # Find campaigns of a team by ID
    api_response = api_instance.team_team_id_campaigns_get(api_key, team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_campaigns_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| ID of team whose campaigns need to be fetched | 

### Return type

[**list[Campaign]**](Campaign.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_id_contacts_get**
> list[DeepTeamEmailContact] team_team_id_contacts_get(api_key, team_id, limit=limit, offset=offset, contact_type=contact_type, search=search)

Find contacts of a team by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | ID of team whose campaigns need to be fetched
limit = 56 # int | Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10. (optional)
offset = 56 # int | Offset from where we contacts should be retrieved. Default value is 0. (optional)
contact_type = 'contact_type_example' # str | Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all (optional)
search = 'search_example' # str | search term which shall be run against contact's first name, last name and email. (optional)

try: 
    # Find contacts of a team by ID
    api_response = api_instance.team_team_id_contacts_get(api_key, team_id, limit=limit, offset=offset, contact_type=contact_type, search=search)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_contacts_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| ID of team whose campaigns need to be fetched | 
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

# **team_team_id_delete**
> team_team_id_delete(api_key, team_id)

Deletes a team



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | Team ID to delete

try: 
    # Deletes a team
    api_instance.team_team_id_delete(api_key, team_id)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| Team ID to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_id_get**
> Team team_team_id_get(api_key, team_id)

Find team by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | ID of team that needs to be fetched

try: 
    # Find team by ID
    api_response = api_instance.team_team_id_get(api_key, team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| ID of team that needs to be fetched | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_id_lists_get**
> list[List] team_team_id_lists_get(api_key, team_id)

Find lists of a team by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | ID of team whose campaigns need to be fetched

try: 
    # Find lists of a team by ID
    api_response = api_instance.team_team_id_lists_get(api_key, team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_lists_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| ID of team whose campaigns need to be fetched | 

### Return type

[**list[List]**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_id_put**
> InlineResponse2002 team_team_id_put(api_key, team_id, body)

Update a team by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | ID of team that needs to be updated
body = swagger_client.TeamAddUpdate() # TeamAddUpdate | Team object that needs to be added

try: 
    # Update a team by ID
    api_response = api_instance.team_team_id_put(api_key, team_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| ID of team that needs to be updated | 
 **body** | [**TeamAddUpdate**](TeamAddUpdate.md)| Team object that needs to be added | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_id_tags_get**
> list[Tag] team_team_id_tags_get(api_key, team_id)

Find tags of a team by ID



### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamApi()
api_key = 'api_key_example' # str | 
team_id = 789 # int | ID of team whose campaigns need to be fetched

try: 
    # Find tags of a team by ID
    api_response = api_instance.team_team_id_tags_get(api_key, team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamApi->team_team_id_tags_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **team_id** | **int**| ID of team whose campaigns need to be fetched | 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

