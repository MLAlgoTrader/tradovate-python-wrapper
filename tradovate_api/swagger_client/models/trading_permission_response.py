# coding: utf-8

"""
    Tradovate API

    # Getting Started With the Tradovate API The Tradovate API is a robust web interface that clients can utilize to bring our Trading services to their own applications and  extensions. There are a number of supported operations that a client can perform by accessing the REST API. Essentially any functionality that is available on the Tradovate Trader application is also exposed via the API. For the comprehensive JavaScript guide to using our API, please go [here](https://github.com/tradovate/example-api-js/).  ## Place and Modify Orders The Tradovate REST API makes it easy to place and modify orders from code. Any type of order supported by the Tradovate Trader application is also able to be placed via the REST API. For interactive examples see the [Orders](#tag/Orders) section.  ## Query Positions, Contracts, Maturities and More From the Tradovate REST API we can get data about positions, contracts, products, prices, currencies, maturities, and more. Any data that you could view by browsing Tradovate Trader is queryable from the API. For interactive examples see the [ContractLibrary](#tag/ContractLibrary) section.  ## Query Account Data Using our `/account/*` operations allow you to do things like find an account by its ID, get a snapshot of an account's current cash balance, and access account trading permissions. For interactive examples see the [Accounting](#tag/Accounting) section.  ## Manage Risk We can use all of the risk management features available on Tradovate Trader from the API. This includes setting position limits and creating, deleting, and modifying risk-parameters. For live examples, see the [Risk](#tag/Risks) section.  ## Access Alert and Live Chat Functions You can use the REST API to generate alerts which can be seen from the Tradovate Trader application. You can use all of the Chat functionality from from  the REST API. This includes opening and closing the chat context, querying and posting chat message items, and even allowing us to mark a chat item as 'read'. For more examples see the [Alerts](#tag/Alerts) and [Chat](#tag/Chat) sections.  ## How Do I Use the Tradovate REST API? In order to access the features of the Tradovate REST API you'll need to sign up for a [Tradovate Trader](https://trader.tradovate.com/welcome) account. You must meet some other requirements as well: - You need a LIVE account with more than $1000 in equity. - You need a subscription to API Access. - You'll need to generate an API Key.  Then you simply need to acquire an access token using your API Key, as described in the [Access](#tag/Access) section.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TradingPermissionResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error_text': 'str',
        'trading_permission': 'TradingPermission'
    }

    attribute_map = {
        'error_text': 'errorText',
        'trading_permission': 'tradingPermission'
    }

    def __init__(self, error_text=None, trading_permission=None):  # noqa: E501
        """TradingPermissionResponse - a model defined in Swagger"""  # noqa: E501
        self._error_text = None
        self._trading_permission = None
        self.discriminator = None
        if error_text is not None:
            self.error_text = error_text
        if trading_permission is not None:
            self.trading_permission = trading_permission

    @property
    def error_text(self):
        """Gets the error_text of this TradingPermissionResponse.  # noqa: E501

        Non-empty if the request failed  # noqa: E501

        :return: The error_text of this TradingPermissionResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        """Sets the error_text of this TradingPermissionResponse.

        Non-empty if the request failed  # noqa: E501

        :param error_text: The error_text of this TradingPermissionResponse.  # noqa: E501
        :type: str
        """

        self._error_text = error_text

    @property
    def trading_permission(self):
        """Gets the trading_permission of this TradingPermissionResponse.  # noqa: E501


        :return: The trading_permission of this TradingPermissionResponse.  # noqa: E501
        :rtype: TradingPermission
        """
        return self._trading_permission

    @trading_permission.setter
    def trading_permission(self, trading_permission):
        """Sets the trading_permission of this TradingPermissionResponse.


        :param trading_permission: The trading_permission of this TradingPermissionResponse.  # noqa: E501
        :type: TradingPermission
        """

        self._trading_permission = trading_permission

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TradingPermissionResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TradingPermissionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
