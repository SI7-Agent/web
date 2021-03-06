# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class Object(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, value: str=None):  # noqa: E501
        """Object - a model defined in Swagger

        :param id: The id of this Object.  # noqa: E501
        :type id: int
        :param value: The value of this Object.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'id': int,
            'value': str
        }

        self.attribute_map = {
            'id': 'id',
            'value': 'value'
        }

        self._id = id
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Object':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Object of this Object.  # noqa: E501
        :rtype: Object
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Object.


        :return: The id of this Object.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Object.


        :param id: The id of this Object.
        :type id: int
        """

        self._id = id

    @property
    def value(self) -> str:
        """Gets the value of this Object.

        Detection values  # noqa: E501

        :return: The value of this Object.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Object.

        Detection values  # noqa: E501

        :param value: The value of this Object.
        :type value: str
        """

        self._value = value
