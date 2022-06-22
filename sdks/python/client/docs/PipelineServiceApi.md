# argo_workflows.PipelineServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pipeline**](PipelineServiceApi.md#delete_pipeline) | **DELETE** /api/v1/pipelines/{namespace}/{name} | 
[**get_pipeline**](PipelineServiceApi.md#get_pipeline) | **GET** /api/v1/pipelines/{namespace}/{name} | 
[**list_pipelines**](PipelineServiceApi.md#list_pipelines) | **GET** /api/v1/pipelines/{namespace} | 
[**pipeline_logs**](PipelineServiceApi.md#pipeline_logs) | **GET** /api/v1/stream/pipelines/{namespace}/logs | 
[**restart_pipeline**](PipelineServiceApi.md#restart_pipeline) | **POST** /api/v1/pipelines/{namespace}/{name}/restart | 
[**watch_pipelines**](PipelineServiceApi.md#watch_pipelines) | **GET** /api/v1/stream/pipelines/{namespace} | 
[**watch_steps**](PipelineServiceApi.md#watch_steps) | **GET** /api/v1/stream/steps/{namespace} | 

# **delete_pipeline**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_pipeline(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_pipeline(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->delete_pipeline: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
        'deleteOptions.gracePeriodSeconds': "deleteOptions.gracePeriodSeconds_example",
        'deleteOptions.preconditions.uid': "deleteOptions.preconditions.uid_example",
        'deleteOptions.preconditions.resourceVersion': "deleteOptions.preconditions.resourceVersion_example",
        'deleteOptions.orphanDependents': True,
        'deleteOptions.propagationPolicy': "deleteOptions.propagationPolicy_example",
        'deleteOptions.dryRun': [
        "deleteOptions.dryRun_example"
    ],
    }
    try:
        api_response = api_instance.delete_pipeline(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->delete_pipeline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deleteOptions.gracePeriodSeconds | DeleteOptionsGracePeriodSecondsSchema | | optional
deleteOptions.preconditions.uid | DeleteOptionsPreconditionsUidSchema | | optional
deleteOptions.preconditions.resourceVersion | DeleteOptionsPreconditionsResourceVersionSchema | | optional
deleteOptions.orphanDependents | DeleteOptionsOrphanDependentsSchema | | optional
deleteOptions.propagationPolicy | DeleteOptionsPropagationPolicySchema | | optional
deleteOptions.dryRun | DeleteOptionsDryRunSchema | | optional


#### DeleteOptionsGracePeriodSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsPreconditionsUidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsPreconditionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsOrphanDependentsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### DeleteOptionsPropagationPolicySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DeleteOptionsDryRunSchema

Type | Description | Notes
------------- | ------------- | -------------
**[str]** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline get_pipeline(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.github_com_argoproj_labs_argo_dataflow_api_v1alpha1_pipeline import GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_pipeline(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->get_pipeline: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    query_params = {
        'getOptions.resourceVersion': "getOptions.resourceVersion_example",
    }
    try:
        api_response = api_instance.get_pipeline(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->get_pipeline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
getOptions.resourceVersion | GetOptionsResourceVersionSchema | | optional


#### GetOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline**](GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



[**GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline**](GithubComArgoprojLabsArgoDataflowApiV1alpha1Pipeline.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList list_pipelines(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.github_com_argoproj_labs_argo_dataflow_api_v1alpha1_pipeline_list import GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_pipelines(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->list_pipelines: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'listOptions.labelSelector': "listOptions.labelSelector_example",
        'listOptions.fieldSelector': "listOptions.fieldSelector_example",
        'listOptions.watch': True,
        'listOptions.allowWatchBookmarks': True,
        'listOptions.resourceVersion': "listOptions.resourceVersion_example",
        'listOptions.resourceVersionMatch': "listOptions.resourceVersionMatch_example",
        'listOptions.timeoutSeconds': "listOptions.timeoutSeconds_example",
        'listOptions.limit': "listOptions.limit_example",
        'listOptions.continue': "listOptions.continue_example",
    }
    try:
        api_response = api_instance.list_pipelines(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->list_pipelines: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
listOptions.labelSelector | ListOptionsLabelSelectorSchema | | optional
listOptions.fieldSelector | ListOptionsFieldSelectorSchema | | optional
listOptions.watch | ListOptionsWatchSchema | | optional
listOptions.allowWatchBookmarks | ListOptionsAllowWatchBookmarksSchema | | optional
listOptions.resourceVersion | ListOptionsResourceVersionSchema | | optional
listOptions.resourceVersionMatch | ListOptionsResourceVersionMatchSchema | | optional
listOptions.timeoutSeconds | ListOptionsTimeoutSecondsSchema | | optional
listOptions.limit | ListOptionsLimitSchema | | optional
listOptions.continue | ListOptionsContinueSchema | | optional


#### ListOptionsLabelSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsFieldSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsWatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsAllowWatchBookmarksSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsResourceVersionMatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsTimeoutSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsContinueSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList**](GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList.md) |  | 


#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



[**GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList**](GithubComArgoprojLabsArgoDataflowApiV1alpha1PipelineList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_logs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} pipeline_logs(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.pipeline_log_entry import PipelineLogEntry
from argo_workflows.model.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.pipeline_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->pipeline_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'name': "name_example",
        'stepName': "stepName_example",
        'grep': "grep_example",
        'podLogOptions.container': "podLogOptions.container_example",
        'podLogOptions.follow': True,
        'podLogOptions.previous': True,
        'podLogOptions.sinceSeconds': "podLogOptions.sinceSeconds_example",
        'podLogOptions.sinceTime.seconds': "podLogOptions.sinceTime.seconds_example",
        'podLogOptions.sinceTime.nanos': 1,
        'podLogOptions.timestamps': True,
        'podLogOptions.tailLines': "podLogOptions.tailLines_example",
        'podLogOptions.limitBytes': "podLogOptions.limitBytes_example",
        'podLogOptions.insecureSkipTLSVerifyBackend': True,
    }
    try:
        api_response = api_instance.pipeline_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->pipeline_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
stepName | StepNameSchema | | optional
grep | GrepSchema | | optional
podLogOptions.container | PodLogOptionsContainerSchema | | optional
podLogOptions.follow | PodLogOptionsFollowSchema | | optional
podLogOptions.previous | PodLogOptionsPreviousSchema | | optional
podLogOptions.sinceSeconds | PodLogOptionsSinceSecondsSchema | | optional
podLogOptions.sinceTime.seconds | PodLogOptionsSinceTimeSecondsSchema | | optional
podLogOptions.sinceTime.nanos | PodLogOptionsSinceTimeNanosSchema | | optional
podLogOptions.timestamps | PodLogOptionsTimestampsSchema | | optional
podLogOptions.tailLines | PodLogOptionsTailLinesSchema | | optional
podLogOptions.limitBytes | PodLogOptionsLimitBytesSchema | | optional
podLogOptions.insecureSkipTLSVerifyBackend | PodLogOptionsInsecureSkipTLSVerifyBackendSchema | | optional


#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StepNameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### GrepSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsContainerSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsFollowSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### PodLogOptionsPreviousSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### PodLogOptionsSinceSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsSinceTimeSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsSinceTimeNanosSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

#### PodLogOptionsTimestampsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### PodLogOptionsTailLinesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsLimitBytesSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### PodLogOptionsInsecureSkipTLSVerifyBackendSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.(streaming responses)
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**PipelineLogEntry**](PipelineLogEntry.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_pipeline**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} restart_pipeline(namespacename)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'name': "name_example",
    }
    try:
        api_response = api_instance.restart_pipeline(
            path_params=path_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->restart_pipeline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
name | NameSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### NameSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_pipelines**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} watch_pipelines(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.pipeline_pipeline_watch_event import PipelinePipelineWatchEvent
from argo_workflows.model.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.watch_pipelines(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->watch_pipelines: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'listOptions.labelSelector': "listOptions.labelSelector_example",
        'listOptions.fieldSelector': "listOptions.fieldSelector_example",
        'listOptions.watch': True,
        'listOptions.allowWatchBookmarks': True,
        'listOptions.resourceVersion': "listOptions.resourceVersion_example",
        'listOptions.resourceVersionMatch': "listOptions.resourceVersionMatch_example",
        'listOptions.timeoutSeconds': "listOptions.timeoutSeconds_example",
        'listOptions.limit': "listOptions.limit_example",
        'listOptions.continue': "listOptions.continue_example",
    }
    try:
        api_response = api_instance.watch_pipelines(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->watch_pipelines: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
listOptions.labelSelector | ListOptionsLabelSelectorSchema | | optional
listOptions.fieldSelector | ListOptionsFieldSelectorSchema | | optional
listOptions.watch | ListOptionsWatchSchema | | optional
listOptions.allowWatchBookmarks | ListOptionsAllowWatchBookmarksSchema | | optional
listOptions.resourceVersion | ListOptionsResourceVersionSchema | | optional
listOptions.resourceVersionMatch | ListOptionsResourceVersionMatchSchema | | optional
listOptions.timeoutSeconds | ListOptionsTimeoutSecondsSchema | | optional
listOptions.limit | ListOptionsLimitSchema | | optional
listOptions.continue | ListOptionsContinueSchema | | optional


#### ListOptionsLabelSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsFieldSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsWatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsAllowWatchBookmarksSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsResourceVersionMatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsTimeoutSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsContinueSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.(streaming responses)
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**PipelinePipelineWatchEvent**](PipelinePipelineWatchEvent.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_steps**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} watch_steps(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import pipeline_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.pipeline_step_watch_event import PipelineStepWatchEvent
from argo_workflows.model.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:2746
# See configuration.py for a list of all supported configuration parameters.
configuration = argo_workflows.Configuration(
    host = "http://localhost:2746"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API client
with argo_workflows.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_service_api.PipelineServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.watch_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->watch_steps: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'listOptions.labelSelector': "listOptions.labelSelector_example",
        'listOptions.fieldSelector': "listOptions.fieldSelector_example",
        'listOptions.watch': True,
        'listOptions.allowWatchBookmarks': True,
        'listOptions.resourceVersion': "listOptions.resourceVersion_example",
        'listOptions.resourceVersionMatch': "listOptions.resourceVersionMatch_example",
        'listOptions.timeoutSeconds': "listOptions.timeoutSeconds_example",
        'listOptions.limit': "listOptions.limit_example",
        'listOptions.continue': "listOptions.continue_example",
    }
    try:
        api_response = api_instance.watch_steps(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling PipelineServiceApi->watch_steps: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
listOptions.labelSelector | ListOptionsLabelSelectorSchema | | optional
listOptions.fieldSelector | ListOptionsFieldSelectorSchema | | optional
listOptions.watch | ListOptionsWatchSchema | | optional
listOptions.allowWatchBookmarks | ListOptionsAllowWatchBookmarksSchema | | optional
listOptions.resourceVersion | ListOptionsResourceVersionSchema | | optional
listOptions.resourceVersionMatch | ListOptionsResourceVersionMatchSchema | | optional
listOptions.timeoutSeconds | ListOptionsTimeoutSecondsSchema | | optional
listOptions.limit | ListOptionsLimitSchema | | optional
listOptions.continue | ListOptionsContinueSchema | | optional


#### ListOptionsLabelSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsFieldSelectorSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsWatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsAllowWatchBookmarksSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | 

#### ListOptionsResourceVersionSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsResourceVersionMatchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsTimeoutSecondsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### ListOptionsContinueSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | A successful response.(streaming responses)
default | ApiResponseForDefault | An unexpected error response.

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**GrpcGatewayRuntimeStreamError**](GrpcGatewayRuntimeStreamError.md) |  | [optional] 
**result** | [**PipelineStepWatchEvent**](PipelineStepWatchEvent.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

#### ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GrpcGatewayRuntimeError**](GrpcGatewayRuntimeError.md) |  | 



**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

