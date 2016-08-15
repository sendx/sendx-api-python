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


class ListAddUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, encrypted_id=None, name=None, type=None, thankyou_from_email=None, thankyou_mail_subject=None, thankyou_mail_message=None, confirm_from_email=None, confirm_mail_subject=None, confirm_mail_message=None, goodbye_from_email=None, goodbye_mail_subject=None, goodbye_mail_message=None, send_thank_you_mail=None, send_confirm_unsubscribe_mail=None, subscribe_success_page=None, confirm_success_page=None, unsubscribe_success_page=None, team_id=None, subscribed=None, confirmed=None, unsubscribed=None, bounced=None, marked_spam=None):
        """
        ListAddUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'encrypted_id': 'str',
            'name': 'str',
            'type': 'int',
            'thankyou_from_email': 'str',
            'thankyou_mail_subject': 'str',
            'thankyou_mail_message': 'str',
            'confirm_from_email': 'str',
            'confirm_mail_subject': 'str',
            'confirm_mail_message': 'str',
            'goodbye_from_email': 'str',
            'goodbye_mail_subject': 'str',
            'goodbye_mail_message': 'str',
            'send_thank_you_mail': 'bool',
            'send_confirm_unsubscribe_mail': 'bool',
            'subscribe_success_page': 'str',
            'confirm_success_page': 'str',
            'unsubscribe_success_page': 'str',
            'team_id': 'int',
            'subscribed': 'int',
            'confirmed': 'int',
            'unsubscribed': 'int',
            'bounced': 'int',
            'marked_spam': 'int'
        }

        self.attribute_map = {
            'encrypted_id': 'encryptedId',
            'name': 'name',
            'type': 'type',
            'thankyou_from_email': 'thankyou_from_email',
            'thankyou_mail_subject': 'thankyouMailSubject',
            'thankyou_mail_message': 'thankyouMailMessage',
            'confirm_from_email': 'confirm_from_email',
            'confirm_mail_subject': 'confirmMailSubject',
            'confirm_mail_message': 'confirmMailMessage',
            'goodbye_from_email': 'goodbye_from_email',
            'goodbye_mail_subject': 'goodbyeMailSubject',
            'goodbye_mail_message': 'goodbyeMailMessage',
            'send_thank_you_mail': 'sendThankYouMail',
            'send_confirm_unsubscribe_mail': 'sendConfirmUnsubscribeMail',
            'subscribe_success_page': 'subscribeSuccessPage',
            'confirm_success_page': 'confirmSuccessPage',
            'unsubscribe_success_page': 'unsubscribeSuccessPage',
            'team_id': 'team_id',
            'subscribed': 'subscribed',
            'confirmed': 'confirmed',
            'unsubscribed': 'unsubscribed',
            'bounced': 'bounced',
            'marked_spam': 'marked_spam'
        }

        self._encrypted_id = encrypted_id
        self._name = name
        self._type = type
        self._thankyou_from_email = thankyou_from_email
        self._thankyou_mail_subject = thankyou_mail_subject
        self._thankyou_mail_message = thankyou_mail_message
        self._confirm_from_email = confirm_from_email
        self._confirm_mail_subject = confirm_mail_subject
        self._confirm_mail_message = confirm_mail_message
        self._goodbye_from_email = goodbye_from_email
        self._goodbye_mail_subject = goodbye_mail_subject
        self._goodbye_mail_message = goodbye_mail_message
        self._send_thank_you_mail = send_thank_you_mail
        self._send_confirm_unsubscribe_mail = send_confirm_unsubscribe_mail
        self._subscribe_success_page = subscribe_success_page
        self._confirm_success_page = confirm_success_page
        self._unsubscribe_success_page = unsubscribe_success_page
        self._team_id = team_id
        self._subscribed = subscribed
        self._confirmed = confirmed
        self._unsubscribed = unsubscribed
        self._bounced = bounced
        self._marked_spam = marked_spam

    @property
    def encrypted_id(self):
        """
        Gets the encrypted_id of this ListAddUpdate.


        :return: The encrypted_id of this ListAddUpdate.
        :rtype: str
        """
        return self._encrypted_id

    @encrypted_id.setter
    def encrypted_id(self, encrypted_id):
        """
        Sets the encrypted_id of this ListAddUpdate.


        :param encrypted_id: The encrypted_id of this ListAddUpdate.
        :type: str
        """

        self._encrypted_id = encrypted_id

    @property
    def name(self):
        """
        Gets the name of this ListAddUpdate.


        :return: The name of this ListAddUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListAddUpdate.


        :param name: The name of this ListAddUpdate.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ListAddUpdate.


        :return: The type of this ListAddUpdate.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ListAddUpdate.


        :param type: The type of this ListAddUpdate.
        :type: int
        """

        self._type = type

    @property
    def thankyou_from_email(self):
        """
        Gets the thankyou_from_email of this ListAddUpdate.


        :return: The thankyou_from_email of this ListAddUpdate.
        :rtype: str
        """
        return self._thankyou_from_email

    @thankyou_from_email.setter
    def thankyou_from_email(self, thankyou_from_email):
        """
        Sets the thankyou_from_email of this ListAddUpdate.


        :param thankyou_from_email: The thankyou_from_email of this ListAddUpdate.
        :type: str
        """

        self._thankyou_from_email = thankyou_from_email

    @property
    def thankyou_mail_subject(self):
        """
        Gets the thankyou_mail_subject of this ListAddUpdate.


        :return: The thankyou_mail_subject of this ListAddUpdate.
        :rtype: str
        """
        return self._thankyou_mail_subject

    @thankyou_mail_subject.setter
    def thankyou_mail_subject(self, thankyou_mail_subject):
        """
        Sets the thankyou_mail_subject of this ListAddUpdate.


        :param thankyou_mail_subject: The thankyou_mail_subject of this ListAddUpdate.
        :type: str
        """

        self._thankyou_mail_subject = thankyou_mail_subject

    @property
    def thankyou_mail_message(self):
        """
        Gets the thankyou_mail_message of this ListAddUpdate.


        :return: The thankyou_mail_message of this ListAddUpdate.
        :rtype: str
        """
        return self._thankyou_mail_message

    @thankyou_mail_message.setter
    def thankyou_mail_message(self, thankyou_mail_message):
        """
        Sets the thankyou_mail_message of this ListAddUpdate.


        :param thankyou_mail_message: The thankyou_mail_message of this ListAddUpdate.
        :type: str
        """

        self._thankyou_mail_message = thankyou_mail_message

    @property
    def confirm_from_email(self):
        """
        Gets the confirm_from_email of this ListAddUpdate.


        :return: The confirm_from_email of this ListAddUpdate.
        :rtype: str
        """
        return self._confirm_from_email

    @confirm_from_email.setter
    def confirm_from_email(self, confirm_from_email):
        """
        Sets the confirm_from_email of this ListAddUpdate.


        :param confirm_from_email: The confirm_from_email of this ListAddUpdate.
        :type: str
        """

        self._confirm_from_email = confirm_from_email

    @property
    def confirm_mail_subject(self):
        """
        Gets the confirm_mail_subject of this ListAddUpdate.


        :return: The confirm_mail_subject of this ListAddUpdate.
        :rtype: str
        """
        return self._confirm_mail_subject

    @confirm_mail_subject.setter
    def confirm_mail_subject(self, confirm_mail_subject):
        """
        Sets the confirm_mail_subject of this ListAddUpdate.


        :param confirm_mail_subject: The confirm_mail_subject of this ListAddUpdate.
        :type: str
        """

        self._confirm_mail_subject = confirm_mail_subject

    @property
    def confirm_mail_message(self):
        """
        Gets the confirm_mail_message of this ListAddUpdate.


        :return: The confirm_mail_message of this ListAddUpdate.
        :rtype: str
        """
        return self._confirm_mail_message

    @confirm_mail_message.setter
    def confirm_mail_message(self, confirm_mail_message):
        """
        Sets the confirm_mail_message of this ListAddUpdate.


        :param confirm_mail_message: The confirm_mail_message of this ListAddUpdate.
        :type: str
        """

        self._confirm_mail_message = confirm_mail_message

    @property
    def goodbye_from_email(self):
        """
        Gets the goodbye_from_email of this ListAddUpdate.


        :return: The goodbye_from_email of this ListAddUpdate.
        :rtype: str
        """
        return self._goodbye_from_email

    @goodbye_from_email.setter
    def goodbye_from_email(self, goodbye_from_email):
        """
        Sets the goodbye_from_email of this ListAddUpdate.


        :param goodbye_from_email: The goodbye_from_email of this ListAddUpdate.
        :type: str
        """

        self._goodbye_from_email = goodbye_from_email

    @property
    def goodbye_mail_subject(self):
        """
        Gets the goodbye_mail_subject of this ListAddUpdate.


        :return: The goodbye_mail_subject of this ListAddUpdate.
        :rtype: str
        """
        return self._goodbye_mail_subject

    @goodbye_mail_subject.setter
    def goodbye_mail_subject(self, goodbye_mail_subject):
        """
        Sets the goodbye_mail_subject of this ListAddUpdate.


        :param goodbye_mail_subject: The goodbye_mail_subject of this ListAddUpdate.
        :type: str
        """

        self._goodbye_mail_subject = goodbye_mail_subject

    @property
    def goodbye_mail_message(self):
        """
        Gets the goodbye_mail_message of this ListAddUpdate.


        :return: The goodbye_mail_message of this ListAddUpdate.
        :rtype: str
        """
        return self._goodbye_mail_message

    @goodbye_mail_message.setter
    def goodbye_mail_message(self, goodbye_mail_message):
        """
        Sets the goodbye_mail_message of this ListAddUpdate.


        :param goodbye_mail_message: The goodbye_mail_message of this ListAddUpdate.
        :type: str
        """

        self._goodbye_mail_message = goodbye_mail_message

    @property
    def send_thank_you_mail(self):
        """
        Gets the send_thank_you_mail of this ListAddUpdate.


        :return: The send_thank_you_mail of this ListAddUpdate.
        :rtype: bool
        """
        return self._send_thank_you_mail

    @send_thank_you_mail.setter
    def send_thank_you_mail(self, send_thank_you_mail):
        """
        Sets the send_thank_you_mail of this ListAddUpdate.


        :param send_thank_you_mail: The send_thank_you_mail of this ListAddUpdate.
        :type: bool
        """

        self._send_thank_you_mail = send_thank_you_mail

    @property
    def send_confirm_unsubscribe_mail(self):
        """
        Gets the send_confirm_unsubscribe_mail of this ListAddUpdate.


        :return: The send_confirm_unsubscribe_mail of this ListAddUpdate.
        :rtype: bool
        """
        return self._send_confirm_unsubscribe_mail

    @send_confirm_unsubscribe_mail.setter
    def send_confirm_unsubscribe_mail(self, send_confirm_unsubscribe_mail):
        """
        Sets the send_confirm_unsubscribe_mail of this ListAddUpdate.


        :param send_confirm_unsubscribe_mail: The send_confirm_unsubscribe_mail of this ListAddUpdate.
        :type: bool
        """

        self._send_confirm_unsubscribe_mail = send_confirm_unsubscribe_mail

    @property
    def subscribe_success_page(self):
        """
        Gets the subscribe_success_page of this ListAddUpdate.


        :return: The subscribe_success_page of this ListAddUpdate.
        :rtype: str
        """
        return self._subscribe_success_page

    @subscribe_success_page.setter
    def subscribe_success_page(self, subscribe_success_page):
        """
        Sets the subscribe_success_page of this ListAddUpdate.


        :param subscribe_success_page: The subscribe_success_page of this ListAddUpdate.
        :type: str
        """

        self._subscribe_success_page = subscribe_success_page

    @property
    def confirm_success_page(self):
        """
        Gets the confirm_success_page of this ListAddUpdate.


        :return: The confirm_success_page of this ListAddUpdate.
        :rtype: str
        """
        return self._confirm_success_page

    @confirm_success_page.setter
    def confirm_success_page(self, confirm_success_page):
        """
        Sets the confirm_success_page of this ListAddUpdate.


        :param confirm_success_page: The confirm_success_page of this ListAddUpdate.
        :type: str
        """

        self._confirm_success_page = confirm_success_page

    @property
    def unsubscribe_success_page(self):
        """
        Gets the unsubscribe_success_page of this ListAddUpdate.


        :return: The unsubscribe_success_page of this ListAddUpdate.
        :rtype: str
        """
        return self._unsubscribe_success_page

    @unsubscribe_success_page.setter
    def unsubscribe_success_page(self, unsubscribe_success_page):
        """
        Sets the unsubscribe_success_page of this ListAddUpdate.


        :param unsubscribe_success_page: The unsubscribe_success_page of this ListAddUpdate.
        :type: str
        """

        self._unsubscribe_success_page = unsubscribe_success_page

    @property
    def team_id(self):
        """
        Gets the team_id of this ListAddUpdate.


        :return: The team_id of this ListAddUpdate.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this ListAddUpdate.


        :param team_id: The team_id of this ListAddUpdate.
        :type: int
        """

        self._team_id = team_id

    @property
    def subscribed(self):
        """
        Gets the subscribed of this ListAddUpdate.


        :return: The subscribed of this ListAddUpdate.
        :rtype: int
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """
        Sets the subscribed of this ListAddUpdate.


        :param subscribed: The subscribed of this ListAddUpdate.
        :type: int
        """

        self._subscribed = subscribed

    @property
    def confirmed(self):
        """
        Gets the confirmed of this ListAddUpdate.


        :return: The confirmed of this ListAddUpdate.
        :rtype: int
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """
        Sets the confirmed of this ListAddUpdate.


        :param confirmed: The confirmed of this ListAddUpdate.
        :type: int
        """

        self._confirmed = confirmed

    @property
    def unsubscribed(self):
        """
        Gets the unsubscribed of this ListAddUpdate.


        :return: The unsubscribed of this ListAddUpdate.
        :rtype: int
        """
        return self._unsubscribed

    @unsubscribed.setter
    def unsubscribed(self, unsubscribed):
        """
        Sets the unsubscribed of this ListAddUpdate.


        :param unsubscribed: The unsubscribed of this ListAddUpdate.
        :type: int
        """

        self._unsubscribed = unsubscribed

    @property
    def bounced(self):
        """
        Gets the bounced of this ListAddUpdate.


        :return: The bounced of this ListAddUpdate.
        :rtype: int
        """
        return self._bounced

    @bounced.setter
    def bounced(self, bounced):
        """
        Sets the bounced of this ListAddUpdate.


        :param bounced: The bounced of this ListAddUpdate.
        :type: int
        """

        self._bounced = bounced

    @property
    def marked_spam(self):
        """
        Gets the marked_spam of this ListAddUpdate.


        :return: The marked_spam of this ListAddUpdate.
        :rtype: int
        """
        return self._marked_spam

    @marked_spam.setter
    def marked_spam(self, marked_spam):
        """
        Sets the marked_spam of this ListAddUpdate.


        :param marked_spam: The marked_spam of this ListAddUpdate.
        :type: int
        """

        self._marked_spam = marked_spam

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