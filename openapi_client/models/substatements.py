# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.13
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Substatements(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'substatement_id': 'str',
        'substatement': 'str',
        'matches': 'list[SubstatementsMatches]'
    }

    attribute_map = {
        'substatement_id': 'substatementID',
        'substatement': 'substatement',
        'matches': 'matches'
    }

    def __init__(self, substatement_id=None, substatement=None, matches=None):  # noqa: E501
        """Substatements - a model defined in OpenAPI"""  # noqa: E501

        self._substatement_id = None
        self._substatement = None
        self._matches = None
        self.discriminator = None

        if substatement_id is not None:
            self.substatement_id = substatement_id
        if substatement is not None:
            self.substatement = substatement
        if matches is not None:
            self.matches = matches

    @property
    def substatement_id(self):
        """Gets the substatement_id of this Substatements.  # noqa: E501

        UUID referring to  # noqa: E501

        :return: The substatement_id of this Substatements.  # noqa: E501
        :rtype: str
        """
        return self._substatement_id

    @substatement_id.setter
    def substatement_id(self, substatement_id):
        """Sets the substatement_id of this Substatements.

        UUID referring to  # noqa: E501

        :param substatement_id: The substatement_id of this Substatements.  # noqa: E501
        :type: str
        """

        self._substatement_id = substatement_id

    @property
    def substatement(self):
        """Gets the substatement of this Substatements.  # noqa: E501

        this is the job description substatment text  # noqa: E501

        :return: The substatement of this Substatements.  # noqa: E501
        :rtype: str
        """
        return self._substatement

    @substatement.setter
    def substatement(self, substatement):
        """Sets the substatement of this Substatements.

        this is the job description substatment text  # noqa: E501

        :param substatement: The substatement of this Substatements.  # noqa: E501
        :type: str
        """

        self._substatement = substatement

    @property
    def matches(self):
        """Gets the matches of this Substatements.  # noqa: E501


        :return: The matches of this Substatements.  # noqa: E501
        :rtype: list[SubstatementsMatches]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this Substatements.


        :param matches: The matches of this Substatements.  # noqa: E501
        :type: list[SubstatementsMatches]
        """

        self._matches = matches

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Substatements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
