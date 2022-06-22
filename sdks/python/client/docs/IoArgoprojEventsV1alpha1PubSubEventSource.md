# IoArgoprojEventsV1alpha1PubSubEventSource

PubSubEventSource refers to event-source for GCP PubSub related events.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentialSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**deleteSubscriptionOnFinish** | **bool** |  | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**jsonBody** | **bool** |  | [optional] 
**metadata** | **{str: (str,)}** |  | [optional] 
**projectID** | **str** |  | [optional] 
**subscriptionID** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**topicProjectID** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

