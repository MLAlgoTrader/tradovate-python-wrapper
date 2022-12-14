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

class Command(object):
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
        'order_id': 'int',
        'timestamp': 'datetime',
        'cl_ord_id': 'str',
        'command_type': 'str',
        'command_status': 'str',
        'sender_id': 'int',
        'user_session_id': 'int',
        'activation_time': 'datetime',
        'custom_tag50': 'str',
        'is_automated': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'order_id': 'orderId',
        'timestamp': 'timestamp',
        'cl_ord_id': 'clOrdId',
        'command_type': 'commandType',
        'command_status': 'commandStatus',
        'sender_id': 'senderId',
        'user_session_id': 'userSessionId',
        'activation_time': 'activationTime',
        'custom_tag50': 'customTag50',
        'is_automated': 'isAutomated'
    }

    def __init__(self, id=None, order_id=None, timestamp=None, cl_ord_id=None, command_type=None, command_status=None, sender_id=None, user_session_id=None, activation_time=None, custom_tag50=None, is_automated=None):  # noqa: E501
        """Command - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._order_id = None
        self._timestamp = None
        self._cl_ord_id = None
        self._command_type = None
        self._command_status = None
        self._sender_id = None
        self._user_session_id = None
        self._activation_time = None
        self._custom_tag50 = None
        self._is_automated = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.order_id = order_id
        self.timestamp = timestamp
        if cl_ord_id is not None:
            self.cl_ord_id = cl_ord_id
        self.command_type = command_type
        self.command_status = command_status
        if sender_id is not None:
            self.sender_id = sender_id
        if user_session_id is not None:
            self.user_session_id = user_session_id
        if activation_time is not None:
            self.activation_time = activation_time
        if custom_tag50 is not None:
            self.custom_tag50 = custom_tag50
        if is_automated is not None:
            self.is_automated = is_automated

    @property
    def id(self):
        """Gets the id of this Command.  # noqa: E501


        :return: The id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Command.


        :param id: The id of this Command.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def order_id(self):
        """Gets the order_id of this Command.  # noqa: E501


        :return: The order_id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Command.


        :param order_id: The order_id of this Command.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def timestamp(self):
        """Gets the timestamp of this Command.  # noqa: E501


        :return: The timestamp of this Command.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Command.


        :param timestamp: The timestamp of this Command.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def cl_ord_id(self):
        """Gets the cl_ord_id of this Command.  # noqa: E501


        :return: The cl_ord_id of this Command.  # noqa: E501
        :rtype: str
        """
        return self._cl_ord_id

    @cl_ord_id.setter
    def cl_ord_id(self, cl_ord_id):
        """Sets the cl_ord_id of this Command.


        :param cl_ord_id: The cl_ord_id of this Command.  # noqa: E501
        :type: str
        """

        self._cl_ord_id = cl_ord_id

    @property
    def command_type(self):
        """Gets the command_type of this Command.  # noqa: E501

        Cancel, Modify, New  # noqa: E501

        :return: The command_type of this Command.  # noqa: E501
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this Command.

        Cancel, Modify, New  # noqa: E501

        :param command_type: The command_type of this Command.  # noqa: E501
        :type: str
        """
        if command_type is None:
            raise ValueError("Invalid value for `command_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Cancel", "Modify", "New"]  # noqa: E501
        if command_type not in allowed_values:
            raise ValueError(
                "Invalid value for `command_type` ({0}), must be one of {1}"  # noqa: E501
                .format(command_type, allowed_values)
            )

        self._command_type = command_type

    @property
    def command_status(self):
        """Gets the command_status of this Command.  # noqa: E501

        AtExecution, ExecutionRejected, ExecutionStopped, ExecutionSuspended, OnHold, Pending, PendingExecution, Replaced, RiskPassed, RiskRejected  # noqa: E501

        :return: The command_status of this Command.  # noqa: E501
        :rtype: str
        """
        return self._command_status

    @command_status.setter
    def command_status(self, command_status):
        """Sets the command_status of this Command.

        AtExecution, ExecutionRejected, ExecutionStopped, ExecutionSuspended, OnHold, Pending, PendingExecution, Replaced, RiskPassed, RiskRejected  # noqa: E501

        :param command_status: The command_status of this Command.  # noqa: E501
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
    def sender_id(self):
        """Gets the sender_id of this Command.  # noqa: E501


        :return: The sender_id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this Command.


        :param sender_id: The sender_id of this Command.  # noqa: E501
        :type: int
        """

        self._sender_id = sender_id

    @property
    def user_session_id(self):
        """Gets the user_session_id of this Command.  # noqa: E501


        :return: The user_session_id of this Command.  # noqa: E501
        :rtype: int
        """
        return self._user_session_id

    @user_session_id.setter
    def user_session_id(self, user_session_id):
        """Sets the user_session_id of this Command.


        :param user_session_id: The user_session_id of this Command.  # noqa: E501
        :type: int
        """

        self._user_session_id = user_session_id

    @property
    def activation_time(self):
        """Gets the activation_time of this Command.  # noqa: E501


        :return: The activation_time of this Command.  # noqa: E501
        :rtype: datetime
        """
        return self._activation_time

    @activation_time.setter
    def activation_time(self, activation_time):
        """Sets the activation_time of this Command.


        :param activation_time: The activation_time of this Command.  # noqa: E501
        :type: datetime
        """

        self._activation_time = activation_time

    @property
    def custom_tag50(self):
        """Gets the custom_tag50 of this Command.  # noqa: E501


        :return: The custom_tag50 of this Command.  # noqa: E501
        :rtype: str
        """
        return self._custom_tag50

    @custom_tag50.setter
    def custom_tag50(self, custom_tag50):
        """Sets the custom_tag50 of this Command.


        :param custom_tag50: The custom_tag50 of this Command.  # noqa: E501
        :type: str
        """

        self._custom_tag50 = custom_tag50

    @property
    def is_automated(self):
        """Gets the is_automated of this Command.  # noqa: E501


        :return: The is_automated of this Command.  # noqa: E501
        :rtype: bool
        """
        return self._is_automated

    @is_automated.setter
    def is_automated(self, is_automated):
        """Sets the is_automated of this Command.


        :param is_automated: The is_automated of this Command.  # noqa: E501
        :type: bool
        """

        self._is_automated = is_automated

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
        if issubclass(Command, dict):
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
        if not isinstance(other, Command):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
