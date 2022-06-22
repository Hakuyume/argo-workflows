# IoArgoprojEventsV1alpha1SQSEventSource

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKey** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**dlq** | **bool** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**jsonBody** | **bool** |  | [optional] 
**metadata** | **{str: (str,)}** |  | [optional] 
**queue** | **str** |  | [optional] 
**queueAccountId** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**roleARN** | **str** |  | [optional] 
**secretKey** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**waitTimeSeconds** | **str** | WaitTimeSeconds is The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

