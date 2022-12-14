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

class AccountRiskStatus(object):
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
        'admin_action': 'str',
        'admin_timestamp': 'datetime',
        'liquidate_only': 'datetime',
        'user_triggered_liq_only': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'admin_action': 'adminAction',
        'admin_timestamp': 'adminTimestamp',
        'liquidate_only': 'liquidateOnly',
        'user_triggered_liq_only': 'userTriggeredLiqOnly'
    }

    def __init__(self, id=None, admin_action=None, admin_timestamp=None, liquidate_only=None, user_triggered_liq_only=None):  # noqa: E501
        """AccountRiskStatus - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._admin_action = None
        self._admin_timestamp = None
        self._liquidate_only = None
        self._user_triggered_liq_only = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if admin_action is not None:
            self.admin_action = admin_action
        if admin_timestamp is not None:
            self.admin_timestamp = admin_timestamp
        if liquidate_only is not None:
            self.liquidate_only = liquidate_only
        if user_triggered_liq_only is not None:
            self.user_triggered_liq_only = user_triggered_liq_only

    @property
    def id(self):
        """Gets the id of this AccountRiskStatus.  # noqa: E501


        :return: The id of this AccountRiskStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountRiskStatus.


        :param id: The id of this AccountRiskStatus.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def admin_action(self):
        """Gets the admin_action of this AccountRiskStatus.  # noqa: E501

        AgreedOnLiqOnlyModeByAutoLiq, AgreedOnLiquidationByAutoLiq, DisableAutoLiq, LiquidateImmediately, LiquidateOnlyModeImmediately, LockTradingImmediately, Normal, PlaceAutoLiqOnHold  # noqa: E501

        :return: The admin_action of this AccountRiskStatus.  # noqa: E501
        :rtype: str
        """
        return self._admin_action

    @admin_action.setter
    def admin_action(self, admin_action):
        """Sets the admin_action of this AccountRiskStatus.

        AgreedOnLiqOnlyModeByAutoLiq, AgreedOnLiquidationByAutoLiq, DisableAutoLiq, LiquidateImmediately, LiquidateOnlyModeImmediately, LockTradingImmediately, Normal, PlaceAutoLiqOnHold  # noqa: E501

        :param admin_action: The admin_action of this AccountRiskStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["AgreedOnLiqOnlyModeByAutoLiq", "AgreedOnLiquidationByAutoLiq", "DisableAutoLiq", "LiquidateImmediately", "LiquidateOnlyModeImmediately", "LockTradingImmediately", "Normal", "PlaceAutoLiqOnHold"]  # noqa: E501
        if admin_action not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_action` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_action, allowed_values)
            )

        self._admin_action = admin_action

    @property
    def admin_timestamp(self):
        """Gets the admin_timestamp of this AccountRiskStatus.  # noqa: E501


        :return: The admin_timestamp of this AccountRiskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._admin_timestamp

    @admin_timestamp.setter
    def admin_timestamp(self, admin_timestamp):
        """Sets the admin_timestamp of this AccountRiskStatus.


        :param admin_timestamp: The admin_timestamp of this AccountRiskStatus.  # noqa: E501
        :type: datetime
        """

        self._admin_timestamp = admin_timestamp

    @property
    def liquidate_only(self):
        """Gets the liquidate_only of this AccountRiskStatus.  # noqa: E501


        :return: The liquidate_only of this AccountRiskStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._liquidate_only

    @liquidate_only.setter
    def liquidate_only(self, liquidate_only):
        """Sets the liquidate_only of this AccountRiskStatus.


        :param liquidate_only: The liquidate_only of this AccountRiskStatus.  # noqa: E501
        :type: datetime
        """

        self._liquidate_only = liquidate_only

    @property
    def user_triggered_liq_only(self):
        """Gets the user_triggered_liq_only of this AccountRiskStatus.  # noqa: E501


        :return: The user_triggered_liq_only of this AccountRiskStatus.  # noqa: E501
        :rtype: bool
        """
        return self._user_triggered_liq_only

    @user_triggered_liq_only.setter
    def user_triggered_liq_only(self, user_triggered_liq_only):
        """Sets the user_triggered_liq_only of this AccountRiskStatus.


        :param user_triggered_liq_only: The user_triggered_liq_only of this AccountRiskStatus.  # noqa: E501
        :type: bool
        """

        self._user_triggered_liq_only = user_triggered_liq_only

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
        if issubclass(AccountRiskStatus, dict):
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
        if not isinstance(other, AccountRiskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
