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


class FrameworkData(object):
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
        'uuid': 'str',
        'object_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'object_type': 'objectType',
        'name': 'name'
    }

    def __init__(self, uuid=None, object_type=None, name=None):  # noqa: E501
        """FrameworkData - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._object_type = None
        self._name = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if object_type is not None:
            self.object_type = object_type
        if name is not None:
            self.name = name

    @property
    def uuid(self):
        """Gets the uuid of this FrameworkData.  # noqa: E501

        uuid of framework  # noqa: E501

        :return: The uuid of this FrameworkData.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FrameworkData.

        uuid of framework  # noqa: E501

        :param uuid: The uuid of this FrameworkData.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def object_type(self):
        """Gets the object_type of this FrameworkData.  # noqa: E501

        competency, industry, occupation?  # noqa: E501

        :return: The object_type of this FrameworkData.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this FrameworkData.

        competency, industry, occupation?  # noqa: E501

        :param object_type: The object_type of this FrameworkData.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def name(self):
        """Gets the name of this FrameworkData.  # noqa: E501

        name of the framework  # noqa: E501

        :return: The name of this FrameworkData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FrameworkData.

        name of the framework  # noqa: E501

        :param name: The name of this FrameworkData.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, FrameworkData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
