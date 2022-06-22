# IoArgoprojWorkflowV1alpha1WorkflowStatus

WorkflowStatus contains overall status information about a workflow

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactRepositoryRef** | [**IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus**](IoArgoprojWorkflowV1alpha1ArtifactRepositoryRefStatus.md) |  | [optional] 
**compressedNodes** | **str** | Compressed and base64 decoded Nodes map | [optional] 
**conditions** | **[IoArgoprojWorkflowV1alpha1Condition]** | Conditions is a list of conditions the Workflow may have | [optional] 
**estimatedDuration** | **int** | EstimatedDuration in seconds. | [optional] 
**finishedAt** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | A human readable message indicating details about why the workflow is in this condition. | [optional] 
**nodes** | **{str: (IoArgoprojWorkflowV1alpha1NodeStatus,)}** | Nodes is a mapping between a node ID and the node&#x27;s status. | [optional] 
**offloadNodeStatusVersion** | **str** | Whether on not node status has been offloaded to a database. If exists, then Nodes and CompressedNodes will be empty. This will actually be populated with a hash of the offloaded data. | [optional] 
**outputs** | [**IoArgoprojWorkflowV1alpha1Outputs**](IoArgoprojWorkflowV1alpha1Outputs.md) |  | [optional] 
**persistentVolumeClaims** | **[Volume]** | PersistentVolumeClaims tracks all PVCs that were created as part of the io.argoproj.workflow.v1alpha1. The contents of this list are drained at the end of the workflow. | [optional] 
**phase** | **str** | Phase a simple, high-level summary of where the workflow is in its lifecycle. | [optional] 
**progress** | **str** | Progress to completion | [optional] 
**resourcesDuration** | **{str: (int,)}** | ResourcesDuration is the total for the workflow | [optional] 
**startedAt** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**storedTemplates** | **{str: (IoArgoprojWorkflowV1alpha1Template,)}** | StoredTemplates is a mapping between a template ref and the node&#x27;s status. | [optional] 
**storedWorkflowTemplateSpec** | [**IoArgoprojWorkflowV1alpha1WorkflowSpec**](IoArgoprojWorkflowV1alpha1WorkflowSpec.md) |  | [optional] 
**synchronization** | [**IoArgoprojWorkflowV1alpha1SynchronizationStatus**](IoArgoprojWorkflowV1alpha1SynchronizationStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

