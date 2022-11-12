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

class MarginSnapshot(object):
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
        'timestamp': 'datetime',
        'risk_time_period_id': 'int',
        'initial_margin': 'float',
        'maintenance_margin': 'float',
        'auto_liq_level': 'float',
        'liq_only_level': 'float',
        'total_used_margin': 'float',
        'full_initial_margin': 'float'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'risk_time_period_id': 'riskTimePeriodId',
        'initial_margin': 'initialMargin',
        'maintenance_margin': 'maintenanceMargin',
        'auto_liq_level': 'autoLiqLevel',
        'liq_only_level': 'liqOnlyLevel',
        'total_used_margin': 'totalUsedMargin',
        'full_initial_margin': 'fullInitialMargin'
    }

    def __init__(self, id=None, timestamp=None, risk_time_period_id=None, initial_margin=None, maintenance_margin=None, auto_liq_level=None, liq_only_level=None, total_used_margin=None, full_initial_margin=None):  # noqa: E501
        """MarginSnapshot - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._timestamp = None
        self._risk_time_period_id = None
        self._initial_margin = None
        self._maintenance_margin = None
        self._auto_liq_level = None
        self._liq_only_level = None
        self._total_used_margin = None
        self._full_initial_margin = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.timestamp = timestamp
        self.risk_time_period_id = risk_time_period_id
        self.initial_margin = initial_margin
        self.maintenance_margin = maintenance_margin
        if auto_liq_level is not None:
            self.auto_liq_level = auto_liq_level
        if liq_only_level is not None:
            self.liq_only_level = liq_only_level
        self.total_used_margin = total_used_margin
        self.full_initial_margin = full_initial_margin

    @property
    def id(self):
        """Gets the id of this MarginSnapshot.  # noqa: E501


        :return: The id of this MarginSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarginSnapshot.


        :param id: The id of this MarginSnapshot.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this MarginSnapshot.  # noqa: E501


        :return: The timestamp of this MarginSnapshot.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MarginSnapshot.


        :param timestamp: The timestamp of this MarginSnapshot.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def risk_time_period_id(self):
        """Gets the risk_time_period_id of this MarginSnapshot.  # noqa: E501


        :return: The risk_time_period_id of this MarginSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._risk_time_period_id

    @risk_time_period_id.setter
    def risk_time_period_id(self, risk_time_period_id):
        """Sets the risk_time_period_id of this MarginSnapshot.


        :param risk_time_period_id: The risk_time_period_id of this MarginSnapshot.  # noqa: E501
        :type: int
        """
        if risk_time_period_id is None:
            raise ValueError("Invalid value for `risk_time_period_id`, must not be `None`")  # noqa: E501

        self._risk_time_period_id = risk_time_period_id

    @property
    def initial_margin(self):
        """Gets the initial_margin of this MarginSnapshot.  # noqa: E501


        :return: The initial_margin of this MarginSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._initial_margin

    @initial_margin.setter
    def initial_margin(self, initial_margin):
        """Sets the initial_margin of this MarginSnapshot.


        :param initial_margin: The initial_margin of this MarginSnapshot.  # noqa: E501
        :type: float
        """
        if initial_margin is None:
            raise ValueError("Invalid value for `initial_margin`, must not be `None`")  # noqa: E501

        self._initial_margin = initial_margin

    @property
    def maintenance_margin(self):
        """Gets the maintenance_margin of this MarginSnapshot.  # noqa: E501


        :return: The maintenance_margin of this MarginSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._maintenance_margin

    @maintenance_margin.setter
    def maintenance_margin(self, maintenance_margin):
        """Sets the maintenance_margin of this MarginSnapshot.


        :param maintenance_margin: The maintenance_margin of this MarginSnapshot.  # noqa: E501
        :type: float
        """
        if maintenance_margin is None:
            raise ValueError("Invalid value for `maintenance_margin`, must not be `None`")  # noqa: E501

        self._maintenance_margin = maintenance_margin

    @property
    def auto_liq_level(self):
        """Gets the auto_liq_level of this MarginSnapshot.  # noqa: E501


        :return: The auto_liq_level of this MarginSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._auto_liq_level

    @auto_liq_level.setter
    def auto_liq_level(self, auto_liq_level):
        """Sets the auto_liq_level of this MarginSnapshot.


        :param auto_liq_level: The auto_liq_level of this MarginSnapshot.  # noqa: E501
        :type: float
        """

        self._auto_liq_level = auto_liq_level

    @property
    def liq_only_level(self):
        """Gets the liq_only_level of this MarginSnapshot.  # noqa: E501


        :return: The liq_only_level of this MarginSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._liq_only_level

    @liq_only_level.setter
    def liq_only_level(self, liq_only_level):
        """Sets the liq_only_level of this MarginSnapshot.


        :param liq_only_level: The liq_only_level of this MarginSnapshot.  # noqa: E501
        :type: float
        """

        self._liq_only_level = liq_only_level

    @property
    def total_used_margin(self):
        """Gets the total_used_margin of this MarginSnapshot.  # noqa: E501


        :return: The total_used_margin of this MarginSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._total_used_margin

    @total_used_margin.setter
    def total_used_margin(self, total_used_margin):
        """Sets the total_used_margin of this MarginSnapshot.


        :param total_used_margin: The total_used_margin of this MarginSnapshot.  # noqa: E501
        :type: float
        """
        if total_used_margin is None:
            raise ValueError("Invalid value for `total_used_margin`, must not be `None`")  # noqa: E501

        self._total_used_margin = total_used_margin

    @property
    def full_initial_margin(self):
        """Gets the full_initial_margin of this MarginSnapshot.  # noqa: E501


        :return: The full_initial_margin of this MarginSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._full_initial_margin

    @full_initial_margin.setter
    def full_initial_margin(self, full_initial_margin):
        """Sets the full_initial_margin of this MarginSnapshot.


        :param full_initial_margin: The full_initial_margin of this MarginSnapshot.  # noqa: E501
        :type: float
        """
        if full_initial_margin is None:
            raise ValueError("Invalid value for `full_initial_margin`, must not be `None`")  # noqa: E501

        self._full_initial_margin = full_initial_margin

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
        if issubclass(MarginSnapshot, dict):
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
        if not isinstance(other, MarginSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
