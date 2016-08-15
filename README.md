# SendX API Python
SendX is built on the simple tenet that users must have open access to their data. SendX API is the first step in that direction. To cite some examples:   - subscribe / unsubscribe a contact from a list   - Schedule campaign to a segment of users   - Trigger transactional emails   - Get / PUT / POST and DELETE operations on team, campaign, list, contact, report etc. and so on.  As companies grow big, custom use cases around email marketing also crop up. SendX API ensures   that SendX platform is able to satisfy such unforeseen use cases. They may range from building     custom reporting dashboard to tagging contacts with custom attributes or triggering emails based on recommendation algorithm.  We do our best to have all our URLs be [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer). Every endpoint (URL) may support one of four different http verbs. GET requests fetch information about an object, POST requests create objects, PUT requests update objects, and finally DELETE requests will delete objects.  Also all API calls besides:   - Subscribe / unsubscribe signup form  required **api_key** to be passed as **header**   ### The Envelope Every response is contained by an envelope. That is, each response has a predictable set of keys with which you can expect to interact: ```json {     \"status\": \"200\",      \"message\": \"OK\",     \"data\"\": [        {          ...        },        .        .        .     ] } ```  #### Status  The status key is used to communicate extra information about the response to the developer. If all goes well, you'll only ever see a code key with value 200. However, sometimes things go wrong, and in that case you might see a response like: ```json {     \"status\": \"404\" } ```  #### Data  The data key is the meat of the response. It may be a list containing single object or multiple objects  #### Message  This returns back human readable message. This is specially useful to make sense in case of error scenarios. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build date: 2016-08-15T11:00:27.460Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.CampaignApi
api_key = 'api_key_example' # str | 
campaign_id = 789 # int | Campaign ID to delete

try:
    # Deletes a campaign
    api_instance.campaign_campaign_id_delete(api_key, campaign_id)
except ApiException as e:
    print "Exception when calling CampaignApi->campaign_campaign_id_delete: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8080/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignApi* | [**campaign_campaign_id_delete**](docs/CampaignApi.md#campaign_campaign_id_delete) | **DELETE** /campaign/{campaignId} | Deletes a campaign
