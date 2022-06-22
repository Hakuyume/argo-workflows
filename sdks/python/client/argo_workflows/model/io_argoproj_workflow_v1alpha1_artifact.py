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


class IoArgoprojWorkflowV1alpha1Artifact(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Artifact indicates an artifact to place at a specified path
    """
    _required_property_names = set((
        'name',
    ))

    @classmethod
    @property
    def archive(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1ArchiveStrategy']:
        return IoArgoprojWorkflowV1alpha1ArchiveStrategy
    archiveLogs = BoolSchema

    @classmethod
    @property
    def artifactGC(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1ArtifactGC']:
        return IoArgoprojWorkflowV1alpha1ArtifactGC

    @classmethod
    @property
    def artifactory(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1ArtifactoryArtifact']:
        return IoArgoprojWorkflowV1alpha1ArtifactoryArtifact
    deleted = BoolSchema
    _from = StrSchema
    locals()['from'] = _from
    del locals()['_from']
    fromExpression = StrSchema

    @classmethod
    @property
    def gcs(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1GCSArtifact']:
        return IoArgoprojWorkflowV1alpha1GCSArtifact

    @classmethod
    @property
    def git(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1GitArtifact']:
        return IoArgoprojWorkflowV1alpha1GitArtifact
    globalName = StrSchema

    @classmethod
    @property
    def hdfs(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1HDFSArtifact']:
        return IoArgoprojWorkflowV1alpha1HDFSArtifact

    @classmethod
    @property
    def http(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1HTTPArtifact']:
        return IoArgoprojWorkflowV1alpha1HTTPArtifact
    mode = IntSchema
    name = StrSchema
    optional = BoolSchema

    @classmethod
    @property
    def oss(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1OSSArtifact']:
        return IoArgoprojWorkflowV1alpha1OSSArtifact
    path = StrSchema

    @classmethod
    @property
    def raw(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1RawArtifact']:
        return IoArgoprojWorkflowV1alpha1RawArtifact
    recurseMode = BoolSchema

    @classmethod
    @property
    def s3(cls) -> typing.Type['IoArgoprojWorkflowV1alpha1S3Artifact']:
        return IoArgoprojWorkflowV1alpha1S3Artifact
    subPath = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: name,
        archive: typing.Union['IoArgoprojWorkflowV1alpha1ArchiveStrategy', Unset] = unset,
        archiveLogs: typing.Union[archiveLogs, Unset] = unset,
        artifactGC: typing.Union['IoArgoprojWorkflowV1alpha1ArtifactGC', Unset] = unset,
        artifactory: typing.Union['IoArgoprojWorkflowV1alpha1ArtifactoryArtifact', Unset] = unset,
        deleted: typing.Union[deleted, Unset] = unset,
        fromExpression: typing.Union[fromExpression, Unset] = unset,
        gcs: typing.Union['IoArgoprojWorkflowV1alpha1GCSArtifact', Unset] = unset,
        git: typing.Union['IoArgoprojWorkflowV1alpha1GitArtifact', Unset] = unset,
        globalName: typing.Union[globalName, Unset] = unset,
        hdfs: typing.Union['IoArgoprojWorkflowV1alpha1HDFSArtifact', Unset] = unset,
        http: typing.Union['IoArgoprojWorkflowV1alpha1HTTPArtifact', Unset] = unset,
        mode: typing.Union[mode, Unset] = unset,
        optional: typing.Union[optional, Unset] = unset,
        oss: typing.Union['IoArgoprojWorkflowV1alpha1OSSArtifact', Unset] = unset,
        path: typing.Union[path, Unset] = unset,
        raw: typing.Union['IoArgoprojWorkflowV1alpha1RawArtifact', Unset] = unset,
        recurseMode: typing.Union[recurseMode, Unset] = unset,
        s3: typing.Union['IoArgoprojWorkflowV1alpha1S3Artifact', Unset] = unset,
        subPath: typing.Union[subPath, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'IoArgoprojWorkflowV1alpha1Artifact':
        return super().__new__(
            cls,
            *args,
            name=name,
            archive=archive,
            archiveLogs=archiveLogs,
            artifactGC=artifactGC,
            artifactory=artifactory,
            deleted=deleted,
            fromExpression=fromExpression,
            gcs=gcs,
            git=git,
            globalName=globalName,
            hdfs=hdfs,
            http=http,
            mode=mode,
            optional=optional,
            oss=oss,
            path=path,
            raw=raw,
            recurseMode=recurseMode,
            s3=s3,
            subPath=subPath,
            _configuration=_configuration,
            **kwargs,
        )

from argo_workflows.model.io_argoproj_workflow_v1alpha1_archive_strategy import IoArgoprojWorkflowV1alpha1ArchiveStrategy
from argo_workflows.model.io_argoproj_workflow_v1alpha1_artifact_gc import IoArgoprojWorkflowV1alpha1ArtifactGC
from argo_workflows.model.io_argoproj_workflow_v1alpha1_artifactory_artifact import IoArgoprojWorkflowV1alpha1ArtifactoryArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_gcs_artifact import IoArgoprojWorkflowV1alpha1GCSArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_git_artifact import IoArgoprojWorkflowV1alpha1GitArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_hdfs_artifact import IoArgoprojWorkflowV1alpha1HDFSArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_http_artifact import IoArgoprojWorkflowV1alpha1HTTPArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_oss_artifact import IoArgoprojWorkflowV1alpha1OSSArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_raw_artifact import IoArgoprojWorkflowV1alpha1RawArtifact
from argo_workflows.model.io_argoproj_workflow_v1alpha1_s3_artifact import IoArgoprojWorkflowV1alpha1S3Artifact
