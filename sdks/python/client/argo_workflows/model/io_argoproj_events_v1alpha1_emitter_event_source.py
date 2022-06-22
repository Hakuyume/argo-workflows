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


class IoArgoprojEventsV1alpha1EmitterEventSource(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    broker = StrSchema
    channelKey = StrSchema
    channelName = StrSchema

    @classmethod
    @property
    def connectionBackoff(cls) -> typing.Type['IoArgoprojEventsV1alpha1Backoff']:
        return IoArgoprojEventsV1alpha1Backoff

    @classmethod
    @property
    def filter(cls) -> typing.Type['IoArgoprojEventsV1alpha1EventSourceFilter']:
        return IoArgoprojEventsV1alpha1EventSourceFilter
    jsonBody = BoolSchema
    
    
    class metadata(
        DictSchema
    ):
        _additional_properties = StrSchema
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'metadata':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )

    @classmethod
    @property
    def password(cls) -> typing.Type['SecretKeySelector']:
        return SecretKeySelector

    @classmethod
    @property
    def tls(cls) -> typing.Type['IoArgoprojEventsV1alpha1TLSConfig']:
        return IoArgoprojEventsV1alpha1TLSConfig

    @classmethod
    @property
    def username(cls) -> typing.Type['SecretKeySelector']:
        return SecretKeySelector


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        broker: typing.Union[broker, Unset] = unset,
        channelKey: typing.Union[channelKey, Unset] = unset,
        channelName: typing.Union[channelName, Unset] = unset,
        connectionBackoff: typing.Union['IoArgoprojEventsV1alpha1Backoff', Unset] = unset,
        filter: typing.Union['IoArgoprojEventsV1alpha1EventSourceFilter', Unset] = unset,
        jsonBody: typing.Union[jsonBody, Unset] = unset,
        metadata: typing.Union[metadata, Unset] = unset,
        password: typing.Union['SecretKeySelector', Unset] = unset,
        tls: typing.Union['IoArgoprojEventsV1alpha1TLSConfig', Unset] = unset,
        username: typing.Union['SecretKeySelector', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'IoArgoprojEventsV1alpha1EmitterEventSource':
        return super().__new__(
            cls,
            *args,
            broker=broker,
            channelKey=channelKey,
            channelName=channelName,
            connectionBackoff=connectionBackoff,
            filter=filter,
            jsonBody=jsonBody,
            metadata=metadata,
            password=password,
            tls=tls,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )

from argo_workflows.model.io_argoproj_events_v1alpha1_backoff import IoArgoprojEventsV1alpha1Backoff
from argo_workflows.model.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.model.io_argoproj_events_v1alpha1_tls_config import IoArgoprojEventsV1alpha1TLSConfig
from argo_workflows.model.secret_key_selector import SecretKeySelector
