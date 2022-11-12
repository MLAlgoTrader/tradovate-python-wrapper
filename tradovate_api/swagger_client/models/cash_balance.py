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

class CashBalance(object):
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
        'account_id': 'int',
        'timestamp': 'datetime',
        'trade_date': 'TradeDate',
        'currency_id': 'int',
        'amount': 'float',
        'realized_pn_l': 'float',
        'week_realized_pn_l': 'float'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountId',
        'timestamp': 'timestamp',
        'trade_date': 'tradeDate',
        'currency_id': 'currencyId',
        'amount': 'amount',
        'realized_pn_l': 'realizedPnL',
        'week_realized_pn_l': 'weekRealizedPnL'
    }

    def __init__(self, id=None, account_id=None, timestamp=None, trade_date=None, currency_id=None, amount=None, realized_pn_l=None, week_realized_pn_l=None):  # noqa: E501
        """CashBalance - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._timestamp = None
        self._trade_date = None
        self._currency_id = None
        self._amount = None
        self._realized_pn_l = None
        self._week_realized_pn_l = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.account_id = account_id
        self.timestamp = timestamp
        self.trade_date = trade_date
        self.currency_id = currency_id
        self.amount = amount
        if realized_pn_l is not None:
            self.realized_pn_l = realized_pn_l
        if week_realized_pn_l is not None:
            self.week_realized_pn_l = week_realized_pn_l

    @property
    def id(self):
        """Gets the id of this CashBalance.  # noqa: E501


        :return: The id of this CashBalance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CashBalance.


        :param id: The id of this CashBalance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this CashBalance.  # noqa: E501


        :return: The account_id of this CashBalance.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CashBalance.


        :param account_id: The account_id of this CashBalance.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def timestamp(self):
        """Gets the timestamp of this CashBalance.  # noqa: E501


        :return: The timestamp of this CashBalance.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CashBalance.


        :param timestamp: The timestamp of this CashBalance.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def trade_date(self):
        """Gets the trade_date of this CashBalance.  # noqa: E501


        :return: The trade_date of this CashBalance.  # noqa: E501
        :rtype: TradeDate
        """
        return self._trade_date

    @trade_date.setter
    def trade_date(self, trade_date):
        """Sets the trade_date of this CashBalance.


        :param trade_date: The trade_date of this CashBalance.  # noqa: E501
        :type: TradeDate
        """
        if trade_date is None:
            raise ValueError("Invalid value for `trade_date`, must not be `None`")  # noqa: E501

        self._trade_date = trade_date

    @property
    def currency_id(self):
        """Gets the currency_id of this CashBalance.  # noqa: E501


        :return: The currency_id of this CashBalance.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this CashBalance.


        :param currency_id: The currency_id of this CashBalance.  # noqa: E501
        :type: int
        """
        if currency_id is None:
            raise ValueError("Invalid value for `currency_id`, must not be `None`")  # noqa: E501

        self._currency_id = currency_id

    @property
    def amount(self):
        """Gets the amount of this CashBalance.  # noqa: E501


        :return: The amount of this CashBalance.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashBalance.


        :param amount: The amount of this CashBalance.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def realized_pn_l(self):
        """Gets the realized_pn_l of this CashBalance.  # noqa: E501


        :return: The realized_pn_l of this CashBalance.  # noqa: E501
        :rtype: float
        """
        return self._realized_pn_l

    @realized_pn_l.setter
    def realized_pn_l(self, realized_pn_l):
        """Sets the realized_pn_l of this CashBalance.


        :param realized_pn_l: The realized_pn_l of this CashBalance.  # noqa: E501
        :type: float
        """

        self._realized_pn_l = realized_pn_l

    @property
    def week_realized_pn_l(self):
        """Gets the week_realized_pn_l of this CashBalance.  # noqa: E501


        :return: The week_realized_pn_l of this CashBalance.  # noqa: E501
        :rtype: float
        """
        return self._week_realized_pn_l

    @week_realized_pn_l.setter
    def week_realized_pn_l(self, week_realized_pn_l):
        """Sets the week_realized_pn_l of this CashBalance.


        :param week_realized_pn_l: The week_realized_pn_l of this CashBalance.  # noqa: E501
        :type: float
        """

        self._week_realized_pn_l = week_realized_pn_l

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
        if issubclass(CashBalance, dict):
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
        if not isinstance(other, CashBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
