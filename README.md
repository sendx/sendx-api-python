# SendX Python Client

SendX REST API has two methods:

* [Identify](#identify_api)
* [Track](#track_api)

## <a name="identify_api"></a> Identify API Method

Identify API Method is used to attach data to a visitor. If a contact is not yet created then we will create the contact. In case contact already exists then we update it.

**Example Request:**

> 
    {
      email: "john.doe@gmail.com",  
      firstName: "John",
      lastName: "Doe",
      birthday: "1989-03-03",
      customFields: { "Designation": "Software Engineer", "Age": "27", "Experience": "5"},  
      tags: ["Developer", "API Team"],  
     }


Note that tags are an array of strings. In case they don't exist previously then API will create them and associate them with the contact.

Similarly if a custom field doesn't exist then it is first created and then associated with the contact along-with the corresponding value. In case custom field exists already then we simply update the value of it for the aforementioned contact.

We don't delete any of the properties based on identify call. What this means is that if for the same contact you did two API calls like:


**API Call A**
 
> 
    {
       email: "john.doe@gmail.com", 
       firstName: "John",
       birthday: "1989-03-03",
       customFields: { "Designation": "Software Engineer"},  
       tags: ["Developer"],  
    }


**API Call B**

> 
    {  
      email: "john.doe@gmail.com",  
      customFields: { "Age": "29"},  
      tags: ["API Team"],  
    }


The the final contact will have firstName as **John**, birthday as **1989-03-03** present. Also both tags **Developer** and **API Team** shall be present alongwith custom fields **Designation** and **Age**.


**Properties:**

* **firstName**: type string
* **lastName**: type string
* **email**: type string  
* **company**: type string  
* **birthday**: type string with format **YYYY-MM-DD** eg: 2016-11-21  
* **customFields**: type map[string]string   
* **tags**: type array of string 


**Response:**

> 
    {
      "status": "200",
      "message": "OK",
      "data": {
        "encryptedTeamId": "CLdh9Ig5GLIN1u8gTRvoja",
        "encryptedId": "c9QF63nrBenCaAXe660byz",
        "tags": [
          "API Team",
          "Tech"
        ],
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@gmail.com",
        "company": "",
        "birthday": "1989-03-03",
        "customFields": {
          "Age": "29",
          "Designation": "Software Engineer"
        }
      }
    }


## <a name="track_api"></a> Track API Method


Track API Method is used to associate **tags** with a contact. You can have automation rules based on tag addition and they will get executed. For eg:

* **On user registration** tag start onboarding drip for him / her.
* **Account Upgrade** tag start add user to paid user list and start account expansion drip. 

**Response:**

>
   {
    "status": "200",
    "message": "OK",
    "data": "success"
   }

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
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
from __future__ import print_function
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

## Documentation for API Endpoints

All URIs are relative to *http://app.sendx.io/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContactApi* | [**contact_identify_post**](docs/ContactApi.md#contact_identify_post) | **POST** /contact/identify | Identify a contact as user
*ContactApi* | [**contact_track_post**](docs/ContactApi.md#contact_track_post) | **POST** /contact/track | Add tracking info using tags to a contact


## Documentation For Models

 - [Contact](docs/Contact.md)
 - [ContactResponse](docs/ContactResponse.md)
 - [TrackResponse](docs/TrackResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



