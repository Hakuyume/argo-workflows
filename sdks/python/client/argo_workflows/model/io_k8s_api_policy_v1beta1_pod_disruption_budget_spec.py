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


class IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.
    """
    maxUnavailable = StrSchema
    minAvailable = StrSchema

    @classmethod
    @property
    def selector(cls) -> typing.Type['LabelSelector']:
        return LabelSelector


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        maxUnavailable: typing.Union[maxUnavailable, Unset] = unset,
        minAvailable: typing.Union[minAvailable, Unset] = unset,
        selector: typing.Union['LabelSelector', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec':
        return super().__new__(
            cls,
            *args,
            maxUnavailable=maxUnavailable,
            minAvailable=minAvailable,
            selector=selector,
            _configuration=_configuration,
            **kwargs,
        )

from argo_workflows.model.label_selector import LabelSelector
