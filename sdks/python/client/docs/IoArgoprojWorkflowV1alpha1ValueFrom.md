# IoArgoprojWorkflowV1alpha1ValueFrom

ValueFrom describes a location in which to obtain the value to a parameter

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configMapKeyRef** | [**ConfigMapKeySelector**](ConfigMapKeySelector.md) |  | [optional] 
**default** | **str** | Default specifies a value to be used if retrieving the value from the specified source fails | [optional] 
**event** | **str** | Selector (https://github.com/antonmedv/expr) that is evaluated against the event to get the value of the parameter. E.g. &#x60;payload.message&#x60; | [optional] 
**expression** | **str** | Expression, if defined, is evaluated to specify the value for the parameter | [optional] 
**jqFilter** | **str** | JQFilter expression against the resource object in resource templates | [optional] 
**jsonPath** | **str** | JSONPath of a resource to retrieve an output parameter value from in resource templates | [optional] 
**parameter** | **str** | Parameter reference to a step or dag task in which to retrieve an output parameter value from (e.g. &#x27;{{steps.mystep.outputs.myparam}}&#x27;) | [optional] 
**path** | **str** | Path in the container to retrieve an output parameter value from in container templates | [optional] 
**supplied** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | SuppliedValueFrom is a placeholder for a value to be filled in directly, either through the CLI, API, etc. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

