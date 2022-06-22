# argo_workflows.EventServiceApi

All URIs are relative to *http://localhost:2746*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_workflow_event_bindings**](EventServiceApi.md#list_workflow_event_bindings) | **GET** /api/v1/workflow-event-bindings/{namespace} | 
[**receive_event**](EventServiceApi.md#receive_event) | **POST** /api/v1/events/{namespace}/{discriminator} | 

# **list_workflow_event_bindings**
> IoArgoprojWorkflowV1alpha1WorkflowEventBindingList list_workflow_event_bindings(namespace)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_service_api
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_event_binding_list import IoArgoprojWorkflowV1alpha1WorkflowEventBindingList
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
    api_instance = event_service_api.EventServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_workflow_event_bindings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventServiceApi->list_workflow_event_bindings: %s\n" % e)

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
        api_response = api_instance.list_workflow_event_bindings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventServiceApi->list_workflow_event_bindings: %s\n" % e)
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
[**IoArgoprojWorkflowV1alpha1WorkflowEventBindingList**](IoArgoprojWorkflowV1alpha1WorkflowEventBindingList.md) |  | 


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



[**IoArgoprojWorkflowV1alpha1WorkflowEventBindingList**](IoArgoprojWorkflowV1alpha1WorkflowEventBindingList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_event**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} receive_event(namespacediscriminatorbody)



### Example

* Api Key Authentication (BearerToken):
```python
import argo_workflows
from argo_workflows.api import event_service_api
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
    api_instance = event_service_api.EventServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
        'discriminator': "discriminator_example",
    }
    body = dict()
    try:
        api_response = api_instance.receive_event(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except argo_workflows.ApiException as e:
        print("Exception when calling EventServiceApi->receive_event: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson

Item expands a single workflow step into multiple parallel steps The value of Item can be a map, string, bool, or number

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 
discriminator | DiscriminatorSchema | | 

#### NamespaceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### DiscriminatorSchema

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

