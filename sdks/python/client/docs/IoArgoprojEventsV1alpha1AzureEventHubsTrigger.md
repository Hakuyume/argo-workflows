# IoArgoprojEventsV1alpha1AzureEventHubsTrigger

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** |  | [optional] 
**hubName** | **str** |  | [optional] 
**parameters** | **[IoArgoprojEventsV1alpha1TriggerParameter]** |  | [optional] 
**payload** | **[IoArgoprojEventsV1alpha1TriggerParameter]** | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**sharedAccessKey** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**sharedAccessKeyName** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