*CampaignApi* | [**campaign_campaign_id_get**](docs/CampaignApi.md#campaign_campaign_id_get) | **GET** /campaign/{campaignId} | Find campaign by ID
*CampaignApi* | [**campaign_campaign_id_put**](docs/CampaignApi.md#campaign_campaign_id_put) | **PUT** /campaign/{campaignId} | Update a campaign by ID
*CampaignApi* | [**campaign_get**](docs/CampaignApi.md#campaign_get) | **GET** /campaign | Get information about all campaigns
*CampaignApi* | [**campaign_post**](docs/CampaignApi.md#campaign_post) | **POST** /campaign | Add a new campaign
*ContactApi* | [**contact_contact_id_delete**](docs/ContactApi.md#contact_contact_id_delete) | **DELETE** /contact/{contactId} | Deletes a contact
*ContactApi* | [**contact_contact_id_get**](docs/ContactApi.md#contact_contact_id_get) | **GET** /contact/{contactId} | Find contact by ID
*ContactApi* | [**contact_contact_id_put**](docs/ContactApi.md#contact_contact_id_put) | **PUT** /contact/{contactId} | Update a contact by ID
*ContactApi* | [**contact_get**](docs/ContactApi.md#contact_get) | **GET** /contact | Get information about all contacts
*ContactApi* | [**contact_post**](docs/ContactApi.md#contact_post) | **POST** /contact | Add a new contact
*LinkApi* | [**link_get**](docs/LinkApi.md#link_get) | **GET** /link | Get information about all links
*LinkApi* | [**link_link_id_delete**](docs/LinkApi.md#link_link_id_delete) | **DELETE** /link/{linkId} | Deletes a link
*LinkApi* | [**link_link_id_get**](docs/LinkApi.md#link_link_id_get) | **GET** /link/{linkId} | Find link by ID
*LinkApi* | [**link_link_id_put**](docs/LinkApi.md#link_link_id_put) | **PUT** /link/{linkId} | Update a link by ID
*LinkApi* | [**link_post**](docs/LinkApi.md#link_post) | **POST** /link | Add a new link
*ListApi* | [**list_get**](docs/ListApi.md#list_get) | **GET** /list | Get information about all lists
*ListApi* | [**list_list_id_contacts_get**](docs/ListApi.md#list_list_id_contacts_get) | **GET** /list/{listId}/contacts | Find contacts belonging to a list
*ListApi* | [**list_list_id_delete**](docs/ListApi.md#list_list_id_delete) | **DELETE** /list/{listId} | Deletes a list
*ListApi* | [**list_list_id_get**](docs/ListApi.md#list_list_id_get) | **GET** /list/{listId} | Find list by ID
*ListApi* | [**list_list_id_put**](docs/ListApi.md#list_list_id_put) | **PUT** /list/{listId} | Update a list by ID
*ListApi* | [**list_post**](docs/ListApi.md#list_post) | **POST** /list | Add a new list
*SendApi* | [**send_email_post**](docs/SendApi.md#send_email_post) | **POST** /send/email | Send transactional email to user
*SubscribeApi* | [**subscribe_encrypted_list_id_post**](docs/SubscribeApi.md#subscribe_encrypted_list_id_post) | **POST** /subscribe/{encryptedListId} | Subscribe a new user a list
*SubscribeApi* | [**subscribe_encrypted_list_id_put**](docs/SubscribeApi.md#subscribe_encrypted_list_id_put) | **PUT** /subscribe/{encryptedListId} | Subscribe an existing user a list
*TagApi* | [**tag_get**](docs/TagApi.md#tag_get) | **GET** /tag | Get information about all tags
*TagApi* | [**tag_post**](docs/TagApi.md#tag_post) | **POST** /tag | Add a new tag
*TagApi* | [**tag_tag_id_contact_delete**](docs/TagApi.md#tag_tag_id_contact_delete) | **DELETE** /tag/{tagId}/contact | Remove a contact from a tag
*TagApi* | [**tag_tag_id_contact_post**](docs/TagApi.md#tag_tag_id_contact_post) | **POST** /tag/{tagId}/contact | Add a contact to a tag
*TagApi* | [**tag_tag_id_contacts_get**](docs/TagApi.md#tag_tag_id_contacts_get) | **GET** /tag/{tagId}/contacts | Find contacts belonging to a tag
*TagApi* | [**tag_tag_id_delete**](docs/TagApi.md#tag_tag_id_delete) | **DELETE** /tag/{tagId} | Deletes a tag
*TagApi* | [**tag_tag_id_get**](docs/TagApi.md#tag_tag_id_get) | **GET** /tag/{tagId} | Find tag by ID
*TagApi* | [**tag_tag_id_put**](docs/TagApi.md#tag_tag_id_put) | **PUT** /tag/{tagId} | Update a tag by ID
*TeamApi* | [**team_get**](docs/TeamApi.md#team_get) | **GET** /team | Get information about all teams
*TeamApi* | [**team_post**](docs/TeamApi.md#team_post) | **POST** /team | Add a new team
*TeamApi* | [**team_team_id_campaigns_get**](docs/TeamApi.md#team_team_id_campaigns_get) | **GET** /team/{teamId}/campaigns | Find campaigns of a team by ID
*TeamApi* | [**team_team_id_contacts_get**](docs/TeamApi.md#team_team_id_contacts_get) | **GET** /team/{teamId}/contacts | Find contacts of a team by ID
*TeamApi* | [**team_team_id_delete**](docs/TeamApi.md#team_team_id_delete) | **DELETE** /team/{teamId} | Deletes a team
*TeamApi* | [**team_team_id_get**](docs/TeamApi.md#team_team_id_get) | **GET** /team/{teamId} | Find team by ID
*TeamApi* | [**team_team_id_lists_get**](docs/TeamApi.md#team_team_id_lists_get) | **GET** /team/{teamId}/lists | Find lists of a team by ID
*TeamApi* | [**team_team_id_put**](docs/TeamApi.md#team_team_id_put) | **PUT** /team/{teamId} | Update a team by ID
*TeamApi* | [**team_team_id_tags_get**](docs/TeamApi.md#team_team_id_tags_get) | **GET** /team/{teamId}/tags | Find tags of a team by ID
*UnsubscribeApi* | [**unsubscribe_encrypted_list_id_post**](docs/UnsubscribeApi.md#unsubscribe_encrypted_list_id_post) | **POST** /unsubscribe/{encryptedListId} | Unsubscribe a user from list based on email id


## Documentation For Models

 - [Campaign](docs/Campaign.md)
 - [CampaignAddUpdate](docs/CampaignAddUpdate.md)
 - [Contact](docs/Contact.md)
 - [ContactAddUpdate](docs/ContactAddUpdate.md)
 - [DeepListEmailContact](docs/DeepListEmailContact.md)
 - [DeepTeamEmailContact](docs/DeepTeamEmailContact.md)
 - [EContent](docs/EContent.md)
 - [EMessage](docs/EMessage.md)
 - [Email](docs/Email.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Link](docs/Link.md)
 - [LinkAddUpdate](docs/LinkAddUpdate.md)
 - [List](docs/List.md)
 - [ListAddUpdate](docs/ListAddUpdate.md)
 - [Tag](docs/Tag.md)
 - [TagAddUpdate](docs/TagAddUpdate.md)
 - [TagContact](docs/TagContact.md)
 - [TagContactId](docs/TagContactId.md)
 - [Team](docs/Team.md)
 - [TeamAddUpdate](docs/TeamAddUpdate.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



