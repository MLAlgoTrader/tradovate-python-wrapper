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

class SecondMarketDataSubscription(object):
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
        'user_id': 'int',
        'timestamp': 'datetime',
        'year': 'int',
        'month': 'int',
        'cancelled_renewal': 'bool',
        'cancellation_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'timestamp': 'timestamp',
        'year': 'year',
        'month': 'month',
        'cancelled_renewal': 'cancelledRenewal',
        'cancellation_timestamp': 'cancellationTimestamp'
    }

    def __init__(self, id=None, user_id=None, timestamp=None, year=None, month=None, cancelled_renewal=None, cancellation_timestamp=None):  # noqa: E501
        """SecondMarketDataSubscription - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._timestamp = None
        self._year = None
        self._month = None
        self._cancelled_renewal = None
        self._cancellation_timestamp = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.user_id = user_id
        self.timestamp = timestamp
        self.year = year
        self.month = month
        if cancelled_renewal is not None:
            self.cancelled_renewal = cancelled_renewal
        if cancellation_timestamp is not None:
            self.cancellation_timestamp = cancellation_timestamp

    @property
    def id(self):
        """Gets the id of this SecondMarketDataSubscription.  # noqa: E501


        :return: The id of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecondMarketDataSubscription.


        :param id: The id of this SecondMarketDataSubscription.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this SecondMarketDataSubscription.  # noqa: E501


        :return: The user_id of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SecondMarketDataSubscription.


        :param user_id: The user_id of this SecondMarketDataSubscription.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def timestamp(self):
        """Gets the timestamp of this SecondMarketDataSubscription.  # noqa: E501


        :return: The timestamp of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SecondMarketDataSubscription.


        :param timestamp: The timestamp of this SecondMarketDataSubscription.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def year(self):
        """Gets the year of this SecondMarketDataSubscription.  # noqa: E501


        :return: The year of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this SecondMarketDataSubscription.


        :param year: The year of this SecondMarketDataSubscription.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self):
        """Gets the month of this SecondMarketDataSubscription.  # noqa: E501


        :return: The month of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this SecondMarketDataSubscription.


        :param month: The month of this SecondMarketDataSubscription.  # noqa: E501
        :type: int
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def cancelled_renewal(self):
        """Gets the cancelled_renewal of this SecondMarketDataSubscription.  # noqa: E501


        :return: The cancelled_renewal of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._cancelled_renewal

    @cancelled_renewal.setter
    def cancelled_renewal(self, cancelled_renewal):
        """Sets the cancelled_renewal of this SecondMarketDataSubscription.


        :param cancelled_renewal: The cancelled_renewal of this SecondMarketDataSubscription.  # noqa: E501
        :type: bool
        """

        self._cancelled_renewal = cancelled_renewal

    @property
    def cancellation_timestamp(self):
        """Gets the cancellation_timestamp of this SecondMarketDataSubscription.  # noqa: E501


        :return: The cancellation_timestamp of this SecondMarketDataSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._cancellation_timestamp

    @cancellation_timestamp.setter
    def cancellation_timestamp(self, cancellation_timestamp):
        """Sets the cancellation_timestamp of this SecondMarketDataSubscription.


        :param cancellation_timestamp: The cancellation_timestamp of this SecondMarketDataSubscription.  # noqa: E501
        :type: datetime
        """

        self._cancellation_timestamp = cancellation_timestamp

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
        if issubclass(SecondMarketDataSubscription, dict):
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
        if not isinstance(other, SecondMarketDataSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
