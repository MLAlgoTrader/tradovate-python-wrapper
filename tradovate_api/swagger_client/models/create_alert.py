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

class CreateAlert(object):
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
        'expression': 'str',
        'valid_until': 'datetime',
        'trigger_limits': 'int',
        'message': 'str'
    }

    attribute_map = {
        'expression': 'expression',
        'valid_until': 'validUntil',
        'trigger_limits': 'triggerLimits',
        'message': 'message'
    }

    def __init__(self, expression=None, valid_until=None, trigger_limits=None, message=None):  # noqa: E501
        """CreateAlert - a model defined in Swagger"""  # noqa: E501
        self._expression = None
        self._valid_until = None
        self._trigger_limits = None
        self._message = None
        self.discriminator = None
        self.expression = expression
        if valid_until is not None:
            self.valid_until = valid_until
        if trigger_limits is not None:
            self.trigger_limits = trigger_limits
        if message is not None:
            self.message = message

    @property
    def expression(self):
        """Gets the expression of this CreateAlert.  # noqa: E501


        :return: The expression of this CreateAlert.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this CreateAlert.


        :param expression: The expression of this CreateAlert.  # noqa: E501
        :type: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def valid_until(self):
        """Gets the valid_until of this CreateAlert.  # noqa: E501


        :return: The valid_until of this CreateAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this CreateAlert.


        :param valid_until: The valid_until of this CreateAlert.  # noqa: E501
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def trigger_limits(self):
        """Gets the trigger_limits of this CreateAlert.  # noqa: E501


        :return: The trigger_limits of this CreateAlert.  # noqa: E501
        :rtype: int
        """
        return self._trigger_limits

    @trigger_limits.setter
    def trigger_limits(self, trigger_limits):
        """Sets the trigger_limits of this CreateAlert.


        :param trigger_limits: The trigger_limits of this CreateAlert.  # noqa: E501
        :type: int
        """

        self._trigger_limits = trigger_limits

    @property
    def message(self):
        """Gets the message of this CreateAlert.  # noqa: E501


        :return: The message of this CreateAlert.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateAlert.


        :param message: The message of this CreateAlert.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(CreateAlert, dict):
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
        if not isinstance(other, CreateAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
