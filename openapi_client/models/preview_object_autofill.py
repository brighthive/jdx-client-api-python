# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.12
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PreviewObjectAutofill(object):
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
        'soc': 'str',
        'naics': 'str'
    }

    attribute_map = {
        'soc': 'soc',
        'naics': 'naics'
    }

    def __init__(self, soc=None, naics=None):  # noqa: E501
        """PreviewObjectAutofill - a model defined in OpenAPI"""  # noqa: E501

        self._soc = None
        self._naics = None
        self.discriminator = None

        if soc is not None:
            self.soc = soc
        if naics is not None:
            self.naics = naics

    @property
    def soc(self):
        """Gets the soc of this PreviewObjectAutofill.  # noqa: E501


        :return: The soc of this PreviewObjectAutofill.  # noqa: E501
        :rtype: str
        """
        return self._soc

    @soc.setter
    def soc(self, soc):
        """Sets the soc of this PreviewObjectAutofill.


        :param soc: The soc of this PreviewObjectAutofill.  # noqa: E501
        :type: str
        """

        self._soc = soc

    @property
    def naics(self):
        """Gets the naics of this PreviewObjectAutofill.  # noqa: E501


        :return: The naics of this PreviewObjectAutofill.  # noqa: E501
        :rtype: str
        """
        return self._naics

    @naics.setter
    def naics(self, naics):
        """Sets the naics of this PreviewObjectAutofill.


        :param naics: The naics of this PreviewObjectAutofill.  # noqa: E501
        :type: str
        """

        self._naics = naics

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
        if not isinstance(other, PreviewObjectAutofill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
