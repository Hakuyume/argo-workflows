# IoArgoprojEventsV1alpha1PulsarEventSource

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authTokenSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**connectionBackoff** | [**IoArgoprojEventsV1alpha1Backoff**](IoArgoprojEventsV1alpha1Backoff.md) |  | [optional] 
**filter** | [**IoArgoprojEventsV1alpha1EventSourceFilter**](IoArgoprojEventsV1alpha1EventSourceFilter.md) |  | [optional] 
**jsonBody** | **bool** |  | [optional] 
**metadata** | **{str: (str,)}** |  | [optional] 
**tls** | [**IoArgoprojEventsV1alpha1TLSConfig**](IoArgoprojEventsV1alpha1TLSConfig.md) |  | [optional] 
**tlsAllowInsecureConnection** | **bool** |  | [optional] 
**tlsTrustCertsSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**tlsValidateHostname** | **bool** |  | [optional] 
**topics** | **[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

