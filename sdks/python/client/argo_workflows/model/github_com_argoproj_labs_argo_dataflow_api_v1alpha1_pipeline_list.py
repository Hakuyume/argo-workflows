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


class GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class items(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline']:
            return GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline

    @classmethod
    @property
    def metadata(cls) -> typing.Type['ListMeta']:
        return ListMeta


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        items: typing.Union[items, Unset] = unset,
        metadata: typing.Union['ListMeta', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList':
        return super().__new__(
            cls,
            *args,
            items=items,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from argo_workflows.model.github_com_argoproj_labs_argo_dataflow_api_v1alpha1_pipeline import GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline
from argo_workflows.model.list_meta import ListMeta
