# IoArgoprojEventsV1alpha1Template

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**Affinity**](Affinity.md) |  | [optional] 
**container** | [**Container**](Container.md) |  | [optional] 
**imagePullSecrets** | **[LocalObjectReference]** |  | [optional] 
**metadata** | [**IoArgoprojEventsV1alpha1Metadata**](IoArgoprojEventsV1alpha1Metadata.md) |  | [optional] 
**nodeSelector** | **{str: (str,)}** |  | [optional] 
**priority** | **int** |  | [optional] 
**priorityClassName** | **str** |  | [optional] 
**securityContext** | [**PodSecurityContext**](PodSecurityContext.md) |  | [optional] 
**serviceAccountName** | **str** |  | [optional] 
**tolerations** | **[Toleration]** |  | [optional] 
**volumes** | **[Volume]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

