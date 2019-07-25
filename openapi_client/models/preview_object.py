# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.17
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PreviewObject(object):
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
        'fields': 'list[PreviewFields]',
        'paragraphs': 'list[str]',
        'autofill': 'PreviewObjectAutofill'
    }

    attribute_map = {
        'fields': 'fields',
        'paragraphs': 'paragraphs',
        'autofill': 'autofill'
    }

    def __init__(self, fields=None, paragraphs=None, autofill=None):  # noqa: E501
        """PreviewObject - a model defined in OpenAPI"""  # noqa: E501

        self._fields = None
        self._paragraphs = None
        self._autofill = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if paragraphs is not None:
            self.paragraphs = paragraphs
        if autofill is not None:
            self.autofill = autofill

    @property
    def fields(self):
        """Gets the fields of this PreviewObject.  # noqa: E501


        :return: The fields of this PreviewObject.  # noqa: E501
        :rtype: list[PreviewFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this PreviewObject.


        :param fields: The fields of this PreviewObject.  # noqa: E501
        :type: list[PreviewFields]
        """

        self._fields = fields

    @property
    def paragraphs(self):
        """Gets the paragraphs of this PreviewObject.  # noqa: E501


        :return: The paragraphs of this PreviewObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this PreviewObject.


        :param paragraphs: The paragraphs of this PreviewObject.  # noqa: E501
        :type: list[str]
        """

        self._paragraphs = paragraphs

    @property
    def autofill(self):
        """Gets the autofill of this PreviewObject.  # noqa: E501


        :return: The autofill of this PreviewObject.  # noqa: E501
        :rtype: PreviewObjectAutofill
        """
        return self._autofill

    @autofill.setter
    def autofill(self, autofill):
        """Sets the autofill of this PreviewObject.


        :param autofill: The autofill of this PreviewObject.  # noqa: E501
        :type: PreviewObjectAutofill
        """

        self._autofill = autofill

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
        if not isinstance(other, PreviewObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
