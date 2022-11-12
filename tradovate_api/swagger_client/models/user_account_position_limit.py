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

class UserAccountPositionLimit(object):
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
        'contract_id': 'int',
        'product_id': 'int',
        'exchange_id': 'int',
        'product_type': 'str',
        'risk_discount_contract_group_id': 'int',
        'product_verification_status': 'str',
        'contract_group_id': 'int',
        'active': 'bool',
        'risk_time_period_id': 'int',
        'total_by': 'str',
        'short_limit': 'int',
        'long_limit': 'int',
        'exposed_limit': 'int',
        'description': 'str',
        'account_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'contract_id': 'contractId',
        'product_id': 'productId',
        'exchange_id': 'exchangeId',
        'product_type': 'productType',
        'risk_discount_contract_group_id': 'riskDiscountContractGroupId',
        'product_verification_status': 'productVerificationStatus',
        'contract_group_id': 'contractGroupId',
        'active': 'active',
        'risk_time_period_id': 'riskTimePeriodId',
        'total_by': 'totalBy',
        'short_limit': 'shortLimit',
        'long_limit': 'longLimit',
        'exposed_limit': 'exposedLimit',
        'description': 'description',
        'account_id': 'accountId'
    }

    def __init__(self, id=None, contract_id=None, product_id=None, exchange_id=None, product_type=None, risk_discount_contract_group_id=None, product_verification_status=None, contract_group_id=None, active=None, risk_time_period_id=None, total_by=None, short_limit=None, long_limit=None, exposed_limit=None, description=None, account_id=None):  # noqa: E501
        """UserAccountPositionLimit - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._contract_id = None
        self._product_id = None
        self._exchange_id = None
        self._product_type = None
        self._risk_discount_contract_group_id = None
        self._product_verification_status = None
        self._contract_group_id = None
        self._active = None
        self._risk_time_period_id = None
        self._total_by = None
        self._short_limit = None
        self._long_limit = None
        self._exposed_limit = None
        self._description = None
        self._account_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if contract_id is not None:
            self.contract_id = contract_id
        if product_id is not None:
            self.product_id = product_id
        if exchange_id is not None:
            self.exchange_id = exchange_id
        if product_type is not None:
            self.product_type = product_type
        if risk_discount_contract_group_id is not None:
            self.risk_discount_contract_group_id = risk_discount_contract_group_id
        if product_verification_status is not None:
            self.product_verification_status = product_verification_status
        if contract_group_id is not None:
            self.contract_group_id = contract_group_id
        self.active = active
        if risk_time_period_id is not None:
            self.risk_time_period_id = risk_time_period_id
        self.total_by = total_by
        if short_limit is not None:
            self.short_limit = short_limit
        if long_limit is not None:
            self.long_limit = long_limit
        if exposed_limit is not None:
            self.exposed_limit = exposed_limit
        if description is not None:
            self.description = description
        self.account_id = account_id

    @property
    def id(self):
        """Gets the id of this UserAccountPositionLimit.  # noqa: E501


        :return: The id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAccountPositionLimit.


        :param id: The id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def contract_id(self):
        """Gets the contract_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The contract_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this UserAccountPositionLimit.


        :param contract_id: The contract_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._contract_id = contract_id

    @property
    def product_id(self):
        """Gets the product_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The product_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this UserAccountPositionLimit.


        :param product_id: The product_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def exchange_id(self):
        """Gets the exchange_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The exchange_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this UserAccountPositionLimit.


        :param exchange_id: The exchange_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._exchange_id = exchange_id

    @property
    def product_type(self):
        """Gets the product_type of this UserAccountPositionLimit.  # noqa: E501

        CommonStock, Continuous, Cryptocurrency, Futures, MarketInternals, Options, Spread  # noqa: E501

        :return: The product_type of this UserAccountPositionLimit.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this UserAccountPositionLimit.

        CommonStock, Continuous, Cryptocurrency, Futures, MarketInternals, Options, Spread  # noqa: E501

        :param product_type: The product_type of this UserAccountPositionLimit.  # noqa: E501
        :type: str
        """
        allowed_values = ["CommonStock", "Continuous", "Cryptocurrency", "Futures", "MarketInternals", "Options", "Spread"]  # noqa: E501
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}"  # noqa: E501
                .format(product_type, allowed_values)
            )

        self._product_type = product_type

    @property
    def risk_discount_contract_group_id(self):
        """Gets the risk_discount_contract_group_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The risk_discount_contract_group_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._risk_discount_contract_group_id

    @risk_discount_contract_group_id.setter
    def risk_discount_contract_group_id(self, risk_discount_contract_group_id):
        """Sets the risk_discount_contract_group_id of this UserAccountPositionLimit.


        :param risk_discount_contract_group_id: The risk_discount_contract_group_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._risk_discount_contract_group_id = risk_discount_contract_group_id

    @property
    def product_verification_status(self):
        """Gets the product_verification_status of this UserAccountPositionLimit.  # noqa: E501

        Inactive, Locked, ReadyForContracts, ReadyToTrade, Verified  # noqa: E501

        :return: The product_verification_status of this UserAccountPositionLimit.  # noqa: E501
        :rtype: str
        """
        return self._product_verification_status

    @product_verification_status.setter
    def product_verification_status(self, product_verification_status):
        """Sets the product_verification_status of this UserAccountPositionLimit.

        Inactive, Locked, ReadyForContracts, ReadyToTrade, Verified  # noqa: E501

        :param product_verification_status: The product_verification_status of this UserAccountPositionLimit.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inactive", "Locked", "ReadyForContracts", "ReadyToTrade", "Verified"]  # noqa: E501
        if product_verification_status not in allowed_values:
            raise ValueError(
                "Invalid value for `product_verification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(product_verification_status, allowed_values)
            )

        self._product_verification_status = product_verification_status

    @property
    def contract_group_id(self):
        """Gets the contract_group_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The contract_group_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._contract_group_id

    @contract_group_id.setter
    def contract_group_id(self, contract_group_id):
        """Sets the contract_group_id of this UserAccountPositionLimit.


        :param contract_group_id: The contract_group_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._contract_group_id = contract_group_id

    @property
    def active(self):
        """Gets the active of this UserAccountPositionLimit.  # noqa: E501


        :return: The active of this UserAccountPositionLimit.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserAccountPositionLimit.


        :param active: The active of this UserAccountPositionLimit.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def risk_time_period_id(self):
        """Gets the risk_time_period_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The risk_time_period_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._risk_time_period_id

    @risk_time_period_id.setter
    def risk_time_period_id(self, risk_time_period_id):
        """Sets the risk_time_period_id of this UserAccountPositionLimit.


        :param risk_time_period_id: The risk_time_period_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._risk_time_period_id = risk_time_period_id

    @property
    def total_by(self):
        """Gets the total_by of this UserAccountPositionLimit.  # noqa: E501

        Contract, ContractGroup, DiscountGroup, Exchange, Overall, Product, ProductType  # noqa: E501

        :return: The total_by of this UserAccountPositionLimit.  # noqa: E501
        :rtype: str
        """
        return self._total_by

    @total_by.setter
    def total_by(self, total_by):
        """Sets the total_by of this UserAccountPositionLimit.

        Contract, ContractGroup, DiscountGroup, Exchange, Overall, Product, ProductType  # noqa: E501

        :param total_by: The total_by of this UserAccountPositionLimit.  # noqa: E501
        :type: str
        """
        if total_by is None:
            raise ValueError("Invalid value for `total_by`, must not be `None`")  # noqa: E501
        allowed_values = ["Contract", "ContractGroup", "DiscountGroup", "Exchange", "Overall", "Product", "ProductType"]  # noqa: E501
        if total_by not in allowed_values:
            raise ValueError(
                "Invalid value for `total_by` ({0}), must be one of {1}"  # noqa: E501
                .format(total_by, allowed_values)
            )

        self._total_by = total_by

    @property
    def short_limit(self):
        """Gets the short_limit of this UserAccountPositionLimit.  # noqa: E501


        :return: The short_limit of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._short_limit

    @short_limit.setter
    def short_limit(self, short_limit):
        """Sets the short_limit of this UserAccountPositionLimit.


        :param short_limit: The short_limit of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._short_limit = short_limit

    @property
    def long_limit(self):
        """Gets the long_limit of this UserAccountPositionLimit.  # noqa: E501


        :return: The long_limit of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._long_limit

    @long_limit.setter
    def long_limit(self, long_limit):
        """Sets the long_limit of this UserAccountPositionLimit.


        :param long_limit: The long_limit of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._long_limit = long_limit

    @property
    def exposed_limit(self):
        """Gets the exposed_limit of this UserAccountPositionLimit.  # noqa: E501


        :return: The exposed_limit of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._exposed_limit

    @exposed_limit.setter
    def exposed_limit(self, exposed_limit):
        """Sets the exposed_limit of this UserAccountPositionLimit.


        :param exposed_limit: The exposed_limit of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """

        self._exposed_limit = exposed_limit

    @property
    def description(self):
        """Gets the description of this UserAccountPositionLimit.  # noqa: E501


        :return: The description of this UserAccountPositionLimit.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserAccountPositionLimit.


        :param description: The description of this UserAccountPositionLimit.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def account_id(self):
        """Gets the account_id of this UserAccountPositionLimit.  # noqa: E501


        :return: The account_id of this UserAccountPositionLimit.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UserAccountPositionLimit.


        :param account_id: The account_id of this UserAccountPositionLimit.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

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
        if issubclass(UserAccountPositionLimit, dict):
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
        if not isinstance(other, UserAccountPositionLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
