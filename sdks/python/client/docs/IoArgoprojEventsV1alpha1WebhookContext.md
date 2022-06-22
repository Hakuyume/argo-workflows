# IoArgoprojEventsV1alpha1WebhookContext

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**endpoint** | **str** |  | [optional] 
**metadata** | **{str: (str,)}** |  | [optional] 
**method** | **str** |  | [optional] 
**port** | **str** | Port on which HTTP server is listening for incoming events. | [optional] 
**serverCertSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**serverKeySecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**url** | **str** | URL is the url of the server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

