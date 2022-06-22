# IoArgoprojWorkflowV1alpha1Prometheus

Prometheus is a prometheus metric to be emitted

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter** | [**IoArgoprojWorkflowV1alpha1Counter**](IoArgoprojWorkflowV1alpha1Counter.md) |  | [optional] 
**gauge** | [**IoArgoprojWorkflowV1alpha1Gauge**](IoArgoprojWorkflowV1alpha1Gauge.md) |  | [optional] 
**help** | **str** | Help is a string that describes the metric | 
**histogram** | [**IoArgoprojWorkflowV1alpha1Histogram**](IoArgoprojWorkflowV1alpha1Histogram.md) |  | [optional] 
**labels** | **[IoArgoprojWorkflowV1alpha1MetricLabel]** | Labels is a list of metric labels | [optional] 
**name** | **str** | Name is the name of the metric | 
**when** | **str** | When is a conditional statement that decides when to emit the metric | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

