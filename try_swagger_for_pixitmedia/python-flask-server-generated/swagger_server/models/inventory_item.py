# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.manufacturer import Manufacturer  # noqa: F401,E501
from swagger_server import util


class InventoryItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, release_date: str=None, manufacturer: Manufacturer=None):  # noqa: E501
        """InventoryItem - a model defined in Swagger

        :param id: The id of this InventoryItem.  # noqa: E501
        :type id: str
        :param name: The name of this InventoryItem.  # noqa: E501
        :type name: str
        :param release_date: The release_date of this InventoryItem.  # noqa: E501
        :type release_date: str
        :param manufacturer: The manufacturer of this InventoryItem.  # noqa: E501
        :type manufacturer: Manufacturer
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'release_date': str,
            'manufacturer': Manufacturer
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'release_date': 'releaseDate',
            'manufacturer': 'manufacturer'
        }

        self._id = id
        self._name = name
        self._release_date = release_date
        self._manufacturer = manufacturer

    @classmethod
    def from_dict(cls, dikt) -> 'InventoryItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InventoryItem of this InventoryItem.  # noqa: E501
        :rtype: InventoryItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this InventoryItem.


        :return: The id of this InventoryItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this InventoryItem.


        :param id: The id of this InventoryItem.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this InventoryItem.


        :return: The name of this InventoryItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InventoryItem.


        :param name: The name of this InventoryItem.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def release_date(self) -> str:
        """Gets the release_date of this InventoryItem.


        :return: The release_date of this InventoryItem.
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date: str):
        """Sets the release_date of this InventoryItem.


        :param release_date: The release_date of this InventoryItem.
        :type release_date: str
        """
        if release_date is None:
            raise ValueError("Invalid value for `release_date`, must not be `None`")  # noqa: E501

        self._release_date = release_date

    @property
    def manufacturer(self) -> Manufacturer:
        """Gets the manufacturer of this InventoryItem.


        :return: The manufacturer of this InventoryItem.
        :rtype: Manufacturer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: Manufacturer):
        """Sets the manufacturer of this InventoryItem.


        :param manufacturer: The manufacturer of this InventoryItem.
        :type manufacturer: Manufacturer
        """
        if manufacturer is None:
            raise ValueError("Invalid value for `manufacturer`, must not be `None`")  # noqa: E501

        self._manufacturer = manufacturer
