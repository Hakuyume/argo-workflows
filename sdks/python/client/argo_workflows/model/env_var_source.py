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


class EnvVarSource(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EnvVarSource represents a source for the value of an EnvVar.
    """

    @classmethod
    @property
    def configMapKeyRef(cls) -> typing.Type['ConfigMapKeySelector']:
        return ConfigMapKeySelector

    @classmethod
    @property
    def fieldRef(cls) -> typing.Type['ObjectFieldSelector']:
        return ObjectFieldSelector

    @classmethod
    @property
    def resourceFieldRef(cls) -> typing.Type['ResourceFieldSelector']:
        return ResourceFieldSelector

    @classmethod
    @property
    def secretKeyRef(cls) -> typing.Type['SecretKeySelector']:
        return SecretKeySelector


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        configMapKeyRef: typing.Union['ConfigMapKeySelector', Unset] = unset,
        fieldRef: typing.Union['ObjectFieldSelector', Unset] = unset,
        resourceFieldRef: typing.Union['ResourceFieldSelector', Unset] = unset,
        secretKeyRef: typing.Union['SecretKeySelector', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'EnvVarSource':
        return super().__new__(
            cls,
            *args,
            configMapKeyRef=configMapKeyRef,
            fieldRef=fieldRef,
            resourceFieldRef=resourceFieldRef,
            secretKeyRef=secretKeyRef,
            _configuration=_configuration,
            **kwargs,
        )

from argo_workflows.model.config_map_key_selector import ConfigMapKeySelector
from argo_workflows.model.object_field_selector import ObjectFieldSelector
from argo_workflows.model.resource_field_selector import ResourceFieldSelector
from argo_workflows.model.secret_key_selector import SecretKeySelector
