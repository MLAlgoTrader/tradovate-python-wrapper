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

class CashBalanceLog(object):
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
        'week_realized_pn_l': 'float',
        'cash_change_type': 'str',
        'fill_pair_id': 'int',
        'fill_id': 'int',
        'fund_transaction_id': 'int',
        'comment': 'str',
        'delta': 'float',
        'sender_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountId',
        'timestamp': 'timestamp',
        'trade_date': 'tradeDate',
        'currency_id': 'currencyId',
        'amount': 'amount',
        'realized_pn_l': 'realizedPnL',
        'week_realized_pn_l': 'weekRealizedPnL',
        'cash_change_type': 'cashChangeType',
        'fill_pair_id': 'fillPairId',
        'fill_id': 'fillId',
        'fund_transaction_id': 'fundTransactionId',
        'comment': 'comment',
        'delta': 'delta',
        'sender_id': 'senderId'
    }

    def __init__(self, id=None, account_id=None, timestamp=None, trade_date=None, currency_id=None, amount=None, realized_pn_l=None, week_realized_pn_l=None, cash_change_type=None, fill_pair_id=None, fill_id=None, fund_transaction_id=None, comment=None, delta=None, sender_id=None):  # noqa: E501
        """CashBalanceLog - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._timestamp = None
        self._trade_date = None
        self._currency_id = None
        self._amount = None
        self._realized_pn_l = None
        self._week_realized_pn_l = None
        self._cash_change_type = None
        self._fill_pair_id = None
        self._fill_id = None
        self._fund_transaction_id = None
        self._comment = None
        self._delta = None
        self._sender_id = None
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
        self.cash_change_type = cash_change_type
        if fill_pair_id is not None:
            self.fill_pair_id = fill_pair_id
        if fill_id is not None:
            self.fill_id = fill_id
        if fund_transaction_id is not None:
            self.fund_transaction_id = fund_transaction_id
        if comment is not None:
            self.comment = comment
        self.delta = delta
        if sender_id is not None:
            self.sender_id = sender_id

    @property
    def id(self):
        """Gets the id of this CashBalanceLog.  # noqa: E501


        :return: The id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CashBalanceLog.


        :param id: The id of this CashBalanceLog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this CashBalanceLog.  # noqa: E501


        :return: The account_id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CashBalanceLog.


        :param account_id: The account_id of this CashBalanceLog.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def timestamp(self):
        """Gets the timestamp of this CashBalanceLog.  # noqa: E501


        :return: The timestamp of this CashBalanceLog.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CashBalanceLog.


        :param timestamp: The timestamp of this CashBalanceLog.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def trade_date(self):
        """Gets the trade_date of this CashBalanceLog.  # noqa: E501


        :return: The trade_date of this CashBalanceLog.  # noqa: E501
        :rtype: TradeDate
        """
        return self._trade_date

    @trade_date.setter
    def trade_date(self, trade_date):
        """Sets the trade_date of this CashBalanceLog.


        :param trade_date: The trade_date of this CashBalanceLog.  # noqa: E501
        :type: TradeDate
        """
        if trade_date is None:
            raise ValueError("Invalid value for `trade_date`, must not be `None`")  # noqa: E501

        self._trade_date = trade_date

    @property
    def currency_id(self):
        """Gets the currency_id of this CashBalanceLog.  # noqa: E501


        :return: The currency_id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this CashBalanceLog.


        :param currency_id: The currency_id of this CashBalanceLog.  # noqa: E501
        :type: int
        """
        if currency_id is None:
            raise ValueError("Invalid value for `currency_id`, must not be `None`")  # noqa: E501

        self._currency_id = currency_id

    @property
    def amount(self):
        """Gets the amount of this CashBalanceLog.  # noqa: E501


        :return: The amount of this CashBalanceLog.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashBalanceLog.


        :param amount: The amount of this CashBalanceLog.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def realized_pn_l(self):
        """Gets the realized_pn_l of this CashBalanceLog.  # noqa: E501


        :return: The realized_pn_l of this CashBalanceLog.  # noqa: E501
        :rtype: float
        """
        return self._realized_pn_l

    @realized_pn_l.setter
    def realized_pn_l(self, realized_pn_l):
        """Sets the realized_pn_l of this CashBalanceLog.


        :param realized_pn_l: The realized_pn_l of this CashBalanceLog.  # noqa: E501
        :type: float
        """

        self._realized_pn_l = realized_pn_l

    @property
    def week_realized_pn_l(self):
        """Gets the week_realized_pn_l of this CashBalanceLog.  # noqa: E501


        :return: The week_realized_pn_l of this CashBalanceLog.  # noqa: E501
        :rtype: float
        """
        return self._week_realized_pn_l

    @week_realized_pn_l.setter
    def week_realized_pn_l(self, week_realized_pn_l):
        """Sets the week_realized_pn_l of this CashBalanceLog.


        :param week_realized_pn_l: The week_realized_pn_l of this CashBalanceLog.  # noqa: E501
        :type: float
        """

        self._week_realized_pn_l = week_realized_pn_l

    @property
    def cash_change_type(self):
        """Gets the cash_change_type of this CashBalanceLog.  # noqa: E501

        AutomaticReconciliation, BrokerageFee, CancelledPairedTrade, CashSettlement, ClearingFee, Commission, DeskFee, EntitlementSubscription, ExchangeFee, FundTransaction, FundTransactionFee, IPFee, LiquidationFee, ManualAdjustment, MarketDataSubscription, NewSession, NfaFee, OptionsTrade, OrderRoutingFee, TradePaired, TradovateSubscription  # noqa: E501

        :return: The cash_change_type of this CashBalanceLog.  # noqa: E501
        :rtype: str
        """
        return self._cash_change_type

    @cash_change_type.setter
    def cash_change_type(self, cash_change_type):
        """Sets the cash_change_type of this CashBalanceLog.

        AutomaticReconciliation, BrokerageFee, CancelledPairedTrade, CashSettlement, ClearingFee, Commission, DeskFee, EntitlementSubscription, ExchangeFee, FundTransaction, FundTransactionFee, IPFee, LiquidationFee, ManualAdjustment, MarketDataSubscription, NewSession, NfaFee, OptionsTrade, OrderRoutingFee, TradePaired, TradovateSubscription  # noqa: E501

        :param cash_change_type: The cash_change_type of this CashBalanceLog.  # noqa: E501
        :type: str
        """
        if cash_change_type is None:
            raise ValueError("Invalid value for `cash_change_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AutomaticReconciliation", "BrokerageFee", "CancelledPairedTrade", "CashSettlement", "ClearingFee", "Commission", "DeskFee", "EntitlementSubscription", "ExchangeFee", "FundTransaction", "FundTransactionFee", "IPFee", "LiquidationFee", "ManualAdjustment", "MarketDataSubscription", "NewSession", "NfaFee", "OptionsTrade", "OrderRoutingFee", "TradePaired", "TradovateSubscription"]  # noqa: E501
        if cash_change_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cash_change_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cash_change_type, allowed_values)
            )

        self._cash_change_type = cash_change_type

    @property
    def fill_pair_id(self):
        """Gets the fill_pair_id of this CashBalanceLog.  # noqa: E501


        :return: The fill_pair_id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._fill_pair_id

    @fill_pair_id.setter
    def fill_pair_id(self, fill_pair_id):
        """Sets the fill_pair_id of this CashBalanceLog.


        :param fill_pair_id: The fill_pair_id of this CashBalanceLog.  # noqa: E501
        :type: int
        """

        self._fill_pair_id = fill_pair_id

    @property
    def fill_id(self):
        """Gets the fill_id of this CashBalanceLog.  # noqa: E501


        :return: The fill_id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._fill_id

    @fill_id.setter
    def fill_id(self, fill_id):
        """Sets the fill_id of this CashBalanceLog.


        :param fill_id: The fill_id of this CashBalanceLog.  # noqa: E501
        :type: int
        """

        self._fill_id = fill_id

    @property
    def fund_transaction_id(self):
        """Gets the fund_transaction_id of this CashBalanceLog.  # noqa: E501


        :return: The fund_transaction_id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._fund_transaction_id

    @fund_transaction_id.setter
    def fund_transaction_id(self, fund_transaction_id):
        """Sets the fund_transaction_id of this CashBalanceLog.


        :param fund_transaction_id: The fund_transaction_id of this CashBalanceLog.  # noqa: E501
        :type: int
        """

        self._fund_transaction_id = fund_transaction_id

    @property
    def comment(self):
        """Gets the comment of this CashBalanceLog.  # noqa: E501


        :return: The comment of this CashBalanceLog.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CashBalanceLog.


        :param comment: The comment of this CashBalanceLog.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def delta(self):
        """Gets the delta of this CashBalanceLog.  # noqa: E501


        :return: The delta of this CashBalanceLog.  # noqa: E501
        :rtype: float
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this CashBalanceLog.


        :param delta: The delta of this CashBalanceLog.  # noqa: E501
        :type: float
        """
        if delta is None:
            raise ValueError("Invalid value for `delta`, must not be `None`")  # noqa: E501

        self._delta = delta

    @property
    def sender_id(self):
        """Gets the sender_id of this CashBalanceLog.  # noqa: E501


        :return: The sender_id of this CashBalanceLog.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this CashBalanceLog.


        :param sender_id: The sender_id of this CashBalanceLog.  # noqa: E501
        :type: int
        """

        self._sender_id = sender_id

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
        if issubclass(CashBalanceLog, dict):
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
        if not isinstance(other, CashBalanceLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
