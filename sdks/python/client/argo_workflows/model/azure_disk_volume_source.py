# coding: utf-8

"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from argo_workflows.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class AzureDiskVolumeSource(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    _required_property_names = set((
        'diskName',
        'diskURI',
    ))
    cachingMode = StrSchema
    diskName = StrSchema
    diskURI = StrSchema
    fsType = StrSchema
    kind = StrSchema
    readOnly = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        diskName: diskName,
        diskURI: diskURI,
        cachingMode: typing.Union[cachingMode, Unset] = unset,
        fsType: typing.Union[fsType, Unset] = unset,
        kind: typing.Union[kind, Unset] = unset,
        readOnly: typing.Union[readOnly, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AzureDiskVolumeSource':
        return super().__new__(
            cls,
            *args,
            diskName=diskName,
            diskURI=diskURI,
            cachingMode=cachingMode,
            fsType=fsType,
            kind=kind,
            readOnly=readOnly,
            _configuration=_configuration,
            **kwargs,
        )
