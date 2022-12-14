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

class TradovateSubscription(object):
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
        'plan_price': 'float',
        'credit_card_transaction_id': 'int',
        'cash_balance_log_id': 'int',
        'credit_card_id': 'int',
        'account_id': 'int',
        'tradovate_subscription_plan_id': 'int',
        'start_date': 'TradeDate',
        'expiration_date': 'TradeDate',
        'paid_amount': 'float',
        'cancelled_renewal': 'bool',
        'cancel_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'timestamp': 'timestamp',
        'plan_price': 'planPrice',
        'credit_card_transaction_id': 'creditCardTransactionId',
        'cash_balance_log_id': 'cashBalanceLogId',
        'credit_card_id': 'creditCardId',
        'account_id': 'accountId',
        'tradovate_subscription_plan_id': 'tradovateSubscriptionPlanId',
        'start_date': 'startDate',
        'expiration_date': 'expirationDate',
        'paid_amount': 'paidAmount',
        'cancelled_renewal': 'cancelledRenewal',
        'cancel_reason': 'cancelReason'
    }

    def __init__(self, id=None, user_id=None, timestamp=None, plan_price=None, credit_card_transaction_id=None, cash_balance_log_id=None, credit_card_id=None, account_id=None, tradovate_subscription_plan_id=None, start_date=None, expiration_date=None, paid_amount=None, cancelled_renewal=None, cancel_reason=None):  # noqa: E501
        """TradovateSubscription - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._timestamp = None
        self._plan_price = None
        self._credit_card_transaction_id = None
        self._cash_balance_log_id = None
        self._credit_card_id = None
        self._account_id = None
        self._tradovate_subscription_plan_id = None
        self._start_date = None
        self._expiration_date = None
        self._paid_amount = None
        self._cancelled_renewal = None
        self._cancel_reason = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.user_id = user_id
        self.timestamp = timestamp
        self.plan_price = plan_price
        if credit_card_transaction_id is not None:
            self.credit_card_transaction_id = credit_card_transaction_id
        if cash_balance_log_id is not None:
            self.cash_balance_log_id = cash_balance_log_id
        if credit_card_id is not None:
            self.credit_card_id = credit_card_id
        if account_id is not None:
            self.account_id = account_id
        self.tradovate_subscription_plan_id = tradovate_subscription_plan_id
        self.start_date = start_date
        self.expiration_date = expiration_date
        self.paid_amount = paid_amount
        if cancelled_renewal is not None:
            self.cancelled_renewal = cancelled_renewal
        if cancel_reason is not None:
            self.cancel_reason = cancel_reason

    @property
    def id(self):
        """Gets the id of this TradovateSubscription.  # noqa: E501


        :return: The id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TradovateSubscription.


        :param id: The id of this TradovateSubscription.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this TradovateSubscription.  # noqa: E501


        :return: The user_id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TradovateSubscription.


        :param user_id: The user_id of this TradovateSubscription.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def timestamp(self):
        """Gets the timestamp of this TradovateSubscription.  # noqa: E501


        :return: The timestamp of this TradovateSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TradovateSubscription.


        :param timestamp: The timestamp of this TradovateSubscription.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def plan_price(self):
        """Gets the plan_price of this TradovateSubscription.  # noqa: E501


        :return: The plan_price of this TradovateSubscription.  # noqa: E501
        :rtype: float
        """
        return self._plan_price

    @plan_price.setter
    def plan_price(self, plan_price):
        """Sets the plan_price of this TradovateSubscription.


        :param plan_price: The plan_price of this TradovateSubscription.  # noqa: E501
        :type: float
        """
        if plan_price is None:
            raise ValueError("Invalid value for `plan_price`, must not be `None`")  # noqa: E501

        self._plan_price = plan_price

    @property
    def credit_card_transaction_id(self):
        """Gets the credit_card_transaction_id of this TradovateSubscription.  # noqa: E501


        :return: The credit_card_transaction_id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_transaction_id

    @credit_card_transaction_id.setter
    def credit_card_transaction_id(self, credit_card_transaction_id):
        """Sets the credit_card_transaction_id of this TradovateSubscription.


        :param credit_card_transaction_id: The credit_card_transaction_id of this TradovateSubscription.  # noqa: E501
        :type: int
        """

        self._credit_card_transaction_id = credit_card_transaction_id

    @property
    def cash_balance_log_id(self):
        """Gets the cash_balance_log_id of this TradovateSubscription.  # noqa: E501


        :return: The cash_balance_log_id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._cash_balance_log_id

    @cash_balance_log_id.setter
    def cash_balance_log_id(self, cash_balance_log_id):
        """Sets the cash_balance_log_id of this TradovateSubscription.


        :param cash_balance_log_id: The cash_balance_log_id of this TradovateSubscription.  # noqa: E501
        :type: int
        """

        self._cash_balance_log_id = cash_balance_log_id

    @property
    def credit_card_id(self):
        """Gets the credit_card_id of this TradovateSubscription.  # noqa: E501


        :return: The credit_card_id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_id

    @credit_card_id.setter
    def credit_card_id(self, credit_card_id):
        """Sets the credit_card_id of this TradovateSubscription.


        :param credit_card_id: The credit_card_id of this TradovateSubscription.  # noqa: E501
        :type: int
        """

        self._credit_card_id = credit_card_id

    @property
    def account_id(self):
        """Gets the account_id of this TradovateSubscription.  # noqa: E501


        :return: The account_id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TradovateSubscription.


        :param account_id: The account_id of this TradovateSubscription.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def tradovate_subscription_plan_id(self):
        """Gets the tradovate_subscription_plan_id of this TradovateSubscription.  # noqa: E501


        :return: The tradovate_subscription_plan_id of this TradovateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._tradovate_subscription_plan_id

    @tradovate_subscription_plan_id.setter
    def tradovate_subscription_plan_id(self, tradovate_subscription_plan_id):
        """Sets the tradovate_subscription_plan_id of this TradovateSubscription.


        :param tradovate_subscription_plan_id: The tradovate_subscription_plan_id of this TradovateSubscription.  # noqa: E501
        :type: int
        """
        if tradovate_subscription_plan_id is None:
            raise ValueError("Invalid value for `tradovate_subscription_plan_id`, must not be `None`")  # noqa: E501

        self._tradovate_subscription_plan_id = tradovate_subscription_plan_id

    @property
    def start_date(self):
        """Gets the start_date of this TradovateSubscription.  # noqa: E501


        :return: The start_date of this TradovateSubscription.  # noqa: E501
        :rtype: TradeDate
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TradovateSubscription.


        :param start_date: The start_date of this TradovateSubscription.  # noqa: E501
        :type: TradeDate
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this TradovateSubscription.  # noqa: E501


        :return: The expiration_date of this TradovateSubscription.  # noqa: E501
        :rtype: TradeDate
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this TradovateSubscription.


        :param expiration_date: The expiration_date of this TradovateSubscription.  # noqa: E501
        :type: TradeDate
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def paid_amount(self):
        """Gets the paid_amount of this TradovateSubscription.  # noqa: E501


        :return: The paid_amount of this TradovateSubscription.  # noqa: E501
        :rtype: float
        """
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        """Sets the paid_amount of this TradovateSubscription.


        :param paid_amount: The paid_amount of this TradovateSubscription.  # noqa: E501
        :type: float
        """
        if paid_amount is None:
            raise ValueError("Invalid value for `paid_amount`, must not be `None`")  # noqa: E501

        self._paid_amount = paid_amount

    @property
    def cancelled_renewal(self):
        """Gets the cancelled_renewal of this TradovateSubscription.  # noqa: E501


        :return: The cancelled_renewal of this TradovateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._cancelled_renewal

    @cancelled_renewal.setter
    def cancelled_renewal(self, cancelled_renewal):
        """Sets the cancelled_renewal of this TradovateSubscription.


        :param cancelled_renewal: The cancelled_renewal of this TradovateSubscription.  # noqa: E501
        :type: bool
        """

        self._cancelled_renewal = cancelled_renewal

    @property
    def cancel_reason(self):
        """Gets the cancel_reason of this TradovateSubscription.  # noqa: E501


        :return: The cancel_reason of this TradovateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, cancel_reason):
        """Sets the cancel_reason of this TradovateSubscription.


        :param cancel_reason: The cancel_reason of this TradovateSubscription.  # noqa: E501
        :type: str
        """

        self._cancel_reason = cancel_reason

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
        if issubclass(TradovateSubscription, dict):
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
        if not isinstance(other, TradovateSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
