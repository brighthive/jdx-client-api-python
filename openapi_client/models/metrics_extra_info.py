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


class MetricsExtraInfo(object):
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
        'total_number': 'float',
        'recommended_content': 'str'
    }

    attribute_map = {
        'total_number': 'totalNumber',
        'recommended_content': 'recommendedContent'
    }

    def __init__(self, total_number=None, recommended_content=None):  # noqa: E501
        """MetricsExtraInfo - a model defined in OpenAPI"""  # noqa: E501

        self._total_number = None
        self._recommended_content = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if recommended_content is not None:
            self.recommended_content = recommended_content

    @property
    def total_number(self):
        """Gets the total_number of this MetricsExtraInfo.  # noqa: E501


        :return: The total_number of this MetricsExtraInfo.  # noqa: E501
        :rtype: float
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        """Sets the total_number of this MetricsExtraInfo.


        :param total_number: The total_number of this MetricsExtraInfo.  # noqa: E501
        :type: float
        """

        self._total_number = total_number

    @property
    def recommended_content(self):
        """Gets the recommended_content of this MetricsExtraInfo.  # noqa: E501

        A string to motivate the user to take some action, typically justified by the metricClass and aiming at improving the job description along the same lines as the metricClass  # noqa: E501

        :return: The recommended_content of this MetricsExtraInfo.  # noqa: E501
        :rtype: str
        """
        return self._recommended_content

    @recommended_content.setter
    def recommended_content(self, recommended_content):
        """Sets the recommended_content of this MetricsExtraInfo.

        A string to motivate the user to take some action, typically justified by the metricClass and aiming at improving the job description along the same lines as the metricClass  # noqa: E501

        :param recommended_content: The recommended_content of this MetricsExtraInfo.  # noqa: E501
        :type: str
        """
        if recommended_content is not None and len(recommended_content) > 1024:
            raise ValueError("Invalid value for `recommended_content`, length must be less than or equal to `1024`")  # noqa: E501

        self._recommended_content = recommended_content

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
        if not isinstance(other, MetricsExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
