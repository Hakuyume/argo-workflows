# IoArgoprojEventsV1alpha1GitlabEventSource

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**deleteHookOnFinish** | **bool** |  | [optional] 
**enableSSLVerification** | **bool** |  | [optional] 
**events** | **[str]** | Events are gitlab event to listen to. Refer https://github.com/xanzy/go-gitlab/blob/bf34eca5d13a9f4c3f501d8a97b8ac226d55e4d9/projects.go#L794. | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**gitlabBaseURL** | **str** |  | [optional] 
**metadata** | **{str: (str,)}** |  | [optional] 
**projectID** | **str** |  | [optional] 
**projects** | **[str]** |  | [optional] 
**secretToken** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**webhook** | [**IoArgoprojEventsV1alpha1WebhookContext**](IoArgoprojEventsV1alpha1WebhookContext.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

