# IoArgoprojEventsV1alpha1HTTPTrigger

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basicAuth** | [**IoArgoprojEventsV1alpha1BasicAuth**](IoArgoprojEventsV1alpha1BasicAuth.md) |  | [optional] 
**headers** | **{str: (str,)}** |  | [optional] 
**method** | **str** |  | [optional] 
**parameters** | **[IoArgoprojEventsV1alpha1TriggerParameter]** | Parameters is the list of key-value extracted from event&#x27;s payload that are applied to the HTTP trigger resource. | [optional] 
**payload** | **[IoArgoprojEventsV1alpha1TriggerParameter]** |  | [optional] 
**secureHeaders** | **[IoArgoprojEventsV1alpha1SecureHeader]** |  | [optional] 
**timeout** | **str** |  | [optional] 
**tls** | [**IoArgoprojEventsV1alpha1TLSConfig**](IoArgoprojEventsV1alpha1TLSConfig.md) |  | [optional] 
**url** | **str** | URL refers to the URL to send HTTP request to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

