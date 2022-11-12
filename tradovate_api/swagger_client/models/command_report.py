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

class CommandReport(object):
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
        'command_id': 'int',
        'timestamp': 'datetime',
        'command_status': 'str',
        'reject_reason': 'str',
        'text': 'str',
        'ord_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'command_id': 'commandId',
        'timestamp': 'timestamp',
        'command_status': 'commandStatus',
        'reject_reason': 'rejectReason',
        'text': 'text',
        'ord_status': 'ordStatus'
    }

    def __init__(self, id=None, command_id=None, timestamp=None, command_status=None, reject_reason=None, text=None, ord_status=None):  # noqa: E501
        """CommandReport - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._command_id = None
        self._timestamp = None
        self._command_status = None
        self._reject_reason = None
        self._text = None
        self._ord_status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.command_id = command_id
        self.timestamp = timestamp
        self.command_status = command_status
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if text is not None:
            self.text = text
        if ord_status is not None:
            self.ord_status = ord_status

    @property
    def id(self):
        """Gets the id of this CommandReport.  # noqa: E501


        :return: The id of this CommandReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommandReport.


        :param id: The id of this CommandReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def command_id(self):
        """Gets the command_id of this CommandReport.  # noqa: E501


        :return: The command_id of this CommandReport.  # noqa: E501
        :rtype: int
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this CommandReport.


        :param command_id: The command_id of this CommandReport.  # noqa: E501
        :type: int
        """
        if command_id is None:
            raise ValueError("Invalid value for `command_id`, must not be `None`")  # noqa: E501

        self._command_id = command_id

    @property
    def timestamp(self):
        """Gets the timestamp of this CommandReport.  # noqa: E501


        :return: The timestamp of this CommandReport.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CommandReport.


        :param timestamp: The timestamp of this CommandReport.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def command_status(self):
        """Gets the command_status of this CommandReport.  # noqa: E501

        AtExecution, ExecutionRejected, ExecutionStopped, ExecutionSuspended, OnHold, Pending, PendingExecution, Replaced, RiskPassed, RiskRejected  # noqa: E501

        :return: The command_status of this CommandReport.  # noqa: E501
        :rtype: str
        """
        return self._command_status

    @command_status.setter
    def command_status(self, command_status):
        """Sets the command_status of this CommandReport.

        AtExecution, ExecutionRejected, ExecutionStopped, ExecutionSuspended, OnHold, Pending, PendingExecution, Replaced, RiskPassed, RiskRejected  # noqa: E501

        :param command_status: The command_status of this CommandReport.  # noqa: E501
        :type: str
        """
        if command_status is None:
            raise ValueError("Invalid value for `command_status`, must not be `None`")  # noqa: E501
        allowed_values = ["AtExecution", "ExecutionRejected", "ExecutionStopped", "ExecutionSuspended", "OnHold", "Pending", "PendingExecution", "Replaced", "RiskPassed", "RiskRejected"]  # noqa: E501
        if command_status not in allowed_values:
            raise ValueError(
                "Invalid value for `command_status` ({0}), must be one of {1}"  # noqa: E501
                .format(command_status, allowed_values)
            )

        self._command_status = command_status

    @property
    def reject_reason(self):
        """Gets the reject_reason of this CommandReport.  # noqa: E501

        AccountClosed, AdvancedTrailingStopUnsupported, AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable, InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified, MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached, MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected, RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized, UnknownReason, Unsupported  # noqa: E501

        :return: The reject_reason of this CommandReport.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this CommandReport.

        AccountClosed, AdvancedTrailingStopUnsupported, AnotherCommandPending, BackMonthProhibited, ExecutionProviderNotConfigured, ExecutionProviderUnavailable, InvalidContract, InvalidPrice, LiquidationOnly, LiquidationOnlyBeforeExpiration, MaxOrderQtyIsNotSpecified, MaxOrderQtyLimitReached, MaxPosLimitMisconfigured, MaxPosLimitReached, MaxTotalPosLimitReached, MultipleAccountPlanRequired, NoQuote, NotEnoughLiquidity, OtherExecutionRelated, ParentRejected, RiskCheckTimeout, SessionClosed, Success, TooLate, TradingLocked, TrailingStopNonOrderQtyModify, Unauthorized, UnknownReason, Unsupported  # noqa: E501

        :param reject_reason: The reject_reason of this CommandReport.  # noqa: E501
        :type: str
        """
        allowed_values = ["AccountClosed", "AdvancedTrailingStopUnsupported", "AnotherCommandPending", "BackMonthProhibited", "ExecutionProviderNotConfigured", "ExecutionProviderUnavailable", "InvalidContract", "InvalidPrice", "LiquidationOnly", "LiquidationOnlyBeforeExpiration", "MaxOrderQtyIsNotSpecified", "MaxOrderQtyLimitReached", "MaxPosLimitMisconfigured", "MaxPosLimitReached", "MaxTotalPosLimitReached", "MultipleAccountPlanRequired", "NoQuote", "NotEnoughLiquidity", "OtherExecutionRelated", "ParentRejected", "RiskCheckTimeout", "SessionClosed", "Success", "TooLate", "TradingLocked", "TrailingStopNonOrderQtyModify", "Unauthorized", "UnknownReason", "Unsupported"]  # noqa: E501
        if reject_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reject_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reject_reason, allowed_values)
            )

        self._reject_reason = reject_reason

    @property
    def text(self):
        """Gets the text of this CommandReport.  # noqa: E501


        :return: The text of this CommandReport.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CommandReport.


        :param text: The text of this CommandReport.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def ord_status(self):
        """Gets the ord_status of this CommandReport.  # noqa: E501

        Canceled, Completed, Expired, Filled, PendingCancel, PendingNew, PendingReplace, Rejected, Suspended, Unknown, Working  # noqa: E501

        :return: The ord_status of this CommandReport.  # noqa: E501
        :rtype: str
        """
        return self._ord_status

    @ord_status.setter
    def ord_status(self, ord_status):
        """Sets the ord_status of this CommandReport.

        Canceled, Completed, Expired, Filled, PendingCancel, PendingNew, PendingReplace, Rejected, Suspended, Unknown, Working  # noqa: E501

        :param ord_status: The ord_status of this CommandReport.  # noqa: E501
        :type: str
        """
        allowed_values = ["Canceled", "Completed", "Expired", "Filled", "PendingCancel", "PendingNew", "PendingReplace", "Rejected", "Suspended", "Unknown", "Working"]  # noqa: E501
        if ord_status not in allowed_values:
            raise ValueError(
                "Invalid value for `ord_status` ({0}), must be one of {1}"  # noqa: E501
                .format(ord_status, allowed_values)
            )

        self._ord_status = ord_status

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
        if issubclass(CommandReport, dict):
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
        if not isinstance(other, CommandReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
