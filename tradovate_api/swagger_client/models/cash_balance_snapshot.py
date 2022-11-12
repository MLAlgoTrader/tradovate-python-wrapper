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

class CashBalanceSnapshot(object):
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
        'total_cash_value': 'float',
        'total_pn_l': 'float',
        'initial_margin': 'float',
        'maintenance_margin': 'float',
        'net_liq': 'float',
        'open_pn_l': 'float',
        'realized_pn_l': 'float',
        'week_realized_pn_l': 'float'
    }

    attribute_map = {
        'error_text': 'errorText',
        'total_cash_value': 'totalCashValue',
        'total_pn_l': 'totalPnL',
        'initial_margin': 'initialMargin',
        'maintenance_margin': 'maintenanceMargin',
        'net_liq': 'netLiq',
        'open_pn_l': 'openPnL',
        'realized_pn_l': 'realizedPnL',
        'week_realized_pn_l': 'weekRealizedPnL'
    }

    def __init__(self, error_text=None, total_cash_value=None, total_pn_l=None, initial_margin=None, maintenance_margin=None, net_liq=None, open_pn_l=None, realized_pn_l=None, week_realized_pn_l=None):  # noqa: E501
        """CashBalanceSnapshot - a model defined in Swagger"""  # noqa: E501
        self._error_text = None
        self._total_cash_value = None
        self._total_pn_l = None
        self._initial_margin = None
        self._maintenance_margin = None
        self._net_liq = None
        self._open_pn_l = None
        self._realized_pn_l = None
        self._week_realized_pn_l = None
        self.discriminator = None
        if error_text is not None:
            self.error_text = error_text
        if total_cash_value is not None:
            self.total_cash_value = total_cash_value
        if total_pn_l is not None:
            self.total_pn_l = total_pn_l
        if initial_margin is not None:
            self.initial_margin = initial_margin
        if maintenance_margin is not None:
            self.maintenance_margin = maintenance_margin
        if net_liq is not None:
            self.net_liq = net_liq
        if open_pn_l is not None:
            self.open_pn_l = open_pn_l
        if realized_pn_l is not None:
            self.realized_pn_l = realized_pn_l
        if week_realized_pn_l is not None:
            self.week_realized_pn_l = week_realized_pn_l

    @property
    def error_text(self):
        """Gets the error_text of this CashBalanceSnapshot.  # noqa: E501

        Non-empty if the request failed  # noqa: E501

        :return: The error_text of this CashBalanceSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        """Sets the error_text of this CashBalanceSnapshot.

        Non-empty if the request failed  # noqa: E501

        :param error_text: The error_text of this CashBalanceSnapshot.  # noqa: E501
        :type: str
        """

        self._error_text = error_text

    @property
    def total_cash_value(self):
        """Gets the total_cash_value of this CashBalanceSnapshot.  # noqa: E501


        :return: The total_cash_value of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._total_cash_value

    @total_cash_value.setter
    def total_cash_value(self, total_cash_value):
        """Sets the total_cash_value of this CashBalanceSnapshot.


        :param total_cash_value: The total_cash_value of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._total_cash_value = total_cash_value

    @property
    def total_pn_l(self):
        """Gets the total_pn_l of this CashBalanceSnapshot.  # noqa: E501


        :return: The total_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._total_pn_l

    @total_pn_l.setter
    def total_pn_l(self, total_pn_l):
        """Sets the total_pn_l of this CashBalanceSnapshot.


        :param total_pn_l: The total_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._total_pn_l = total_pn_l

    @property
    def initial_margin(self):
        """Gets the initial_margin of this CashBalanceSnapshot.  # noqa: E501


        :return: The initial_margin of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._initial_margin

    @initial_margin.setter
    def initial_margin(self, initial_margin):
        """Sets the initial_margin of this CashBalanceSnapshot.


        :param initial_margin: The initial_margin of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._initial_margin = initial_margin

    @property
    def maintenance_margin(self):
        """Gets the maintenance_margin of this CashBalanceSnapshot.  # noqa: E501


        :return: The maintenance_margin of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._maintenance_margin

    @maintenance_margin.setter
    def maintenance_margin(self, maintenance_margin):
        """Sets the maintenance_margin of this CashBalanceSnapshot.


        :param maintenance_margin: The maintenance_margin of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._maintenance_margin = maintenance_margin

    @property
    def net_liq(self):
        """Gets the net_liq of this CashBalanceSnapshot.  # noqa: E501


        :return: The net_liq of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._net_liq

    @net_liq.setter
    def net_liq(self, net_liq):
        """Sets the net_liq of this CashBalanceSnapshot.


        :param net_liq: The net_liq of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._net_liq = net_liq

    @property
    def open_pn_l(self):
        """Gets the open_pn_l of this CashBalanceSnapshot.  # noqa: E501


        :return: The open_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._open_pn_l

    @open_pn_l.setter
    def open_pn_l(self, open_pn_l):
        """Sets the open_pn_l of this CashBalanceSnapshot.


        :param open_pn_l: The open_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._open_pn_l = open_pn_l

    @property
    def realized_pn_l(self):
        """Gets the realized_pn_l of this CashBalanceSnapshot.  # noqa: E501


        :return: The realized_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._realized_pn_l

    @realized_pn_l.setter
    def realized_pn_l(self, realized_pn_l):
        """Sets the realized_pn_l of this CashBalanceSnapshot.


        :param realized_pn_l: The realized_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :type: float
        """

        self._realized_pn_l = realized_pn_l

    @property
    def week_realized_pn_l(self):
        """Gets the week_realized_pn_l of this CashBalanceSnapshot.  # noqa: E501


        :return: The week_realized_pn_l of this CashBalanceSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._week_realized_pn_l

    @week_realized_pn_l.setter
    def week_realized_pn_l(self, week_realized_pn_l):
        """Sets the week_realized_pn_l of this CashBalanceSnapshot.


        :param week_realized_pn_l: The week_realized_pn_l of this CashBalanceSnapshot.  # noqa: E501
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
        if issubclass(CashBalanceSnapshot, dict):
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
        if not isinstance(other, CashBalanceSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
