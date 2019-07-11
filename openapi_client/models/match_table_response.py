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


class MatchTableResponse(object):
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
        'match_table': 'list[Substatements]',
        'pipeline_id': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'match_table': 'matchTable',
        'pipeline_id': 'pipelineID',
        'timestamp': 'timestamp'
    }

    def __init__(self, match_table=None, pipeline_id=None, timestamp=None):  # noqa: E501
        """MatchTableResponse - a model defined in OpenAPI"""  # noqa: E501

        self._match_table = None
        self._pipeline_id = None
        self._timestamp = None
        self.discriminator = None

        if match_table is not None:
            self.match_table = match_table
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def match_table(self):
        """Gets the match_table of this MatchTableResponse.  # noqa: E501


        :return: The match_table of this MatchTableResponse.  # noqa: E501
        :rtype: list[Substatements]
        """
        return self._match_table

    @match_table.setter
    def match_table(self, match_table):
        """Sets the match_table of this MatchTableResponse.


        :param match_table: The match_table of this MatchTableResponse.  # noqa: E501
        :type: list[Substatements]
        """

        self._match_table = match_table

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this MatchTableResponse.  # noqa: E501

        An identifier for this jdx reference application session of converting a raw job description  # noqa: E501

        :return: The pipeline_id of this MatchTableResponse.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this MatchTableResponse.

        An identifier for this jdx reference application session of converting a raw job description  # noqa: E501

        :param pipeline_id: The pipeline_id of this MatchTableResponse.  # noqa: E501
        :type: str
        """

        self._pipeline_id = pipeline_id

    @property
    def timestamp(self):
        """Gets the timestamp of this MatchTableResponse.  # noqa: E501

        A timestamp of when this response was generated  # noqa: E501

        :return: The timestamp of this MatchTableResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MatchTableResponse.

        A timestamp of when this response was generated  # noqa: E501

        :param timestamp: The timestamp of this MatchTableResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if not isinstance(other, MatchTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
