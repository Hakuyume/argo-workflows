# IoArgoprojWorkflowV1alpha1HTTPArtifact

HTTPArtifact allows a file served on HTTP to be placed as an input artifact in a container

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoArgoprojWorkflowV1alpha1HTTPAuth**](IoArgoprojWorkflowV1alpha1HTTPAuth.md) |  | [optional] 
**headers** | **[IoArgoprojWorkflowV1alpha1Header]** | Headers are an optional list of headers to send with HTTP requests for artifacts | [optional] 
**url** | **str** | URL of the artifact | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

