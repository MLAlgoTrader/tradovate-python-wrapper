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

class PlaceOCO(object):
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
        'account_spec': 'str',
        'account_id': 'int',
        'cl_ord_id': 'str',
        'action': 'str',
        'symbol': 'str',
        'order_qty': 'int',
        'order_type': 'str',
        'price': 'float',
        'stop_price': 'float',
        'max_show': 'int',
        'peg_difference': 'float',
        'time_in_force': 'str',
        'expire_time': 'datetime',
        'text': 'str',
        'activation_time': 'datetime',
        'custom_tag50': 'str',
        'is_automated': 'bool',
        'other': 'RestrainedOrderVersion'
    }

    attribute_map = {
        'account_spec': 'accountSpec',
        'account_id': 'accountId',
        'cl_ord_id': 'clOrdId',
        'action': 'action',
        'symbol': 'symbol',
        'order_qty': 'orderQty',
        'order_type': 'orderType',
        'price': 'price',
        'stop_price': 'stopPrice',
        'max_show': 'maxShow',
        'peg_difference': 'pegDifference',
        'time_in_force': 'timeInForce',
        'expire_time': 'expireTime',
        'text': 'text',
        'activation_time': 'activationTime',
        'custom_tag50': 'customTag50',
        'is_automated': 'isAutomated',
        'other': 'other'
    }

    def __init__(self, account_spec=None, account_id=None, cl_ord_id=None, action=None, symbol=None, order_qty=None, order_type=None, price=None, stop_price=None, max_show=None, peg_difference=None, time_in_force=None, expire_time=None, text=None, activation_time=None, custom_tag50=None, is_automated=None, other=None):  # noqa: E501
        """PlaceOCO - a model defined in Swagger"""  # noqa: E501
        self._account_spec = None
        self._account_id = None
        self._cl_ord_id = None
        self._action = None
        self._symbol = None
        self._order_qty = None
        self._order_type = None
        self._price = None
        self._stop_price = None
        self._max_show = None
        self._peg_difference = None
        self._time_in_force = None
        self._expire_time = None
        self._text = None
        self._activation_time = None
        self._custom_tag50 = None
        self._is_automated = None
        self._other = None
        self.discriminator = None
        if account_spec is not None:
            self.account_spec = account_spec
        if account_id is not None:
            self.account_id = account_id
        if cl_ord_id is not None:
            self.cl_ord_id = cl_ord_id
        self.action = action
        self.symbol = symbol
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
        if activation_time is not None:
            self.activation_time = activation_time
        if custom_tag50 is not None:
            self.custom_tag50 = custom_tag50
        if is_automated is not None:
            self.is_automated = is_automated
        self.other = other

    @property
    def account_spec(self):
        """Gets the account_spec of this PlaceOCO.  # noqa: E501


        :return: The account_spec of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._account_spec

    @account_spec.setter
    def account_spec(self, account_spec):
        """Sets the account_spec of this PlaceOCO.


        :param account_spec: The account_spec of this PlaceOCO.  # noqa: E501
        :type: str
        """

        self._account_spec = account_spec

    @property
    def account_id(self):
        """Gets the account_id of this PlaceOCO.  # noqa: E501


        :return: The account_id of this PlaceOCO.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PlaceOCO.


        :param account_id: The account_id of this PlaceOCO.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def cl_ord_id(self):
        """Gets the cl_ord_id of this PlaceOCO.  # noqa: E501


        :return: The cl_ord_id of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._cl_ord_id

    @cl_ord_id.setter
    def cl_ord_id(self, cl_ord_id):
        """Sets the cl_ord_id of this PlaceOCO.


        :param cl_ord_id: The cl_ord_id of this PlaceOCO.  # noqa: E501
        :type: str
        """

        self._cl_ord_id = cl_ord_id

    @property
    def action(self):
        """Gets the action of this PlaceOCO.  # noqa: E501

        Buy, Sell  # noqa: E501

        :return: The action of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PlaceOCO.

        Buy, Sell  # noqa: E501

        :param action: The action of this PlaceOCO.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["Buy", "Sell"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def symbol(self):
        """Gets the symbol of this PlaceOCO.  # noqa: E501


        :return: The symbol of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this PlaceOCO.


        :param symbol: The symbol of this PlaceOCO.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def order_qty(self):
        """Gets the order_qty of this PlaceOCO.  # noqa: E501


        :return: The order_qty of this PlaceOCO.  # noqa: E501
        :rtype: int
        """
        return self._order_qty

    @order_qty.setter
    def order_qty(self, order_qty):
        """Sets the order_qty of this PlaceOCO.


        :param order_qty: The order_qty of this PlaceOCO.  # noqa: E501
        :type: int
        """
        if order_qty is None:
            raise ValueError("Invalid value for `order_qty`, must not be `None`")  # noqa: E501

        self._order_qty = order_qty

    @property
    def order_type(self):
        """Gets the order_type of this PlaceOCO.  # noqa: E501

        Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit  # noqa: E501

        :return: The order_type of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this PlaceOCO.

        Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit  # noqa: E501

        :param order_type: The order_type of this PlaceOCO.  # noqa: E501
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
        """Gets the price of this PlaceOCO.  # noqa: E501


        :return: The price of this PlaceOCO.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PlaceOCO.


        :param price: The price of this PlaceOCO.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def stop_price(self):
        """Gets the stop_price of this PlaceOCO.  # noqa: E501


        :return: The stop_price of this PlaceOCO.  # noqa: E501
        :rtype: float
        """
        return self._stop_price

    @stop_price.setter
    def stop_price(self, stop_price):
        """Sets the stop_price of this PlaceOCO.


        :param stop_price: The stop_price of this PlaceOCO.  # noqa: E501
        :type: float
        """

        self._stop_price = stop_price

    @property
    def max_show(self):
        """Gets the max_show of this PlaceOCO.  # noqa: E501


        :return: The max_show of this PlaceOCO.  # noqa: E501
        :rtype: int
        """
        return self._max_show

    @max_show.setter
    def max_show(self, max_show):
        """Sets the max_show of this PlaceOCO.


        :param max_show: The max_show of this PlaceOCO.  # noqa: E501
        :type: int
        """

        self._max_show = max_show

    @property
    def peg_difference(self):
        """Gets the peg_difference of this PlaceOCO.  # noqa: E501


        :return: The peg_difference of this PlaceOCO.  # noqa: E501
        :rtype: float
        """
        return self._peg_difference

    @peg_difference.setter
    def peg_difference(self, peg_difference):
        """Sets the peg_difference of this PlaceOCO.


        :param peg_difference: The peg_difference of this PlaceOCO.  # noqa: E501
        :type: float
        """

        self._peg_difference = peg_difference

    @property
    def time_in_force(self):
        """Gets the time_in_force of this PlaceOCO.  # noqa: E501

        Day, FOK, GTC, GTD, IOC  # noqa: E501

        :return: The time_in_force of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this PlaceOCO.

        Day, FOK, GTC, GTD, IOC  # noqa: E501

        :param time_in_force: The time_in_force of this PlaceOCO.  # noqa: E501
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
        """Gets the expire_time of this PlaceOCO.  # noqa: E501


        :return: The expire_time of this PlaceOCO.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this PlaceOCO.


        :param expire_time: The expire_time of this PlaceOCO.  # noqa: E501
        :type: datetime
        """

        self._expire_time = expire_time

    @property
    def text(self):
        """Gets the text of this PlaceOCO.  # noqa: E501


        :return: The text of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PlaceOCO.


        :param text: The text of this PlaceOCO.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def activation_time(self):
        """Gets the activation_time of this PlaceOCO.  # noqa: E501


        :return: The activation_time of this PlaceOCO.  # noqa: E501
        :rtype: datetime
        """
        return self._activation_time

    @activation_time.setter
    def activation_time(self, activation_time):
        """Sets the activation_time of this PlaceOCO.


        :param activation_time: The activation_time of this PlaceOCO.  # noqa: E501
        :type: datetime
        """

        self._activation_time = activation_time

    @property
    def custom_tag50(self):
        """Gets the custom_tag50 of this PlaceOCO.  # noqa: E501


        :return: The custom_tag50 of this PlaceOCO.  # noqa: E501
        :rtype: str
        """
        return self._custom_tag50

    @custom_tag50.setter
    def custom_tag50(self, custom_tag50):
        """Sets the custom_tag50 of this PlaceOCO.


        :param custom_tag50: The custom_tag50 of this PlaceOCO.  # noqa: E501
        :type: str
        """

        self._custom_tag50 = custom_tag50

    @property
    def is_automated(self):
        """Gets the is_automated of this PlaceOCO.  # noqa: E501


        :return: The is_automated of this PlaceOCO.  # noqa: E501
        :rtype: bool
        """
        return self._is_automated

    @is_automated.setter
    def is_automated(self, is_automated):
        """Sets the is_automated of this PlaceOCO.


        :param is_automated: The is_automated of this PlaceOCO.  # noqa: E501
        :type: bool
        """

        self._is_automated = is_automated

    @property
    def other(self):
        """Gets the other of this PlaceOCO.  # noqa: E501


        :return: The other of this PlaceOCO.  # noqa: E501
        :rtype: RestrainedOrderVersion
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this PlaceOCO.


        :param other: The other of this PlaceOCO.  # noqa: E501
        :type: RestrainedOrderVersion
        """
        if other is None:
            raise ValueError("Invalid value for `other`, must not be `None`")  # noqa: E501

        self._other = other

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
        if issubclass(PlaceOCO, dict):
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
        if not isinstance(other, PlaceOCO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
