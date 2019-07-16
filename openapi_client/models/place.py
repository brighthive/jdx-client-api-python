# coding: utf-8

"""
    JDX reference application API

    This is a collection of schemas and endpoints for the various JDX, Concentric Sky facing REST endpoints, the schemas define an API contract of sorts between the request and response expectations of the JDX reference application. This API is to be mutually developed by Concentric Sky and BrightHive.  # noqa: E501

    The version of the OpenAPI document: 0.0.16
    Contact: engineering@brighthive.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Place(object):
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
        'name': 'str',
        'description': 'str',
        'fax_number': 'str',
        'telephone': 'str',
        'address': 'PostalAddress',
        'geo': 'GeoCoordinates'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'fax_number': 'faxNumber',
        'telephone': 'telephone',
        'address': 'address',
        'geo': 'geo'
    }

    def __init__(self, name=None, description=None, fax_number=None, telephone=None, address=None, geo=None):  # noqa: E501
        """Place - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._fax_number = None
        self._telephone = None
        self._address = None
        self._geo = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if fax_number is not None:
            self.fax_number = fax_number
        if telephone is not None:
            self.telephone = telephone
        if address is not None:
            self.address = address
        if geo is not None:
            self.geo = geo

    @property
    def name(self):
        """Gets the name of this Place.  # noqa: E501


        :return: The name of this Place.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Place.


        :param name: The name of this Place.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 1024:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `1024`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Place.  # noqa: E501


        :return: The description of this Place.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Place.


        :param description: The description of this Place.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def fax_number(self):
        """Gets the fax_number of this Place.  # noqa: E501


        :return: The fax_number of this Place.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this Place.


        :param fax_number: The fax_number of this Place.  # noqa: E501
        :type: str
        """
        if fax_number is not None and len(fax_number) > 128:
            raise ValueError("Invalid value for `fax_number`, length must be less than or equal to `128`")  # noqa: E501

        self._fax_number = fax_number

    @property
    def telephone(self):
        """Gets the telephone of this Place.  # noqa: E501


        :return: The telephone of this Place.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this Place.


        :param telephone: The telephone of this Place.  # noqa: E501
        :type: str
        """
        if telephone is not None and len(telephone) > 64:
            raise ValueError("Invalid value for `telephone`, length must be less than or equal to `64`")  # noqa: E501

        self._telephone = telephone

    @property
    def address(self):
        """Gets the address of this Place.  # noqa: E501


        :return: The address of this Place.  # noqa: E501
        :rtype: PostalAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Place.


        :param address: The address of this Place.  # noqa: E501
        :type: PostalAddress
        """

        self._address = address

    @property
    def geo(self):
        """Gets the geo of this Place.  # noqa: E501


        :return: The geo of this Place.  # noqa: E501
        :rtype: GeoCoordinates
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        """Sets the geo of this Place.


        :param geo: The geo of this Place.  # noqa: E501
        :type: GeoCoordinates
        """

        self._geo = geo

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
        if not isinstance(other, Place):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
