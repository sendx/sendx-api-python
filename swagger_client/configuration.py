# coding: utf-8

"""
    SendX REST API

    **NOTE:** All API calls contain 2 parameters - 'api_key' and 'team_id'. These can be inferred from your settings page 'https://app.sendx.io/setting' under the sections 'Api Key' and 'Team Id' respectively.  For checking language specific Clients: -  [Golang](https://github.com/sendx/sendx-api-go) -  [Python](https://github.com/sendx/sendx-api-python) -  [Ruby](https://github.com/sendx/sendx-api-ruby) -  [Java](https://github.com/sendx/sendx-api-java) -  [PHP](https://github.com/sendx/sendx-api-php) -  [NodeJS](https://github.com/sendx/sendx-api-nodejs)  We also have a [Javascript API](http://help.sendx.io/knowledge_base/topics/javascript-api-1) for client side integrations.  SendX REST API has two methods:    * Identify   * Track    ## Identify API Method    Identify API Method is used to attach data to a visitor. If a contact is not yet created then we will create the contact. In case contact already exists then we update it.    **Example Request:**       ```json      {         email: \"john.doe@gmail.com\",         firstName: \"John\",         lastName: \"Doe\",         birthday: \"1989-03-03\",         customFields: {           \"Designation\": \"Software Engineer\",           \"Age\": \"27\",           \"Experience\": \"5\"         },         tags: [\"Developer\", \"API Team\"],      }   ```         Note that tags are an array of strings. In case they don't exist previously then API will create them and associate them with the contact.      Similarly if a custom field doesn't exist then it is first created and then associated with the contact along-with the corresponding value. In case custom field exists already then we simply update the value of it for the aforementioned contact.      We don't delete any of the properties based on identify call. What this means is that if for the same contact you did two API calls like:         **API Call A**        ```json      {         email: \"john.doe@gmail.com\",         firstName: \"John\",         birthday: \"1989-03-03\",         customFields: {           \"Designation\": \"Software Engineer\"         },         tags: [\"Developer\"],      }   ```         **API Call B**       ```json      {         email: \"john.doe@gmail.com\",         customFields: {           \"Age\": \"29\"         },         tags: [\"API Team\"],      }   ```         Then the final contact will have firstName as **John**, birthday as **1989-03-03** present. Also both tags **Developer** and **API Team** shall be present along with custom fields **Designation** and **Age**.         **Properties:**      * **firstName**: type string   * **lastName**: type string   * **email**: type string     * **newEmail**: type string     * **company**: type string     * **birthday**: type string with format **YYYY-MM-DD** eg: 2016-11-21     * **customFields**: type map[string]string      * **tags**: type array of string       In case email of an already existing contact needs to be updated then specify current email under email property and updated email under newEmail property.          **Response:**       ```json      {         \"status\": \"200\",         \"message\": \"OK\",         \"data\": {           \"encryptedTeamId\": \"CLdh9Ig5GLIN1u8gTRvoja\",           \"encryptedId\": \"c9QF63nrBenCaAXe660byz\",           \"tags\": [             \"API Team\",             \"Tech\"           ],           \"firstName\": \"John\",           \"lastName\": \"Doe\",           \"email\": \"john.doe@gmail.com\",           \"company\": \"\",           \"birthday\": \"1989-03-03\",           \"customFields\": {             \"Age\": \"29\",             \"Designation\": \"Software Engineer\"           }           }        }   ```         ## Track API Method      Track API Method is used to track a contact. In the track API object you can:      * **addTags**:   * **removeTags**:      You can have automation rules based on tag addition as well as tag removal and they will get executed. For eg:      * On **user registration** tag start onboarding drip for him / her.   * **Account Upgrade** tag start add user to paid user list and start account expansion drip.    * On removal of **trial user** tag start upsell trial completed users drip.         **Example Request:**      >     \\_scq.push([\"track\", {        \"addTags\": [\"blogger\", \"female\"]     }]);           >     \\_scq.push([\"track\", {        \"addTags\": [\"paid user\"],        \"removeTags\": [\"trial user\"]     }]);           **Response:**      >      {       \"status\": \"200\",       \"message\": \"OK\",       \"data\": \"success\"      } 

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import urllib3

import sys
import logging

from six import iteritems
from six.moves import http_client as httplib


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Configuration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Constructor
        """
        # Default Base url
        self.host = "https://app.sendx.io/api/v1"
        # Default api client
        self.api_client = None
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("swagger_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None

    @property
    def logger_file(self):
        """
        Gets the logger_file.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """
        Sets the logger_file.

        If the logger_file is None, then add stream handler and remove file handler.
        Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """
        Gets the debug status.
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """
        Sets the debug status.

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """
        Gets the logger_format.
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """
        Sets the logger_format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """
        Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.api_key.get(identifier) and self.api_key_prefix.get(identifier):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """
        Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(basic_auth=self.username + ':' + self.password)\
                           .get('authorization')

    def auth_settings(self):
        """
        Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {

        }

    def to_debug_report(self):
        """
        Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: v1\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)
