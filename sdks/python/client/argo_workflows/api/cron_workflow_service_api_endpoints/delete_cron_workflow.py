# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from argo_workflows import api_client, exceptions
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

from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError

# query params
DeleteOptionsGracePeriodSecondsSchema = StrSchema
DeleteOptionsPreconditionsUidSchema = StrSchema
DeleteOptionsPreconditionsResourceVersionSchema = StrSchema
DeleteOptionsOrphanDependentsSchema = BoolSchema
DeleteOptionsPropagationPolicySchema = StrSchema


class DeleteOptionsDryRunSchema(
    ListSchema
):
    _items = StrSchema
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'deleteOptions.gracePeriodSeconds': DeleteOptionsGracePeriodSecondsSchema,
        'deleteOptions.preconditions.uid': DeleteOptionsPreconditionsUidSchema,
        'deleteOptions.preconditions.resourceVersion': DeleteOptionsPreconditionsResourceVersionSchema,
        'deleteOptions.orphanDependents': DeleteOptionsOrphanDependentsSchema,
        'deleteOptions.propagationPolicy': DeleteOptionsPropagationPolicySchema,
        'deleteOptions.dryRun': DeleteOptionsDryRunSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_delete_options_grace_period_seconds = api_client.QueryParameter(
    name="deleteOptions.gracePeriodSeconds",
    schema=DeleteOptionsGracePeriodSecondsSchema,
)
request_query_delete_options_preconditions_uid = api_client.QueryParameter(
    name="deleteOptions.preconditions.uid",
    schema=DeleteOptionsPreconditionsUidSchema,
)
request_query_delete_options_preconditions_resource_version = api_client.QueryParameter(
    name="deleteOptions.preconditions.resourceVersion",
    schema=DeleteOptionsPreconditionsResourceVersionSchema,
)
request_query_delete_options_orphan_dependents = api_client.QueryParameter(
    name="deleteOptions.orphanDependents",
    schema=DeleteOptionsOrphanDependentsSchema,
)
request_query_delete_options_propagation_policy = api_client.QueryParameter(
    name="deleteOptions.propagationPolicy",
    schema=DeleteOptionsPropagationPolicySchema,
)
request_query_delete_options_dry_run = api_client.QueryParameter(
    name="deleteOptions.dryRun",
    style=api_client.ParameterStyle.FORM,
    schema=DeleteOptionsDryRunSchema,
    explode=True,
)
# path params
NamespaceSchema = StrSchema
NameSchema = StrSchema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'namespace': NamespaceSchema,
        'name': NameSchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_namespace = api_client.PathParameter(
    name="namespace",
    schema=NamespaceSchema,
    required=True,
)
request_path_name = api_client.PathParameter(
    name="name",
    schema=NameSchema,
    required=True,
)
_path = '/api/v1/cron-workflows/{namespace}/{name}'
_method = 'DELETE'
_auth = [
    'BearerToken',
]
SchemaFor200ResponseBodyApplicationJson = DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = GrpcGatewayRuntimeError


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class DeleteCronWorkflow(api_client.Api):

    def delete_cron_workflow(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)

        _path_params = {}
        for parameter in (
            request_path_namespace,
            request_path_name,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        _query_params = []
        for parameter in (
            request_query_delete_options_grace_period_seconds,
            request_query_delete_options_preconditions_uid,
            request_query_delete_options_preconditions_resource_version,
            request_query_delete_options_orphan_dependents,
            request_query_delete_options_propagation_policy,
            request_query_delete_options_dry_run,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _query_params.extend(serialized_data)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            path_params=_path_params,
            query_params=tuple(_query_params),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                default_response = _status_code_to_response.get('default')
                if default_response:
                    api_response = default_response.deserialize(response, self.api_client.configuration)
                else:
                    api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
