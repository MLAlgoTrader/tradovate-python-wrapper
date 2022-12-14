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

class AdminAlertSignal(object):
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
        'admin_alert_id': 'int',
        'related_to_account_id': 'int',
        'related_to_user_id': 'int',
        'owned_by_admin_id': 'int',
        'completed': 'datetime',
        'text': 'str',
        'email_sent': 'bool',
        'subject_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'admin_alert_id': 'adminAlertId',
        'related_to_account_id': 'relatedToAccountId',
        'related_to_user_id': 'relatedToUserId',
        'owned_by_admin_id': 'ownedByAdminId',
        'completed': 'completed',
        'text': 'text',
        'email_sent': 'emailSent',
        'subject_id': 'subjectId'
    }

    def __init__(self, id=None, timestamp=None, admin_alert_id=None, related_to_account_id=None, related_to_user_id=None, owned_by_admin_id=None, completed=None, text=None, email_sent=None, subject_id=None):  # noqa: E501
        """AdminAlertSignal - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._timestamp = None
        self._admin_alert_id = None
        self._related_to_account_id = None
        self._related_to_user_id = None
        self._owned_by_admin_id = None
        self._completed = None
        self._text = None
        self._email_sent = None
        self._subject_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.timestamp = timestamp
        self.admin_alert_id = admin_alert_id
        if related_to_account_id is not None:
            self.related_to_account_id = related_to_account_id
        if related_to_user_id is not None:
            self.related_to_user_id = related_to_user_id
        if owned_by_admin_id is not None:
            self.owned_by_admin_id = owned_by_admin_id
        if completed is not None:
            self.completed = completed
        self.text = text
        self.email_sent = email_sent
        self.subject_id = subject_id

    @property
    def id(self):
        """Gets the id of this AdminAlertSignal.  # noqa: E501


        :return: The id of this AdminAlertSignal.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminAlertSignal.


        :param id: The id of this AdminAlertSignal.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this AdminAlertSignal.  # noqa: E501


        :return: The timestamp of this AdminAlertSignal.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AdminAlertSignal.


        :param timestamp: The timestamp of this AdminAlertSignal.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def admin_alert_id(self):
        """Gets the admin_alert_id of this AdminAlertSignal.  # noqa: E501


        :return: The admin_alert_id of this AdminAlertSignal.  # noqa: E501
        :rtype: int
        """
        return self._admin_alert_id

    @admin_alert_id.setter
    def admin_alert_id(self, admin_alert_id):
        """Sets the admin_alert_id of this AdminAlertSignal.


        :param admin_alert_id: The admin_alert_id of this AdminAlertSignal.  # noqa: E501
        :type: int
        """
        if admin_alert_id is None:
            raise ValueError("Invalid value for `admin_alert_id`, must not be `None`")  # noqa: E501

        self._admin_alert_id = admin_alert_id

    @property
    def related_to_account_id(self):
        """Gets the related_to_account_id of this AdminAlertSignal.  # noqa: E501


        :return: The related_to_account_id of this AdminAlertSignal.  # noqa: E501
        :rtype: int
        """
        return self._related_to_account_id

    @related_to_account_id.setter
    def related_to_account_id(self, related_to_account_id):
        """Sets the related_to_account_id of this AdminAlertSignal.


        :param related_to_account_id: The related_to_account_id of this AdminAlertSignal.  # noqa: E501
        :type: int
        """

        self._related_to_account_id = related_to_account_id

    @property
    def related_to_user_id(self):
        """Gets the related_to_user_id of this AdminAlertSignal.  # noqa: E501


        :return: The related_to_user_id of this AdminAlertSignal.  # noqa: E501
        :rtype: int
        """
        return self._related_to_user_id

    @related_to_user_id.setter
    def related_to_user_id(self, related_to_user_id):
        """Sets the related_to_user_id of this AdminAlertSignal.


        :param related_to_user_id: The related_to_user_id of this AdminAlertSignal.  # noqa: E501
        :type: int
        """

        self._related_to_user_id = related_to_user_id

    @property
    def owned_by_admin_id(self):
        """Gets the owned_by_admin_id of this AdminAlertSignal.  # noqa: E501

        Owned By...  # noqa: E501

        :return: The owned_by_admin_id of this AdminAlertSignal.  # noqa: E501
        :rtype: int
        """
        return self._owned_by_admin_id

    @owned_by_admin_id.setter
    def owned_by_admin_id(self, owned_by_admin_id):
        """Sets the owned_by_admin_id of this AdminAlertSignal.

        Owned By...  # noqa: E501

        :param owned_by_admin_id: The owned_by_admin_id of this AdminAlertSignal.  # noqa: E501
        :type: int
        """

        self._owned_by_admin_id = owned_by_admin_id

    @property
    def completed(self):
        """Gets the completed of this AdminAlertSignal.  # noqa: E501


        :return: The completed of this AdminAlertSignal.  # noqa: E501
        :rtype: datetime
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this AdminAlertSignal.


        :param completed: The completed of this AdminAlertSignal.  # noqa: E501
        :type: datetime
        """

        self._completed = completed

    @property
    def text(self):
        """Gets the text of this AdminAlertSignal.  # noqa: E501


        :return: The text of this AdminAlertSignal.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AdminAlertSignal.


        :param text: The text of this AdminAlertSignal.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def email_sent(self):
        """Gets the email_sent of this AdminAlertSignal.  # noqa: E501


        :return: The email_sent of this AdminAlertSignal.  # noqa: E501
        :rtype: bool
        """
        return self._email_sent

    @email_sent.setter
    def email_sent(self, email_sent):
        """Sets the email_sent of this AdminAlertSignal.


        :param email_sent: The email_sent of this AdminAlertSignal.  # noqa: E501
        :type: bool
        """
        if email_sent is None:
            raise ValueError("Invalid value for `email_sent`, must not be `None`")  # noqa: E501

        self._email_sent = email_sent

    @property
    def subject_id(self):
        """Gets the subject_id of this AdminAlertSignal.  # noqa: E501


        :return: The subject_id of this AdminAlertSignal.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this AdminAlertSignal.


        :param subject_id: The subject_id of this AdminAlertSignal.  # noqa: E501
        :type: int
        """
        if subject_id is None:
            raise ValueError("Invalid value for `subject_id`, must not be `None`")  # noqa: E501

        self._subject_id = subject_id

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
        if issubclass(AdminAlertSignal, dict):
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
        if not isinstance(other, AdminAlertSignal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
