# IoArgoprojEventsV1alpha1PulsarTrigger

PulsarTrigger refers to the specification of the Pulsar trigger.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authTokenSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**connectionBackoff** | [**IoArgoprojEventsV1alpha1Backoff**](IoArgoprojEventsV1alpha1Backoff.md) |  | [optional] 
**parameters** | **[IoArgoprojEventsV1alpha1TriggerParameter]** | Parameters is the list of parameters that is applied to resolved Kafka trigger object. | [optional] 
**payload** | **[IoArgoprojEventsV1alpha1TriggerParameter]** | Payload is the list of key-value extracted from an event payload to construct the request payload. | [optional] 
**tls** | [**IoArgoprojEventsV1alpha1TLSConfig**](IoArgoprojEventsV1alpha1TLSConfig.md) |  | [optional] 
**tlsAllowInsecureConnection** | **bool** |  | [optional] 
**tlsTrustCertsSecret** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**tlsValidateHostname** | **bool** |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

