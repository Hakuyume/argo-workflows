# EnvVarSource

EnvVarSource represents a source for the value of an EnvVar.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configMapKeyRef** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**fieldRef** | [**ObjectFieldSelector**](ObjectFieldSelector.md) |  | [optional] 
**resourceFieldRef** | [**ResourceFieldSelector**](ResourceFieldSelector.md) |  | [optional] 
**secretKeyRef** | [**SecretKeySelector**](SecretKeySelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

