# coding: utf-8

"""
    SendX API

    SendX is built on the simple tenet that users must have open access to their data. SendX API is the first step in that direction. To cite some examples:   - subscribe / unsubscribe a contact from a list   - Schedule campaign to a segment of users   - Trigger transactional emails   - Get / PUT / POST and DELETE operations on team, campaign, list, contact, report etc. and so on.  As companies grow big, custom use cases around email marketing also crop up. SendX API ensures   that SendX platform is able to satisfy such unforeseen use cases. They may range from building     custom reporting dashboard to tagging contacts with custom attributes or triggering emails based on recommendation algorithm.  We do our best to have all our URLs be [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer). Every endpoint (URL) may support one of four different http verbs. GET requests fetch information about an object, POST requests create objects, PUT requests update objects, and finally DELETE requests will delete objects.  Also all API calls besides:   - Subscribe / unsubscribe signup form  required **api_key** to be passed as **header**   ### The Envelope Every response is contained by an envelope. That is, each response has a predictable set of keys with which you can expect to interact: ```json {     \"status\": \"200\",      \"message\": \"OK\",     \"data\"\": [        {          ...        },        .        .        .     ] } ```  #### Status  The status key is used to communicate extra information about the response to the developer. If all goes well, you'll only ever see a code key with value 200. However, sometimes things go wrong, and in that case you might see a response like: ```json {     \"status\": \"404\" } ```  #### Data  The data key is the meat of the response. It may be a list containing single object or multiple objects  #### Message  This returns back human readable message. This is specially useful to make sense in case of error scenarios. 

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

from pprint import pformat
from six import iteritems
import re


class DeepTeamEmailContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, first_name=None, last_name=None, name=None, email=None, list_ids=None):
        """
        DeepTeamEmailContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'first_name': 'str',
            'last_name': 'str',
            'name': 'str',
            'email': 'str',
            'list_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'name': 'name',
            'email': 'email',
            'list_ids': 'list_ids'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._name = name
        self._email = email
        self._list_ids = list_ids

    @property
    def id(self):
        """
        Gets the id of this DeepTeamEmailContact.


        :return: The id of this DeepTeamEmailContact.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeepTeamEmailContact.


        :param id: The id of this DeepTeamEmailContact.
        :type: int
        """

        self._id = id

    @property
    def first_name(self):
        """
        Gets the first_name of this DeepTeamEmailContact.


        :return: The first_name of this DeepTeamEmailContact.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this DeepTeamEmailContact.


        :param first_name: The first_name of this DeepTeamEmailContact.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this DeepTeamEmailContact.


        :return: The last_name of this DeepTeamEmailContact.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this DeepTeamEmailContact.


        :param last_name: The last_name of this DeepTeamEmailContact.
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """
        Gets the name of this DeepTeamEmailContact.


        :return: The name of this DeepTeamEmailContact.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeepTeamEmailContact.


        :param name: The name of this DeepTeamEmailContact.
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """
        Gets the email of this DeepTeamEmailContact.


        :return: The email of this DeepTeamEmailContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this DeepTeamEmailContact.


        :param email: The email of this DeepTeamEmailContact.
        :type: str
        """

        self._email = email

    @property
    def list_ids(self):
        """
        Gets the list_ids of this DeepTeamEmailContact.


        :return: The list_ids of this DeepTeamEmailContact.
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """
        Sets the list_ids of this DeepTeamEmailContact.


        :param list_ids: The list_ids of this DeepTeamEmailContact.
        :type: list[int]
        """

        self._list_ids = list_ids

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
