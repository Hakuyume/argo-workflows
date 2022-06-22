# IoArgoprojWorkflowV1alpha1SubmitOpts

SubmitOpts are workflow submission options

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **str** | Annotations adds to metadata.labels | [optional] 
**dryRun** | **bool** | DryRun validates the workflow on the client-side without creating it. This option is not supported in API | [optional] 
**entryPoint** | **str** | Entrypoint overrides spec.entrypoint | [optional] 
**generateName** | **str** | GenerateName overrides metadata.generateName | [optional] 
**labels** | **str** | Labels adds to metadata.labels | [optional] 
**name** | **str** | Name overrides metadata.name | [optional] 
**ownerReference** | [**OwnerReference**](OwnerReference.md) |  | [optional] 
**parameters** | **[str]** | Parameters passes input parameters to workflow | [optional] 
**podPriorityClassName** | **str** | Set the podPriorityClassName of the workflow | [optional] 
**priority** | **int** | Priority is used if controller is configured to process limited number of workflows in parallel, higher priority workflows are processed first. | [optional] 
**serverDryRun** | **bool** | ServerDryRun validates the workflow on the server-side without creating it | [optional] 
**serviceAccount** | **str** | ServiceAccount runs all pods in the workflow using specified ServiceAccount. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

