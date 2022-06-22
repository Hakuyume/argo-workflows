# IoArgoprojWorkflowV1alpha1WorkflowSpec

WorkflowSpec is the specification of a Workflow.

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeDeadlineSeconds** | **int** | Optional duration in seconds relative to the workflow start time which the workflow is allowed to run before the controller terminates the io.argoproj.workflow.v1alpha1. A value of zero is used to terminate a Running workflow | [optional] 
**affinity** | [**Affinity**](Affinity.md) |  | [optional] 
**archiveLogs** | **bool** | ArchiveLogs indicates if the container logs should be archived | [optional] 
**arguments** | [**IoArgoprojWorkflowV1alpha1Arguments**](IoArgoprojWorkflowV1alpha1Arguments.md) |  | [optional] 
**artifactGC** | [**IoArgoprojWorkflowV1alpha1ArtifactGC**](IoArgoprojWorkflowV1alpha1ArtifactGC.md) |  | [optional] 
**artifactRepositoryRef** | [**IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef**](IoArgoprojWorkflowV1alpha1ArtifactRepositoryRef.md) |  | [optional] 
**automountServiceAccountToken** | **bool** | AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false. | [optional] 
**dnsConfig** | [**PodDNSConfig**](PodDNSConfig.md) |  | [optional] 
**dnsPolicy** | **str** | Set DNS policy for the pod. Defaults to \&quot;ClusterFirst\&quot;. Valid values are &#x27;ClusterFirstWithHostNet&#x27;, &#x27;ClusterFirst&#x27;, &#x27;Default&#x27; or &#x27;None&#x27;. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to &#x27;ClusterFirstWithHostNet&#x27;. | [optional] 
**entrypoint** | **str** | Entrypoint is a template reference to the starting point of the io.argoproj.workflow.v1alpha1. | [optional] 
**executor** | [**IoArgoprojWorkflowV1alpha1ExecutorConfig**](IoArgoprojWorkflowV1alpha1ExecutorConfig.md) |  | [optional] 
**hooks** | **{str: (IoArgoprojWorkflowV1alpha1LifecycleHook,)}** | Hooks holds the lifecycle hook which is invoked at lifecycle of step, irrespective of the success, failure, or error status of the primary step | [optional] 
**hostAliases** | **[HostAlias]** |  | [optional] 
**hostNetwork** | **bool** | Host networking requested for this workflow pod. Default to false. | [optional] 
**imagePullSecrets** | **[LocalObjectReference]** | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod | [optional] 
**metrics** | [**IoArgoprojWorkflowV1alpha1Metrics**](IoArgoprojWorkflowV1alpha1Metrics.md) |  | [optional] 
**nodeSelector** | **{str: (str,)}** | NodeSelector is a selector which will result in all pods of the workflow to be scheduled on the selected node(s). This is able to be overridden by a nodeSelector specified in the template. | [optional] 
**onExit** | **str** | OnExit is a template reference which is invoked at the end of the workflow, irrespective of the success, failure, or error of the primary io.argoproj.workflow.v1alpha1. | [optional] 
**parallelism** | **int** | Parallelism limits the max total parallel pods that can execute at the same time in a workflow | [optional] 
**podDisruptionBudget** | [**IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec**](IoK8sApiPolicyV1beta1PodDisruptionBudgetSpec.md) |  | [optional] 
**podGC** | [**IoArgoprojWorkflowV1alpha1PodGC**](IoArgoprojWorkflowV1alpha1PodGC.md) |  | [optional] 
**podMetadata** | [**IoArgoprojWorkflowV1alpha1Metadata**](IoArgoprojWorkflowV1alpha1Metadata.md) |  | [optional] 
**podPriority** | **int** | Priority to apply to workflow pods. | [optional] 
**podPriorityClassName** | **str** | PriorityClassName to apply to workflow pods. | [optional] 
**podSpecPatch** | **str** | PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits). | [optional] 
**priority** | **int** | Priority is used if controller is configured to process limited number of workflows in parallel. Workflows with higher priority are processed first. | [optional] 
**retryStrategy** | [**IoArgoprojWorkflowV1alpha1RetryStrategy**](IoArgoprojWorkflowV1alpha1RetryStrategy.md) |  | [optional] 
**schedulerName** | **str** | Set scheduler name for all pods. Will be overridden if container/script template&#x27;s scheduler name is set. Default scheduler will be used if neither specified. | [optional] 
**securityContext** | [**PodSecurityContext**](PodSecurityContext.md) |  | [optional] 
**serviceAccountName** | **str** | ServiceAccountName is the name of the ServiceAccount to run all pods of the workflow as. | [optional] 
**shutdown** | **str** | Shutdown will shutdown the workflow according to its ShutdownStrategy | [optional] 
**suspend** | **bool** | Suspend will suspend the workflow and prevent execution of any future steps in the workflow | [optional] 
**synchronization** | [**IoArgoprojWorkflowV1alpha1Synchronization**](IoArgoprojWorkflowV1alpha1Synchronization.md) |  | [optional] 
**templateDefaults** | [**IoArgoprojWorkflowV1alpha1Template**](IoArgoprojWorkflowV1alpha1Template.md) |  | [optional] 
**templates** | **[IoArgoprojWorkflowV1alpha1Template]** | Templates is a list of workflow templates used in a workflow | [optional] 
**tolerations** | **[Toleration]** | Tolerations to apply to workflow pods. | [optional] 
**ttlStrategy** | [**IoArgoprojWorkflowV1alpha1TTLStrategy**](IoArgoprojWorkflowV1alpha1TTLStrategy.md) |  | [optional] 
**volumeClaimGC** | [**IoArgoprojWorkflowV1alpha1VolumeClaimGC**](IoArgoprojWorkflowV1alpha1VolumeClaimGC.md) |  | [optional] 
**volumeClaimTemplates** | **[PersistentVolumeClaim]** | VolumeClaimTemplates is a list of claims that containers are allowed to reference. The Workflow controller will create the claims at the beginning of the workflow and delete the claims upon completion of the workflow | [optional] 
**volumes** | **[Volume]** | Volumes is a list of volumes that can be mounted by containers in a io.argoproj.workflow.v1alpha1. | [optional] 
**workflowMetadata** | [**IoArgoprojWorkflowV1alpha1WorkflowMetadata**](IoArgoprojWorkflowV1alpha1WorkflowMetadata.md) |  | [optional] 
**workflowTemplateRef** | [**IoArgoprojWorkflowV1alpha1WorkflowTemplateRef**](IoArgoprojWorkflowV1alpha1WorkflowTemplateRef.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

