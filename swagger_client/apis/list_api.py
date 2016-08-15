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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ListApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list_get(self, api_key, **kwargs):
        """
        Get information about all lists
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_get(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_get_with_http_info(api_key, **kwargs)
        else:
            (data) = self.list_get_with_http_info(api_key, **kwargs)
            return data

    def list_get_with_http_info(self, api_key, **kwargs):
        """
        Get information about all lists
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_get_with_http_info(api_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `list_get`")

        resource_path = '/list'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2007',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_list_id_contacts_get(self, api_key, list_id, **kwargs):
        """
        Find contacts belonging to a list
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_contacts_get(api_key, list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: ID of list that needs to be fetched (required)
        :param int limit: Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10.
        :param int offset: Offset from where we contacts should be retrieved. Default value is 0.
        :param str contact_type: Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all
        :param str search: search term which shall be run against contact's first name, last name and email.
        :return: list[DeepListEmailContact]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_list_id_contacts_get_with_http_info(api_key, list_id, **kwargs)
        else:
            (data) = self.list_list_id_contacts_get_with_http_info(api_key, list_id, **kwargs)
            return data

    def list_list_id_contacts_get_with_http_info(self, api_key, list_id, **kwargs):
        """
        Find contacts belonging to a list
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_contacts_get_with_http_info(api_key, list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: ID of list that needs to be fetched (required)
        :param int limit: Maximum number of contacts to be returned. Note that limit maximum value is 100 and default value is 10.
        :param int offset: Offset from where we contacts should be retrieved. Default value is 0.
        :param str contact_type: Can be any of the following - all, confirmed, unconfirmed, unsubscribed, bounced, markedspam. Default contact_type is all
        :param str search: search term which shall be run against contact's first name, last name and email.
        :return: list[DeepListEmailContact]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'list_id', 'limit', 'offset', 'contact_type', 'search']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_list_id_contacts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `list_list_id_contacts_get`")
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `list_list_id_contacts_get`")

        resource_path = '/list/{listId}/contacts'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'contact_type' in params:
            query_params['contact_type'] = params['contact_type']
        if 'search' in params:
            query_params['search'] = params['search']

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DeepListEmailContact]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_list_id_delete(self, api_key, list_id, **kwargs):
        """
        Deletes a list
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_delete(api_key, list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: List ID to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_list_id_delete_with_http_info(api_key, list_id, **kwargs)
        else:
            (data) = self.list_list_id_delete_with_http_info(api_key, list_id, **kwargs)
            return data

    def list_list_id_delete_with_http_info(self, api_key, list_id, **kwargs):
        """
        Deletes a list
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_delete_with_http_info(api_key, list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: List ID to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'list_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_list_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `list_list_id_delete`")
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `list_list_id_delete`")

        resource_path = '/list/{listId}'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_list_id_get(self, api_key, list_id, **kwargs):
        """
        Find list by ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_get(api_key, list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: ID of list that needs to be fetched (required)
        :return: List
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_list_id_get_with_http_info(api_key, list_id, **kwargs)
        else:
            (data) = self.list_list_id_get_with_http_info(api_key, list_id, **kwargs)
            return data

    def list_list_id_get_with_http_info(self, api_key, list_id, **kwargs):
        """
        Find list by ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_get_with_http_info(api_key, list_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: ID of list that needs to be fetched (required)
        :return: List
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'list_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_list_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `list_list_id_get`")
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `list_list_id_get`")

        resource_path = '/list/{listId}'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='List',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_list_id_put(self, api_key, list_id, body, **kwargs):
        """
        Update a list by ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_put(api_key, list_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: ID of list that needs to be updated (required)
        :param ListAddUpdate body: List object that needs to be added (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_list_id_put_with_http_info(api_key, list_id, body, **kwargs)
        else:
            (data) = self.list_list_id_put_with_http_info(api_key, list_id, body, **kwargs)
            return data

    def list_list_id_put_with_http_info(self, api_key, list_id, body, **kwargs):
        """
        Update a list by ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_list_id_put_with_http_info(api_key, list_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param int list_id: ID of list that needs to be updated (required)
        :param ListAddUpdate body: List object that needs to be added (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'list_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_list_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `list_list_id_put`")
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params) or (params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `list_list_id_put`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `list_list_id_put`")

        resource_path = '/list/{listId}'.replace('{format}', 'json')
        path_params = {}
        if 'list_id' in params:
            path_params['listId'] = params['list_id']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_post(self, api_key, body, **kwargs):
        """
        Add a new list
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_post(api_key, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param ListAddUpdate body: List object that needs to be added (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_post_with_http_info(api_key, body, **kwargs)
        else:
            (data) = self.list_post_with_http_info(api_key, body, **kwargs)
            return data

    def list_post_with_http_info(self, api_key, body, **kwargs):
        """
        Add a new list
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_post_with_http_info(api_key, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_key:  (required)
        :param ListAddUpdate body: List object that needs to be added (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params) or (params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `list_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `list_post`")

        resource_path = '/list'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2008',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))