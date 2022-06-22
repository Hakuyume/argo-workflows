# IoArgoprojEventsV1alpha1BitbucketServerEventSource

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**bitbucketserverBaseURL** | **str** |  | [optional] 
**deleteHookOnFinish** | **bool** |  | [optional] 
**events** | **[str]** |  | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**metadata** | **{str: (str,)}** |  | [optional] 
**projectKey** | **str** |  | [optional] 
**repositories** | **[IoArgoprojEventsV1alpha1BitbucketServerRepository]** |  | [optional] 
**repositorySlug** | **str** |  | [optional] 
**webhook** | [**IoArgoprojEventsV1alpha1WebhookContext**](IoArgoprojEventsV1alpha1WebhookContext.md) |  | [optional] 
**webhookSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

