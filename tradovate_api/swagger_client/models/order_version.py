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

class OrderVersion(object):
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
        'id': 'int',
        'order_id': 'int',
        'order_qty': 'int',
        'order_type': 'str',
        'price': 'float',
        'stop_price': 'float',
        'max_show': 'int',
        'peg_difference': 'float',
        'time_in_force': 'str',
        'expire_time': 'datetime',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'order_id': 'orderId',
        'order_qty': 'orderQty',
        'order_type': 'orderType',
        'price': 'price',
        'stop_price': 'stopPrice',
        'max_show': 'maxShow',
        'peg_difference': 'pegDifference',
        'time_in_force': 'timeInForce',
        'expire_time': 'expireTime',
        'text': 'text'
    }

    def __init__(self, id=None, order_id=None, order_qty=None, order_type=None, price=None, stop_price=None, max_show=None, peg_difference=None, time_in_force=None, expire_time=None, text=None):  # noqa: E501
        """OrderVersion - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._order_id = None
        self._order_qty = None
        self._order_type = None
        self._price = None
        self._stop_price = None
        self._max_show = None
        self._peg_difference = None
        self._time_in_force = None
        self._expire_time = None
        self._text = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.order_id = order_id
        self.order_qty = order_qty
        self.order_type = order_type
        if price is not None:
            self.price = price
        if stop_price is not None:
            self.stop_price = stop_price
        if max_show is not None:
            self.max_show = max_show
        if peg_difference is not None:
            self.peg_difference = peg_difference
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if expire_time is not None:
            self.expire_time = expire_time
        if text is not None:
            self.text = text

    @property
    def id(self):
        """Gets the id of this OrderVersion.  # noqa: E501


        :return: The id of this OrderVersion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderVersion.


        :param id: The id of this OrderVersion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def order_id(self):
        """Gets the order_id of this OrderVersion.  # noqa: E501


        :return: The order_id of this OrderVersion.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderVersion.


        :param order_id: The order_id of this OrderVersion.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def order_qty(self):
        """Gets the order_qty of this OrderVersion.  # noqa: E501


        :return: The order_qty of this OrderVersion.  # noqa: E501
        :rtype: int
        """
        return self._order_qty

    @order_qty.setter
    def order_qty(self, order_qty):
        """Sets the order_qty of this OrderVersion.


        :param order_qty: The order_qty of this OrderVersion.  # noqa: E501
        :type: int
        """
        if order_qty is None:
            raise ValueError("Invalid value for `order_qty`, must not be `None`")  # noqa: E501

        self._order_qty = order_qty

    @property
    def order_type(self):
        """Gets the order_type of this OrderVersion.  # noqa: E501

        Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit  # noqa: E501

        :return: The order_type of this OrderVersion.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this OrderVersion.

        Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit  # noqa: E501

        :param order_type: The order_type of this OrderVersion.  # noqa: E501
        :type: str
        """
        if order_type is None:
            raise ValueError("Invalid value for `order_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Limit", "MIT", "Market", "QTS", "Stop", "StopLimit", "TrailingStop", "TrailingStopLimit"]  # noqa: E501
        if order_type not in allowed_values:
            raise ValueError(
                "Invalid value for `order_type` ({0}), must be one of {1}"  # noqa: E501
                .format(order_type, allowed_values)
            )

        self._order_type = order_type

    @property
    def price(self):
        """Gets the price of this OrderVersion.  # noqa: E501


        :return: The price of this OrderVersion.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderVersion.


        :param price: The price of this OrderVersion.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def stop_price(self):
        """Gets the stop_price of this OrderVersion.  # noqa: E501


        :return: The stop_price of this OrderVersion.  # noqa: E501
        :rtype: float
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this OrderVersion.


        :param stop_price: The stop_price of this OrderVersion.  # noqa: E501
        :type: float
        """

        self._stop_price = stop_price

    @property
    def max_show(self):
        """Gets the max_show of this OrderVersion.  # noqa: E501


        :return: The max_show of this OrderVersion.  # noqa: E501
        :rtype: int
        """
        return self._max_show

    @max_show.setter
    def max_show(self, max_show):
        """Sets the max_show of this OrderVersion.


        :param max_show: The max_show of this OrderVersion.  # noqa: E501
        :type: int
        """

        self._max_show = max_show

    @property
    def peg_difference(self):
        """Gets the peg_difference of this OrderVersion.  # noqa: E501


        :return: The peg_difference of this OrderVersion.  # noqa: E501
        :rtype: float
        """
        return self._peg_difference

    @peg_difference.setter
    def peg_difference(self, peg_difference):
        """Sets the peg_difference of this OrderVersion.


        :param peg_difference: The peg_difference of this OrderVersion.  # noqa: E501
        :type: float
        """

        self._peg_difference = peg_difference

    @property
    def time_in_force(self):
        """Gets the time_in_force of this OrderVersion.  # noqa: E501

        Day, FOK, GTC, GTD, IOC  # noqa: E501

        :return: The time_in_force of this OrderVersion.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this OrderVersion.

        Day, FOK, GTC, GTD, IOC  # noqa: E501

        :param time_in_force: The time_in_force of this OrderVersion.  # noqa: E501
        :type: str
        """
        allowed_values = ["Day", "FOK", "GTC", "GTD", "IOC"]  # noqa: E501
        if time_in_force not in allowed_values:
            raise ValueError(
                "Invalid value for `time_in_force` ({0}), must be one of {1}"  # noqa: E501
                .format(time_in_force, allowed_values)
            )

        self._time_in_force = time_in_force

    @property
    def expire_time(self):
        """Gets the expire_time of this OrderVersion.  # noqa: E501


        :return: The expire_time of this OrderVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this OrderVersion.


        :param expire_time: The expire_time of this OrderVersion.  # noqa: E501
        :type: datetime
        """

        self._expire_time = expire_time

    @property
    def text(self):
        """Gets the text of this OrderVersion.  # noqa: E501


        :return: The text of this OrderVersion.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this OrderVersion.


        :param text: The text of this OrderVersion.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(OrderVersion, dict):
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
        if not isinstance(other, OrderVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
