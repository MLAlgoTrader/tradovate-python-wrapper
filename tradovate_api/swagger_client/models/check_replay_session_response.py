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

class CheckReplaySessionResponse(object):
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
        'check_status': 'str',
        'start_timestamp': 'datetime'
    }

    attribute_map = {
        'check_status': 'checkStatus',
        'start_timestamp': 'startTimestamp'
    }

    def __init__(self, check_status=None, start_timestamp=None):  # noqa: E501
        """CheckReplaySessionResponse - a model defined in Swagger"""  # noqa: E501
        self._check_status = None
        self._start_timestamp = None
        self.discriminator = None
        self.check_status = check_status
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp

    @property
    def check_status(self):
        """Gets the check_status of this CheckReplaySessionResponse.  # noqa: E501

        Ineligible, OK, StartTimestampAdjusted  # noqa: E501

        :return: The check_status of this CheckReplaySessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._check_status

    @check_status.setter
    def check_status(self, check_status):
        """Sets the check_status of this CheckReplaySessionResponse.

        Ineligible, OK, StartTimestampAdjusted  # noqa: E501

        :param check_status: The check_status of this CheckReplaySessionResponse.  # noqa: E501
        :type: str
        """
        if check_status is None:
            raise ValueError("Invalid value for `check_status`, must not be `None`")  # noqa: E501
        allowed_values = ["Ineligible", "OK", "StartTimestampAdjusted"]  # noqa: E501
        if check_status not in allowed_values:
            raise ValueError(
                "Invalid value for `check_status` ({0}), must be one of {1}"  # noqa: E501
                .format(check_status, allowed_values)
            )

        self._check_status = check_status

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this CheckReplaySessionResponse.  # noqa: E501


        :return: The start_timestamp of this CheckReplaySessionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this CheckReplaySessionResponse.


        :param start_timestamp: The start_timestamp of this CheckReplaySessionResponse.  # noqa: E501
        :type: datetime
        """

        self._start_timestamp = start_timestamp

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
        if issubclass(CheckReplaySessionResponse, dict):
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
        if not isinstance(other, CheckReplaySessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
