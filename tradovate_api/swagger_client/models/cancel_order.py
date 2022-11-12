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

class CancelOrder(object):
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
        'order_id': 'int',
        'cl_ord_id': 'str',
        'activation_time': 'datetime',
        'custom_tag50': 'str',
        'is_automated': 'bool'
    }

    attribute_map = {
        'order_id': 'orderId',
        'cl_ord_id': 'clOrdId',
        'activation_time': 'activationTime',
        'custom_tag50': 'customTag50',
        'is_automated': 'isAutomated'
    }

    def __init__(self, order_id=None, cl_ord_id=None, activation_time=None, custom_tag50=None, is_automated=None):  # noqa: E501
        """CancelOrder - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._cl_ord_id = None
        self._activation_time = None
        self._custom_tag50 = None
        self._is_automated = None
        self.discriminator = None
        self.order_id = order_id
        if cl_ord_id is not None:
            self.cl_ord_id = cl_ord_id
        if activation_time is not None:
            self.activation_time = activation_time
        if custom_tag50 is not None:
            self.custom_tag50 = custom_tag50
        if is_automated is not None:
            self.is_automated = is_automated

    @property
    def order_id(self):
        """Gets the order_id of this CancelOrder.  # noqa: E501


        :return: The order_id of this CancelOrder.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CancelOrder.


        :param order_id: The order_id of this CancelOrder.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def cl_ord_id(self):
        """Gets the cl_ord_id of this CancelOrder.  # noqa: E501


        :return: The cl_ord_id of this CancelOrder.  # noqa: E501
        :rtype: str
        """
        return self._cl_ord_id

    @cl_ord_id.setter
    def cl_ord_id(self, cl_ord_id):
        """Sets the cl_ord_id of this CancelOrder.


        :param cl_ord_id: The cl_ord_id of this CancelOrder.  # noqa: E501
        :type: str
        """

        self._cl_ord_id = cl_ord_id

    @property
    def activation_time(self):
        """Gets the activation_time of this CancelOrder.  # noqa: E501


        :return: The activation_time of this CancelOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._activation_time

    @activation_time.setter
    def activation_time(self, activation_time):
        """Sets the activation_time of this CancelOrder.


        :param activation_time: The activation_time of this CancelOrder.  # noqa: E501
        :type: datetime
        """

        self._activation_time = activation_time

    @property
    def custom_tag50(self):
        """Gets the custom_tag50 of this CancelOrder.  # noqa: E501


        :return: The custom_tag50 of this CancelOrder.  # noqa: E501
        :rtype: str
        """
        return self._custom_tag50

    @custom_tag50.setter
    def custom_tag50(self, custom_tag50):
        """Sets the custom_tag50 of this CancelOrder.


        :param custom_tag50: The custom_tag50 of this CancelOrder.  # noqa: E501
        :type: str
        """

        self._custom_tag50 = custom_tag50

    @property
    def is_automated(self):
        """Gets the is_automated of this CancelOrder.  # noqa: E501


        :return: The is_automated of this CancelOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_automated

    @is_automated.setter
    def is_automated(self, is_automated):
        """Sets the is_automated of this CancelOrder.


        :param is_automated: The is_automated of this CancelOrder.  # noqa: E501
        :type: bool
        """

        self._is_automated = is_automated

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
        if issubclass(CancelOrder, dict):
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
        if not isinstance(other, CancelOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
