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


class IoArgoprojEventsV1alpha1GithubEventSource(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    active = BoolSchema

    @classmethod
    @property
    def apiToken(cls) -> typing.Type['SecretKeySelector']:
        return SecretKeySelector
    contentType = StrSchema
    deleteHookOnFinish = BoolSchema
    
    
    class events(
        ListSchema
    ):
        _items = StrSchema

    @classmethod
    @property
    def filter(cls) -> typing.Type['IoArgoprojEventsV1alpha1EventSourceFilter']:
        return IoArgoprojEventsV1alpha1EventSourceFilter

    @classmethod
    @property
    def githubApp(cls) -> typing.Type['IoArgoprojEventsV1alpha1GithubAppCreds']:
        return IoArgoprojEventsV1alpha1GithubAppCreds
    githubBaseURL = StrSchema
    githubUploadURL = StrSchema
    id = StrSchema
    insecure = BoolSchema
    
    
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
    
    
    class organizations(
        ListSchema
    ):
        _items = StrSchema
    owner = StrSchema
    
    
    class repositories(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['IoArgoprojEventsV1alpha1OwnedRepositories']:
            return IoArgoprojEventsV1alpha1OwnedRepositories
    repository = StrSchema

    @classmethod
    @property
    def webhook(cls) -> typing.Type['IoArgoprojEventsV1alpha1WebhookContext']:
        return IoArgoprojEventsV1alpha1WebhookContext

    @classmethod
    @property
    def webhookSecret(cls) -> typing.Type['SecretKeySelector']:
        return SecretKeySelector


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        active: typing.Union[active, Unset] = unset,
        apiToken: typing.Union['SecretKeySelector', Unset] = unset,
        contentType: typing.Union[contentType, Unset] = unset,
        deleteHookOnFinish: typing.Union[deleteHookOnFinish, Unset] = unset,
        events: typing.Union[events, Unset] = unset,
        filter: typing.Union['IoArgoprojEventsV1alpha1EventSourceFilter', Unset] = unset,
        githubApp: typing.Union['IoArgoprojEventsV1alpha1GithubAppCreds', Unset] = unset,
        githubBaseURL: typing.Union[githubBaseURL, Unset] = unset,
        githubUploadURL: typing.Union[githubUploadURL, Unset] = unset,
        id: typing.Union[id, Unset] = unset,
        insecure: typing.Union[insecure, Unset] = unset,
        metadata: typing.Union[metadata, Unset] = unset,
        organizations: typing.Union[organizations, Unset] = unset,
        owner: typing.Union[owner, Unset] = unset,
        repositories: typing.Union[repositories, Unset] = unset,
        repository: typing.Union[repository, Unset] = unset,
        webhook: typing.Union['IoArgoprojEventsV1alpha1WebhookContext', Unset] = unset,
        webhookSecret: typing.Union['SecretKeySelector', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'IoArgoprojEventsV1alpha1GithubEventSource':
        return super().__new__(
            cls,
            *args,
            active=active,
            apiToken=apiToken,
            contentType=contentType,
            deleteHookOnFinish=deleteHookOnFinish,
            events=events,
            filter=filter,
            githubApp=githubApp,
            githubBaseURL=githubBaseURL,
            githubUploadURL=githubUploadURL,
            id=id,
            insecure=insecure,
            metadata=metadata,
            organizations=organizations,
            owner=owner,
            repositories=repositories,
            repository=repository,
            webhook=webhook,
            webhookSecret=webhookSecret,
            _configuration=_configuration,
            **kwargs,
        )

from argo_workflows.model.io_argoproj_events_v1alpha1_event_source_filter import IoArgoprojEventsV1alpha1EventSourceFilter
from argo_workflows.model.io_argoproj_events_v1alpha1_github_app_creds import IoArgoprojEventsV1alpha1GithubAppCreds
from argo_workflows.model.io_argoproj_events_v1alpha1_owned_repositories import IoArgoprojEventsV1alpha1OwnedRepositories
from argo_workflows.model.io_argoproj_events_v1alpha1_webhook_context import IoArgoprojEventsV1alpha1WebhookContext
from argo_workflows.model.secret_key_selector import SecretKeySelector
